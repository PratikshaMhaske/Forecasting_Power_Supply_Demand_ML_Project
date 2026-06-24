# ⚡ Power Consumption Demand Forecasting using Prophet

## 📌 Project Overview

This project focuses on forecasting electricity power consumption using Time Series Forecasting techniques. Historical PJMW power consumption data was analyzed, preprocessed, and modeled using multiple forecasting approaches including ARIMA, SARIMA, Holt-Winters, and Prophet.

After comparing model performance, Prophet was selected as the final model due to its superior forecasting accuracy.

The trained Prophet model was deployed using Streamlit to provide an interactive forecasting application.

---

## 🎯 Objectives

- Analyze historical power consumption patterns.
- Perform time series preprocessing and exploratory data analysis.
- Build and compare multiple forecasting models.
- Select the best-performing model based on evaluation metrics.
- Forecast future electricity demand for the next 30 days.
- Deploy the forecasting model using Streamlit.

---

## 📊 Dataset Information

**Dataset:** PJMW Hourly Energy Consumption

**Target Variable:**
- `PJMW_MW` → Power consumption in Megawatts (MW)

**Features Engineered:**
- Year
- Month
- Day
- Hour
- DayOfWeek
- Quarter
- WeekOfYear
- IsWeekend

---

## 🔧 Data Preprocessing

The following preprocessing steps were performed:

- Handling missing values
- Duplicate record detection and removal
- Datetime indexing
- Feature engineering
- Time series sorting
- Stationarity testing using ADF Test

---

## 📈 Exploratory Data Analysis

Several visualizations were created to understand data patterns:

- Power Consumption Trend
- Monthly Consumption Analysis
- Daily Consumption Analysis
- Hourly Consumption Analysis
- Correlation Heatmap
- Boxplots for Outlier Detection
- ACF Plot
- PACF Plot

---

## 🧪 Stationarity Test

### Augmented Dickey-Fuller (ADF) Test

Results:

- ADF Statistic = -19.53
- p-value = 0.0000

Conclusion:

The time series is stationary since the p-value is less than 0.05.

---

## 🤖 Models Implemented

### 1. ARIMA

Model:
```
ARIMA(2,0,2)
```

Performance:

| Metric | Value |
|----------|----------|
| MAE | 808.14 |
| RMSE | 996.51 |

---

### 2. SARIMA

Model:
```
SARIMA(1,0,1)(1,0,1,24)
```

Performance:

| Metric | Value |
|----------|----------|
| MAE | 594.36 |
| RMSE | 810.25 |

---

### 3. Holt-Winters

Performance:

| Metric | Value |
|----------|----------|
| MAE | 502.92 |
| RMSE | 660.74 |

---

### 4. Prophet (Final Model)

Performance:

| Metric | Value |
|----------|----------|
| MAE | 444.76 |
| RMSE | 547.13 |

---

## 🏆 Model Comparison

| Model | MAE | RMSE |
|---------|---------:|---------:|
| ARIMA | 808.14 | 996.51 |
| SARIMA | 594.36 | 810.25 |
| Holt-Winters | 502.92 | 660.74 |
| **Prophet** | **444.76** | **547.13** |

### Best Model

✅ Prophet

Prophet achieved the lowest MAE and RMSE among all tested models and was selected as the final forecasting model.

---

## 🔮 Future Forecast

The final Prophet model was used to generate electricity demand forecasts for the next 30 days (720 hours).

Forecast outputs include:

- Predicted demand (`yhat`)
- Lower confidence interval (`yhat_lower`)
- Upper confidence interval (`yhat_upper`)

Author

Er. Pratiksha Mhaske

LinkedIn: https://www.linkedin.com/in/pratiksha-mhaske

GitHub: https://github.com/PratikshaMhaske
