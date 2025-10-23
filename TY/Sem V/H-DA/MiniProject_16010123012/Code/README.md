# 🌤️ Humidity Prediction for Ghatkopar - Time Series Analysis

A comprehensive data analysis project focused on predicting humidity levels for Ghatkopar, Mumbai using time series forecasting models (ARIMA and SARIMA).

---

## 📋 Project Overview

This project analyzes and forecasts humidity patterns using historical weather data from 2023-2025. It implements both ARIMA and SARIMA models to capture trend and seasonal patterns in humidity data.

**Location:** Ghatkopar, Mumbai (19.0860°N, 72.9090°E)  
**Data Source:** Open-Meteo Historical Weather API  
**Time Period:** 2023-2025  
**Models Used:** ARIMA, SARIMA

---

## 🗂️ Project Structure

```
Code/
├── 1)dataset.py                          # Data collection from API
├── 2)data_processing.py                  # Data cleaning & preprocessing
├── 3)EDA.py                              # Exploratory Data Analysis
├── 4)forecasting_with_arima.py           # ARIMA model building
├── 5)model_evaluation.py                 # ARIMA evaluation
├── 6)forecasting_with_sarima.py          # SARIMA model building
├── 7)model_evaluation_sarima.py          # Model comparison
├── requirements.txt                      # Python dependencies
└── README.md                             # This file

Data Files:
├── ghatkopar_humidity_2023_2024.csv     # Raw data
├── cleaned_humidity.csv                  # Processed data
├── forecast_results.csv                  # ARIMA predictions
└── forecast_results_sarima.csv           # SARIMA predictions
```

---

## 🚀 Quick Start

### 1. Install Dependencies

```powershell
pip install -r requirements.txt
```

### 2. Run the Complete Pipeline

Execute scripts in order:

```powershell
# Step 1: Collect data
python "1)dataset.py"

# Step 2: Clean and preprocess
python "2)data_processing.py"

# Step 3: Exploratory analysis
python "3)EDA.py"

# Step 4: Build ARIMA model
python "4)forecasting_with_arima.py"

# Step 5: Evaluate ARIMA
python "5)model_evaluation.py"

# Step 6: Build SARIMA model
python "6)forecasting_with_sarima.py"

# Step 7: Compare models
python "7)model_evaluation_sarima.py"
```

---

## 📊 Methodology

### **Phase 1: Data Collection** (`1)dataset.py`)
- Fetches daily mean humidity data from Open-Meteo API
- Covers multiple years (2023-2025)
- Handles API errors and missing data gracefully
- Outputs: `ghatkopar_humidity_2023_2024.csv`

**Key Features:**
- Configurable location coordinates
- Proper timezone handling (Asia/Kolkata)
- Error logging and validation

---

### **Phase 2: Data Preprocessing** (`2)data_processing.py`)
- Converts dates to datetime format
- Handles missing values using forward/backward fill
- Detects and reports outliers (Z-score method)
- Validates data quality (range checks, duplicates)
- Outputs: `cleaned_humidity.csv`, `data_quality_report.png`

**Quality Checks:**
- ✅ Outlier detection (±3 std deviations)
- ✅ Humidity range validation (0-100%)
- ✅ Duplicate date removal
- ✅ Missing value imputation

---

### **Phase 3: Exploratory Data Analysis** (`3)EDA.py`)
Comprehensive analysis including:

**Stationarity Testing:**
- Augmented Dickey-Fuller (ADF) test
- Determines need for differencing

**Visualizations:**
- Daily humidity trends with moving averages
- Monthly aggregation patterns
- Seasonal decomposition (Trend + Seasonal + Residual)
- ACF/PACF plots for parameter selection
- Year-over-year comparison

**Outputs:**
- `humidity_trend.png`
- `monthly_humidity.png`
- `acf_pacf_plots.png`
- `seasonal_decomposition.png`
- `yearly_comparison.png`

---

### **Phase 4: ARIMA Modeling** (`4)forecasting_with_arima.py`)

**Model Selection:**
- Grid search over parameters (p, d, q)
- AIC-based optimization
- 80-20 train-test split

**Diagnostics:**
- Residual analysis (white noise test)
- Ljung-Box test for autocorrelation
- Shapiro-Wilk normality test
- Q-Q plots

**Outputs:**
- `forecast_results.csv` (predictions + confidence intervals)
- `arima_residual_analysis.png`
- `arima_forecast_with_ci.png`
- `arima_parameter_search_results.csv`

---

### **Phase 5: ARIMA Evaluation** (`5)model_evaluation.py`)

**Metrics Calculated:**
- **MAE** (Mean Absolute Error) - Average prediction error
- **RMSE** (Root Mean Squared Error) - Penalizes large errors
- **MAPE** (Mean Absolute Percentage Error) - Error as percentage
- **R²** (Coefficient of Determination) - Variance explained
- **NRMSE** (Normalized RMSE) - Scale-independent metric

**Outputs:**
- `arima_evaluation_plots.png`
- `arima_evaluation_metrics.csv`

---

### **Phase 6: SARIMA Modeling** (`6)forecasting_with_sarima.py`)

**Seasonal Components:**
- Seasonal period: 12 months
- Grid search: (p,d,q) × (P,D,Q,12)
- Captures monthly humidity patterns

**Advantages:**
- Handles seasonality explicitly
- Better for weather data with annual cycles

**Outputs:**
- `forecast_results_sarima.csv`
- `sarima_residual_analysis.png`
- `sarima_forecast_with_ci.png`
- `sarima_parameter_search_results.csv`

---

### **Phase 7: Model Comparison** (`7)model_evaluation_sarima.py`)

**Comprehensive Comparison:**
- Side-by-side metrics for ARIMA vs SARIMA
- Visual comparison of predictions
- Error distribution analysis
- Statistical recommendation

**Outputs:**
- `model_comparison_comprehensive.png`
- `model_comparison_metrics.csv`
- Console report with winner declaration

---

## 📈 Key Improvements Implemented

### ✅ **Statistical Rigor**
1. **Stationarity Testing** - ADF test to validate modeling assumptions
2. **Residual Diagnostics** - Ensures model captures all patterns
3. **Multiple Metrics** - Comprehensive error evaluation (MAE, RMSE, MAPE, R²)
4. **Confidence Intervals** - Uncertainty quantification in forecasts

### ✅ **Code Quality**
1. **Modular Functions** - Reusable, well-documented code
2. **Error Handling** - Graceful failures with informative messages
3. **Logging** - Professional logging instead of print statements
4. **Configuration** - Centralized settings for easy modification

### ✅ **Visualizations**
1. **High-DPI Plots** - Publication-quality figures (300 DPI)
2. **Comprehensive Analysis** - Multiple perspectives on same data
3. **Confidence Intervals** - Visual uncertainty representation
4. **Comparison Plots** - Easy model performance comparison

### ✅ **Best Practices**
1. **Grid Search** - Systematic parameter optimization
2. **Train-Test Split** - Proper validation methodology
3. **Residual Analysis** - Diagnostic checks for model adequacy
4. **Documentation** - Clear docstrings and comments

---

## 📊 Expected Results

### **Typical Performance:**
- **MAPE**: 3-8% (Excellent to Good)
- **R² Score**: 0.6-0.85 (Moderate to Strong)
- **RMSE**: 3-6% humidity points

### **Model Selection:**
- **SARIMA** typically performs better for seasonal data
- **ARIMA** is simpler and faster for non-seasonal patterns

---

## 🛠️ Troubleshooting

### Issue: "File not found" error
**Solution:** Run scripts in numerical order (1 → 2 → 3 → ...)

### Issue: Import errors for statsmodels/sklearn
**Solution:** 
```powershell
pip install --upgrade statsmodels scikit-learn
```

### Issue: API timeout or rate limiting
**Solution:** Increase timeout in `1)dataset.py` or add delays between requests

### Issue: Poor model performance
**Solution:** 
- Check data quality in EDA
- Expand grid search parameter ranges
- Consider data transformation (log, Box-Cox)

---

## 📚 Additional Enhancements (Future Work)

1. **Advanced Models:**
   - Prophet (Facebook's forecasting tool)
   - LSTM neural networks
   - XGBoost with lag features

2. **Cross-Validation:**
   - TimeSeriesSplit for robust evaluation
   - Walk-forward validation

3. **Feature Engineering:**
   - External variables (temperature, pressure)
   - Calendar features (holidays, weekends)
   - Lag features

4. **Automation:**
   - Pipeline orchestration script
   - Automated model retraining
   - Real-time predictions

---

## 🎓 Learning Outcomes

This project demonstrates proficiency in:
- ✅ Time series analysis and forecasting
- ✅ Statistical modeling (ARIMA/SARIMA)
- ✅ Data preprocessing and quality control
- ✅ Model evaluation and comparison
- ✅ Python programming best practices
- ✅ Data visualization and communication

---

## 📝 References

- **Open-Meteo API:** https://open-meteo.com/
- **Statsmodels Documentation:** https://www.statsmodels.org/
- **Time Series Analysis:** Box, G. E. P., Jenkins, G. M., & Reinsel, G. C. (2015)

---

## 👨‍💻 Author

**Project Type:** Mini-Project for Higher Diploma in Data Analytics  
**Institution:** KJSCE (K.J. Somaiya College of Engineering)  
**Course:** TY BTech, Semester V  
**Subject:** H-DA (Higher Diploma - Data Analytics)

---

## 📄 License

This project is for educational purposes.

---

**Last Updated:** October 2025
