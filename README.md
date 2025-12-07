# End-to-End Insurance Risk Analytics & Predictive Modeling

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![DVC](https://img.shields.io/badge/Data%20Version%20Control-DVC-9cf)](https://dvc.org/)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)

**Repository:** [https://github.com/Mulat-K/insurance_analytics](https://github.com/Mulat-K/insurance_analytics)

---

## 📌 Project Overview
**AlphaCare Insurance Solutions (ACIS)** is optimizing its marketing strategy and risk assessment for car insurance in South Africa. As a Marketing Analytics Engineer, this project involves analyzing historical claim data to identify "low-risk" segments for premium reduction and building predictive models to estimate claim severity.

The project demonstrates an end-to-end data pipeline including **Exploratory Data Analysis (EDA)**, **Statistical A/B Testing**, **Data Version Control (DVC)**, and **Machine Learning**.

---

## 🚀 Business Objective
The primary goals are:

1. **Risk Analysis**: Understand risk differences across provinces, zip codes, gender, and vehicle types.  
2. **Profitability**: Identify segments with high margins and low loss ratios.  
3. **Predictive Modeling**: Build models to predict `TotalClaims` (severity) and optimize premiums using Linear Regression, XGBoost, and Random Forests.

---

## 📂 Project Structure

```text
insurance_analytics/
├── .dvc/                  # DVC configuration files
├── .github/workflows/     # CI/CD pipelines (GitHub Actions)
├── data/                  # Data directory (tracked by DVC)
│   └── insurance_claims.csv.dvc
├── notebooks/             # Jupyter Notebooks for analysis
│   ├── 01_eda.ipynb               # Exploratory Data Analysis
│   ├── 02_hypothesis_testing.ipynb # Statistical A/B Testing
│   └── 03_predictive_modeling.ipynb # ML & SHAP Analysis
├── src/                   # Source code for modular processing
│   ├── data_loader.py
│   ├── eda_utils.py
│   └── modeling.py
├── scripts/               # Utility scripts
├── requirements.txt       # Python dependencies
├── README.md              # Project documentation
└── .gitignore
```

## 🛠 Tech Stack

- **Language:** Python 3.x  
- **Data Manipulation:** Pandas, NumPy  
- **Visualization:** Matplotlib, Seaborn  
- **Machine Learning:** Scikit-Learn, XGBoost  
- **Explainability:** SHAP (SHapley Additive exPlanations)  
- **Version Control:** Git, DVC (Data Version Control)  
- **Statistical Analysis:** Scipy (Stats)  

---

## 📝 Key Features & Implementation

### Task 1: Exploratory Data Analysis (EDA)
- Deep-dive analysis of insurance dataset (Feb 2014 - Aug 2015).  
- Handled missing values in `TotalClaims`, `TotalPremium`, and `Gender`.  
- Created KPIs: Loss Ratio (`Claims/Premium`) and Margin.  
- Visualized distributions of premiums and claims, risk heatmaps by Province and Vehicle Type.  

### Task 2: Data Version Control (DVC)
- Implemented DVC to ensure reproducibility and auditability of data.  
- Raw data tracked via `.dvc` files.  
- Remote storage simulation enabled for team collaboration.  

### Task 3: A/B Hypothesis Testing
- Validated business assumptions using statistical tests (Chi-Squared, T-Tests, ANOVA).  
- **Provinces:** Tested for risk differences across provinces.  
- **Zip Codes:** Analyzed margin differences between regions.  
- **Gender:** Investigated if Gender has a statistically significant impact on risk.  

### Task 4: Predictive Modeling
- Built and evaluated models to predict Claim Severity (`TotalClaims` for incidents > 0).  
- **Models:** Linear Regression (per ZipCode), Random Forest, XGBoost.  
- **Evaluation Metrics:** RMSE, MAE, R-Squared.  
- **Interpretability:** Used SHAP plots to identify top drivers of risk (e.g., Vehicle Age, SumInsured).  

---

## ⚙️ Installation & Setup

### Clone the Repository
```bash
git clone https://github.com/Mulat-K/insurance_analytics.git
cd insurance_analytics

