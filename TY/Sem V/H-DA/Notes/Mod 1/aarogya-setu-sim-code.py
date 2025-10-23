# Aarogya Setu Big Data Analytics - Executable Code Examples
# This file contains working code implementations for all 4 types of data analysis

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime, timedelta
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix, roc_auc_score
from sklearn.preprocessing import StandardScaler
from scipy.optimize import minimize
import networkx as nx
import warnings
warnings.filterwarnings('ignore')

# Generate synthetic Aarogya Setu-like data
np.random.seed(42)

def generate_synthetic_data():
    """Generate synthetic data resembling Aarogya Setu dataset"""
    
    # Generate 10,000 user records
    n_users = 10000
    
    # User demographics
    user_data = pd.DataFrame({
        'user_id': range(n_users),
        'age': np.random.normal(35, 15, n_users).astype(int).clip(18, 80),
        'state_code': np.random.choice(['MH', 'DL', 'KA', 'TN', 'UP', 'WB'], n_users),
        'urban_rural': np.random.choice(['urban', 'rural'], n_users, p=[0.7, 0.3]),
        'app_install_date': pd.date_range('2020-04-01', '2020-06-01', periods=n_users)
    })
    
    # Generate contact events (50,000 events)
    n_contacts = 50000
    contact_data = pd.DataFrame({
        'contact_id': range(n_contacts),
        'user_id_1': np.random.randint(0, n_users, n_contacts),
        'user_id_2': np.random.randint(0, n_users, n_contacts),
        'contact_date': pd.date_range('2020-04-01', '2020-08-31', periods=n_contacts),
        'duration_minutes': np.random.exponential(15, n_contacts),
        'distance_meters': np.random.gamma(2, 2, n_contacts),
        'location_type': np.random.choice(['home', 'office', 'transport', 'market', 'hospital'], n_contacts)
    })
    
    # Generate health data
    health_data = pd.DataFrame({
        'user_id': np.random.choice(range(n_users), n_users//2, replace=False),
        'symptoms_reported': np.random.choice([0, 1], n_users//2, p=[0.8, 0.2]),
        'test_result': np.random.choice(['negative', 'positive', 'pending'], n_users//2, p=[0.85, 0.10, 0.05]),
        'vaccination_status': np.random.choice(['none', 'partial', 'full'], n_users//2, p=[0.4, 0.3, 0.3]),
        'test_date': pd.date_range('2020-04-01', '2020-08-31', periods=n_users//2)
    })
    
    # Generate location data
    location_data = pd.DataFrame({
        'user_id': np.repeat(range(min(1000, n_users)), 100),  # 100 location points per user (subset)
        'timestamp': pd.date_range('2020-04-01', '2020-08-31', periods=100000),
        'latitude': np.random.uniform(18.9, 19.3, 100000),  # Mumbai coordinates
        'longitude': np.random.uniform(72.8, 73.0, 100000),
        'accuracy_meters': np.random.exponential(50, 100000)
    })
    
    return user_data, contact_data, health_data, location_data

# Generate data
print("Generating synthetic Aarogya Setu data...")
user_data, contact_data, health_data, location_data = generate_synthetic_data()
print(f"Generated {len(user_data)} users, {len(contact_data)} contacts, {len(health_data)} health records")

# =============================================================================
# 1. DESCRIPTIVE ANALYTICS: "What Happened?"
# =============================================================================

def descriptive_analytics():
    """Analyze what happened in the data - patterns and trends"""
    
    print("\n" + "="*60)
    print("1. DESCRIPTIVE ANALYTICS")
    print("="*60)
    
    # Basic statistics
    print("\n--- Basic Statistics ---")
    print(f"Total Users: {len(user_data):,}")
    print(f"Total Contact Events: {len(contact_data):,}")
    print(f"Average Age: {user_data['age'].mean():.1f} years")
    print(f"Urban vs Rural: {user_data['urban_rural'].value_counts().to_dict()}")
    
    # Daily contact patterns
    contact_daily = contact_data.groupby(contact_data['contact_date'].dt.date).agg({
        'contact_id': 'count',
        'duration_minutes': 'mean',
        'distance_meters': 'mean'
    }).rename(columns={'contact_id': 'daily_contacts'})
    
    print(f"\n--- Daily Contact Patterns ---")
    print(f"Average daily contacts: {contact_daily['daily_contacts'].mean():.0f}")
    print(f"Peak contact day: {contact_daily['daily_contacts'].max()} contacts")
    print(f"Average contact duration: {contact_daily['duration_minutes'].mean():.1f} minutes")
    
    # State-wise distribution
    state_stats = user_data.groupby('state_code').agg({
        'user_id': 'count',
        'age': 'mean'
    }).rename(columns={'user_id': 'user_count'}).sort_values('user_count', ascending=False)
    
    print(f"\n--- State-wise User Distribution ---")
    print(state_stats.head())
    
    # Contact network analysis
    print(f"\n--- Contact Network Analysis ---")
    G = nx.from_pandas_edgelist(contact_data, 'user_id_1', 'user_id_2')
    print(f"Network nodes (users): {G.number_of_nodes()}")
    print(f"Network edges (contacts): {G.number_of_edges()}")
    print(f"Average connections per user: {G.number_of_edges() * 2 / G.number_of_nodes():.1f}")
    
    if G.number_of_nodes() > 0:
        try:
            # Calculate centrality for subset to avoid computation issues
            largest_cc = max(nx.connected_components(G), key=len)
            subgraph = G.subgraph(largest_cc)
            if len(subgraph) > 100:
                subgraph = G.subgraph(list(largest_cc)[:100])
            
            centrality = nx.degree_centrality(subgraph)
            top_users = sorted(centrality.items(), key=lambda x: x[1], reverse=True)[:5]
            print(f"Top 5 most connected users: {top_users}")
        except:
            print("Network centrality calculation skipped (complex network)")
    
    # Health statistics
    if len(health_data) > 0:
        health_stats = health_data.groupby('test_result').size()
        print(f"\n--- Health Statistics ---")
        print(f"Test results distribution:")
        for result, count in health_stats.items():
            print(f"  {result}: {count} ({count/len(health_data)*100:.1f}%)")
    
    return contact_daily, state_stats

# =============================================================================
# 2. DIAGNOSTIC ANALYTICS: "Why Did It Happen?"
# =============================================================================

def diagnostic_analytics():
    """Analyze why certain patterns occurred - correlation and causation"""
    
    print("\n" + "="*60)
    print("2. DIAGNOSTIC ANALYTICS")
    print("="*60)
    
    # Merge data for analysis
    user_contact_summary = contact_data.groupby('user_id_1').agg({
        'contact_id': 'count',
        'duration_minutes': 'mean',
        'distance_meters': 'mean'
    }).rename(columns={
        'contact_id': 'total_contacts',
        'duration_minutes': 'avg_duration',
        'distance_meters': 'avg_distance'
    })
    
    # Merge with user data
    analysis_data = user_data.merge(user_contact_summary, left_on='user_id', right_index=True, how='left')
    analysis_data = analysis_data.merge(health_data[['user_id', 'symptoms_reported', 'test_result']], 
                                      on='user_id', how='left')
    
    # Fill missing values
    analysis_data['total_contacts'] = analysis_data['total_contacts'].fillna(0)
    analysis_data['symptoms_reported'] = analysis_data['symptoms_reported'].fillna(0)
    analysis_data['has_positive_test'] = (analysis_data['test_result'] == 'positive').astype(int)
    
    # Age group analysis
    analysis_data['age_group'] = pd.cut(analysis_data['age'], 
                                      bins=[0, 30, 50, 70, 100], 
                                      labels=['18-30', '31-50', '51-70', '70+'])
    
    print("\n--- Correlation Analysis ---")
    
    # Correlation between contacts and symptoms
    if analysis_data['total_contacts'].var() > 0 and analysis_data['symptoms_reported'].var() > 0:
        contact_symptom_corr = analysis_data['total_contacts'].corr(analysis_data['symptoms_reported'])
        print(f"Correlation between total contacts and symptoms: {contact_symptom_corr:.3f}")
    
    # Age group vs contact patterns
    age_contact_stats = analysis_data.groupby('age_group').agg({
        'total_contacts': 'mean',
        'symptoms_reported': 'mean',
        'has_positive_test': 'mean'
    })
    
    print(f"\n--- Age Group Analysis ---")
    print(age_contact_stats)
    
    # Urban vs Rural analysis
    urban_rural_stats = analysis_data.groupby('urban_rural').agg({
        'total_contacts': 'mean',
        'avg_duration': 'mean',
        'symptoms_reported': 'mean',
        'has_positive_test': 'mean'
    })
    
    print(f"\n--- Urban vs Rural Analysis ---")
    print(urban_rural_stats)
    
    # State-wise risk analysis
    state_risk = analysis_data.groupby('state_code').agg({
        'total_contacts': 'mean',
        'symptoms_reported': 'mean',
        'has_positive_test': 'mean'
    }).sort_values('has_positive_test', ascending=False)
    
    print(f"\n--- State-wise Risk Analysis ---")
    print(state_risk)
    
    # Contact location type analysis
    location_risk = contact_data.groupby('location_type').agg({
        'duration_minutes': 'mean',
        'distance_meters': 'mean',
        'contact_id': 'count'
    }).sort_values('duration_minutes', ascending=False)
    
    print(f"\n--- Contact Location Risk Analysis ---")
    print(location_risk)
    
    # Find potential super-spreader events
    super_spreader_threshold = analysis_data['total_contacts'].quantile(0.95)
    super_spreaders = analysis_data[analysis_data['total_contacts'] > super_spreader_threshold]
    
    print(f"\n--- Potential Super-spreader Analysis ---")
    print(f"Super-spreader threshold (95th percentile): {super_spreader_threshold:.0f} contacts")
    print(f"Number of potential super-spreaders: {len(super_spreaders)}")
    if len(super_spreaders) > 0:
        print(f"Average age of super-spreaders: {super_spreaders['age'].mean():.1f}")
        print(f"Super-spreader positive test rate: {super_spreaders['has_positive_test'].mean():.1%}")
    
    return analysis_data

# =============================================================================
# 3. PREDICTIVE ANALYTICS: "What Will Happen?"
# =============================================================================

def predictive_analytics(analysis_data):
    """Build predictive models to forecast outcomes"""
    
    print("\n" + "="*60)
    print("3. PREDICTIVE ANALYTICS")
    print("="*60)
    
    # Prepare features for prediction
    feature_columns = ['age', 'total_contacts', 'avg_duration', 'avg_distance']
    
    # Create additional features
    analysis_data['contact_intensity'] = analysis_data['total_contacts'] * analysis_data['avg_duration']
    analysis_data['urban_numeric'] = (analysis_data['urban_rural'] == 'urban').astype(int)
    
    feature_columns.extend(['contact_intensity', 'urban_numeric'])
    
    # Remove rows with missing values
    model_data = analysis_data[feature_columns + ['symptoms_reported', 'has_positive_test']].dropna()
    
    if len(model_data) < 100:
        print("Insufficient data for predictive modeling")
        return None
    
    print(f"Model training data: {len(model_data)} samples")
    
    # Model 1: Predict symptom reporting
    print(f"\n--- Model 1: Symptom Prediction ---")
    
    X_symptoms = model_data[feature_columns]
    y_symptoms = model_data['symptoms_reported']
    
    if y_symptoms.sum() > 10:  # Ensure we have enough positive cases
        X_train, X_test, y_train, y_test = train_test_split(X_symptoms, y_symptoms, test_size=0.3, random_state=42)
        
        # Scale features
        scaler = StandardScaler()
        X_train_scaled = scaler.fit_transform(X_train)
        X_test_scaled = scaler.transform(X_test)
        
        # Train Random Forest
        rf_symptoms = RandomForestClassifier(n_estimators=100, random_state=42)
        rf_symptoms.fit(X_train_scaled, y_train)
        
        # Predictions
        y_pred_symptoms = rf_symptoms.predict(X_test_scaled)
        y_prob_symptoms = rf_symptoms.predict_proba(X_test_scaled)[:, 1]
        
        print(f"Symptom Prediction Accuracy: {rf_symptoms.score(X_test_scaled, y_test):.3f}")
        if len(np.unique(y_test)) > 1:
            print(f"Symptom Prediction AUC: {roc_auc_score(y_test, y_prob_symptoms):.3f}")
        
        # Feature importance
        feature_importance = pd.DataFrame({
            'feature': feature_columns,
            'importance': rf_symptoms.feature_importances_
        }).sort_values('importance', ascending=False)
        
        print("\nTop Feature Importances for Symptom Prediction:")
        print(feature_importance.head())
    
    # Model 2: Risk scoring model
    print(f"\n--- Model 2: Risk Scoring Model ---")
    
    # Create risk score based on multiple factors
    analysis_data['risk_score'] = (
        (analysis_data['total_contacts'] / analysis_data['total_contacts'].max() * 0.4) +
        (analysis_data['contact_intensity'] / analysis_data['contact_intensity'].max() * 0.3) +
        (analysis_data['age'] / 80 * 0.2) +  # Age risk factor
        (analysis_data['urban_numeric'] * 0.1)  # Urban area risk
    )
    
    # Categorize risk levels
    analysis_data['risk_category'] = pd.cut(analysis_data['risk_score'], 
                                          bins=[0, 0.3, 0.6, 1.0], 
                                          labels=['Low', 'Medium', 'High'])
    
    risk_distribution = analysis_data['risk_category'].value_counts()
    print("Risk Score Distribution:")
    print(risk_distribution)
    
    # Time series prediction (simplified)
    print(f"\n--- Model 3: Time Series Forecasting ---")
    
    # Daily contact trend
    daily_contacts = contact_data.groupby(contact_data['contact_date'].dt.date)['contact_id'].count()
    daily_contacts.index = pd.to_datetime(daily_contacts.index)
    
    # Simple trend analysis
    daily_contacts_df = daily_contacts.reset_index()
    daily_contacts_df['day_number'] = range(len(daily_contacts_df))
    
    # Linear trend
    trend_coef = np.polyfit(daily_contacts_df['day_number'], daily_contacts_df['contact_id'], 1)
    
    print(f"Daily contact trend: {trend_coef[0]:.2f} contacts per day change")
    
    # Predict next 7 days
    last_day = len(daily_contacts_df)
    next_7_days = []
    for i in range(1, 8):
        predicted_contacts = trend_coef[0] * (last_day + i) + trend_coef[1]
        next_7_days.append(max(0, int(predicted_contacts)))
    
    print(f"Predicted contacts for next 7 days: {next_7_days}")
    
    return analysis_data, feature_importance if 'feature_importance' in locals() else None

# =============================================================================
# 4. PRESCRIPTIVE ANALYTICS: "What Should We Do?"
# =============================================================================

def prescriptive_analytics(analysis_data):
    """Provide recommendations and optimal actions"""
    
    print("\n" + "="*60)
    print("4. PRESCRIPTIVE ANALYTICS")
    print("="*60)
    
    # Resource allocation optimization
    print(f"\n--- Resource Allocation Optimization ---")
    
    # State-wise resource needs based on risk
    state_needs = analysis_data.groupby('state_code').agg({
        'risk_score': 'mean',
        'user_id': 'count',
        'has_positive_test': 'sum'
    }).rename(columns={'user_id': 'user_count', 'has_positive_test': 'positive_cases'})
    
    # Calculate priority score
    state_needs['priority_score'] = (
        state_needs['risk_score'] * 0.4 +
        (state_needs['user_count'] / state_needs['user_count'].max()) * 0.3 +
        (state_needs['positive_cases'] / state_needs['positive_cases'].max()) * 0.3
    )
    
    state_needs = state_needs.sort_values('priority_score', ascending=False)
    print("State Priority for Resource Allocation:")
    print(state_needs)
    
    # Testing center optimization
    print(f"\n--- Testing Center Placement Optimization ---")
    
    # Simplified facility location problem
    def optimize_testing_centers(demand_points, n_facilities=5):
        """Optimize placement of testing centers"""
        
        # Generate random coordinates for demand points (simplified)
        np.random.seed(42)
        locations = np.random.rand(len(demand_points), 2) * 100  # 100x100 grid
        demands = demand_points.values
        
        def objective(facility_coords):
            facility_coords = facility_coords.reshape(n_facilities, 2)
            total_cost = 0
            
            for i, (loc, demand) in enumerate(zip(locations, demands)):
                # Find closest facility
                distances = [np.linalg.norm(loc - facility) for facility in facility_coords]
                min_distance = min(distances)
                total_cost += demand * min_distance
            
            return total_cost
        
        # Initial random placement
        initial_coords = np.random.rand(n_facilities * 2) * 100
        
        # Optimize
        result = minimize(objective, initial_coords, method='SLSQP')
        
        return result.x.reshape(n_facilities, 2), result.fun
    
    # Use state user counts as demands
    optimal_locations, min_cost = optimize_testing_centers(state_needs['user_count'])
    
    print(f"Optimal testing center locations (simplified coordinates):")
    for i, loc in enumerate(optimal_locations):
        print(f"  Center {i+1}: ({loc[0]:.1f}, {loc[1]:.1f})")
    print(f"Minimum total weighted distance: {min_cost:.1f}")
    
    # Alert optimization
    print(f"\n--- Alert System Optimization ---")
    
    # Risk-based alert thresholds
    high_risk_users = analysis_data[analysis_data['risk_score'] > 0.6]
    medium_risk_users = analysis_data[(analysis_data['risk_score'] > 0.3) & (analysis_data['risk_score'] <= 0.6)]
    low_risk_users = analysis_data[analysis_data['risk_score'] <= 0.3]
    
    print(f"Alert Strategy Recommendations:")
    print(f"  High Risk Users ({len(high_risk_users)}): Immediate testing + daily monitoring")
    print(f"  Medium Risk Users ({len(medium_risk_users)}): Self-monitoring + testing if symptoms")
    print(f"  Low Risk Users ({len(low_risk_users)}): General precautions + periodic testing")
    
    # Contact tracing optimization
    print(f"\n--- Contact Tracing Optimization ---")
    
    # Identify users who should be prioritized for contact tracing
    contact_priority = analysis_data.copy()
    contact_priority['tracing_priority'] = (
        contact_priority['total_contacts'] / contact_priority['total_contacts'].max() * 0.5 +
        contact_priority['has_positive_test'] * 0.3 +
        contact_priority['symptoms_reported'] * 0.2
    )
    
    top_priority_users = contact_priority.nlargest(20, 'tracing_priority')[
        ['user_id', 'total_contacts', 'risk_score', 'tracing_priority']
    ]
    
    print("Top 20 Users for Priority Contact Tracing:")
    print(top_priority_users.head(10))
    
    # Policy recommendations
    print(f"\n--- Policy Recommendations ---")
    
    urban_risk = analysis_data[analysis_data['urban_rural'] == 'urban']['risk_score'].mean()
    rural_risk = analysis_data[analysis_data['urban_rural'] == 'rural']['risk_score'].mean()
    
    print(f"1. Focus on {'urban' if urban_risk > rural_risk else 'rural'} areas (higher average risk)")
    print(f"2. Target age group: {analysis_data.groupby('age_group')['risk_score'].mean().idxmax()}")
    print(f"3. High-risk contact locations: {contact_data.groupby('location_type')['duration_minutes'].mean().idxmax()}")
    
    # Vaccination strategy
    vaccination_priority = analysis_data.nlargest(1000, 'risk_score')[['user_id', 'age', 'risk_score']]
    print(f"\n4. Vaccination Priority: Target top 1000 high-risk users")
    print(f"   Average age of priority group: {vaccination_priority['age'].mean():.1f}")
    
    # ROI calculation
    print(f"\n--- Return on Investment Analysis ---")
    
    total_users = len(analysis_data)
    high_risk_count = len(high_risk_users)
    
    # Simplified cost-benefit analysis
    cost_per_test = 500  # INR
    cost_per_alert = 1    # INR
    cost_saved_per_prevented_case = 50000  # INR
    
    testing_cost = high_risk_count * cost_per_test
    alert_cost = total_users * cost_per_alert
    total_intervention_cost = testing_cost + alert_cost
    
    # Assume 20% reduction in transmission with interventions
    prevented_cases = int(analysis_data['has_positive_test'].sum() * 0.2)
    cost_savings = prevented_cases * cost_saved_per_prevented_case
    
    roi = (cost_savings - total_intervention_cost) / total_intervention_cost * 100
    
    print(f"Intervention Cost: ₹{total_intervention_cost:,}")
    print(f"Estimated Cost Savings: ₹{cost_savings:,}")
    print(f"Estimated ROI: {roi:.1f}%")
    
    return state_needs, optimal_locations

# =============================================================================
# MAIN EXECUTION
# =============================================================================

def main():
    """Execute all four types of analytics"""
    
    print("AAROGYA SETU BIG DATA ANALYTICS DEMONSTRATION")
    print("=" * 80)
    
    # 1. Descriptive Analytics
    contact_daily, state_stats = descriptive_analytics()
    
    # 2. Diagnostic Analytics
    analysis_data = diagnostic_analytics()
    
    # 3. Predictive Analytics
    enhanced_data, feature_importance = predictive_analytics(analysis_data)
    
    # 4. Prescriptive Analytics
    state_needs, optimal_locations = prescriptive_analytics(enhanced_data)
    
    print("\n" + "="*80)
    print("ANALYTICS DEMONSTRATION COMPLETED")
    print("="*80)
    print("\nSUMMARY:")
    print(f"• Processed {len(user_data):,} users and {len(contact_data):,} contact events")
    print(f"• Identified {len(enhanced_data[enhanced_data['risk_category'] == 'High'])} high-risk users")
    print(f"• Generated predictive models with feature importance analysis")
    print(f"• Provided optimization recommendations for resource allocation")
    print(f"• Calculated ROI for intervention strategies")

if __name__ == "__main__":
    main()