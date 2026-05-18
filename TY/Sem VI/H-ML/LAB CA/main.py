import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.cluster import KMeans
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import StandardScaler

def main():
    # 1. Setup & Data Loading
    print("Loading dataset...")
    df = pd.read_csv("smart_city_traffic_stress_dataset.csv")
    df = df.dropna()

    # Create a folder to save plots for the report
    os.makedirs("plots_for_report", exist_ok=True)
    sns.set_theme(style="whitegrid")

    # ---------------------------------------------------------
    # PART 1: EXPLORATORY DATA ANALYSIS (EDA) for PATTERNS
    # ---------------------------------------------------------
    print("Generating Correlation Heatmap...")
    plt.figure(figsize=(10, 8))
    # Select only numeric columns for correlation matrix
    numeric_cols = df.select_dtypes(include=[np.number])
    corr = numeric_cols.corr()
    sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f")
    plt.title("Correlation Matrix of Traffic Variables")
    plt.tight_layout()
    plt.savefig("plots_for_report/1_Correlation_Matrix.png")
    plt.close()

    # ---------------------------------------------------------
    # PART 2: CLUSTERING CONGESTION PATTERNS (Unsupervised ML)
    # Problem Statement: "Identify and analyze... patterns"
    # ---------------------------------------------------------
    print("Performing K-Means Clustering on Congestion Variables...")
    # We focus on the core congestion indicators
    congestion_features = ['traffic_density', 'avg_speed', 'signal_wait_time']
    X_cluster = df[congestion_features]
    
    # Scale data for clustering
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X_cluster)
    
    # Apply K-Means (Grouping into 3 patterns: Free Flow, Moderate, Severe Congestion)
    kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
    df['Congestion_Cluster'] = kmeans.fit_predict(X_scaled)
    
    # Plot the clusters
    plt.figure(figsize=(8, 6))
    sns.scatterplot(x='traffic_density', y='avg_speed', hue='Congestion_Cluster', 
                    palette='viridis', data=df, alpha=0.6)
    plt.title("Traffic Congestion Patterns (Clusters)")
    plt.xlabel("Traffic Density")
    plt.ylabel("Average Speed")
    plt.tight_layout()
    plt.savefig("plots_for_report/2_Congestion_Clusters.png")
    plt.close()

    # ---------------------------------------------------------
    # PART 3: PREDICTING STRESS INDEX (Supervised ML)
    # ---------------------------------------------------------
    print("Training Random Forest to Predict Traffic Stress...")
    # Prepare data for regression
    df_reg = pd.get_dummies(df.drop('Congestion_Cluster', axis=1), drop_first=True)
    
    X = df_reg.drop("stress_index", axis=1)
    y = df_reg["stress_index"]
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    
    y_pred = model.predict(X_test)
    
    print("--- Model Performance ---")
    print("MSE:", mean_squared_error(y_test, y_pred))
    print("R2 Score:", r2_score(y_test, y_pred))
    
    # Actual vs Predicted Plot
    plt.figure(figsize=(8, 6))
    plt.scatter(y_test, y_pred, alpha=0.5, color='royalblue')
    plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--', lw=2)
    plt.xlabel("Actual Stress")
    plt.ylabel("Predicted Stress")
    plt.title("Random Forest: Actual vs Predicted Stress Index")
    plt.tight_layout()
    plt.savefig("plots_for_report/3_Actual_vs_Predicted.png")
    plt.close()

    # Feature Importance Plot
    plt.figure(figsize=(10, 6))
    feature_importances = pd.Series(model.feature_importances_, index=X.columns).sort_values(ascending=False)
    sns.barplot(x=feature_importances.values, y=feature_importances.index, hue=feature_importances.index, palette="mako", legend=False)
    plt.title("What causes the most Traffic Stress? (Feature Importance)")
    plt.xlabel("Importance Score")
    plt.tight_layout()
    plt.savefig("plots_for_report/4_Feature_Importance.png")
    plt.close()

    print("\nSUCCESS! All analysis is complete.")
    print("Go to the 'plots_for_report' folder to get all the graphs for your team's PPT and Report!")

if __name__ == "__main__":
    main()