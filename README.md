# End-to-End Insurance Risk Analytics & Predictive Modeling

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![DVC](https://img.shields.io/badge/Data%20Version%20Control-DVC-9cf)](https://dvc.org/)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)
![CI
Pipeline](https://github.com/Mulat-K/insurance_analytics/actions/workflows/ci_pipeline.yml/badge.svg)

**Repository:** https://github.com/Mulat-K/insurance_analytics

------------------------------------------------------------------------

## 🔍 Project Overview

**AlphaCare Insurance Solutions (ACIS)** is developing an advanced
insurance analytics system for car insurance customers across South
Africa.\
Your role: **Marketing Analytics Engineer** responsible for end-to-end
analysis of historical car insurance claim data.

This project includes:

-   Exploratory Data Analysis (EDA)
-   Statistical A/B Testing
-   Machine Learning Models (Linear Regression, Random Forest, XGBoost)
-   SHAP-based explainability
-   DVC-powered data versioning
-   CI/CD using GitHub Actions

------------------------------------------------------------------------

## 🚀 Business Objective

### The project aims to:

1.  **Analyze risk** across provinces, gender, vehicle type, and zip
    codes\
2.  **Identify profitable low-risk segments**\
3.  **Predict claim severity** (TotalClaims)\
4.  **Support premium optimization** with data-driven models

------------------------------------------------------------------------

## 🛠 Tech Stack

  Category          Tools
  ----------------- -----------------------
  Language          Python 3.x
  Data              Pandas, NumPy
  Visualizations    Matplotlib, Seaborn
  Modeling          Scikit-Learn, XGBoost
  Explainability    SHAP
  Statistics        Scipy
  Version Control   Git + DVC
  CI/CD             GitHub Actions
  Testing           Pytest
  Linting           Flake8

------------------------------------------------------------------------

## 📂 Project Structure

``` text
insurance_analytics/
├── .dvc/                       
├── .github/workflows/          
│   └── ci_pipeline.yml
├── data/
│   └── insurance_claims.csv.dvc
├── notebooks/
│   ├── 01_eda.ipynb
│   ├── 02_hypothesis_testing.ipynb
│   └── 03_predictive_modeling.ipynb
├── src/
│   ├── data_loader.py
│   ├── eda_utils.py
│   └── modeling.py
├── scripts/
├── tests/
│   └── test_sample.py
├── requirements.txt
├── README.md
└── .gitignore
```

------------------------------------------------------------------------

## 📊 Features & Implementation

### 1️⃣ Exploratory Data Analysis (EDA)

-   Missing value treatment\
-   Statistical summary of `TotalPremium`, `TotalClaims`\
-   Loss Ratio & Margin calculation\
-   Heatmaps, boxplots, histograms\
-   Risk analysis by: Province, Gender, Vehicle Type, Zip Code

------------------------------------------------------------------------

### 2️⃣ Hypothesis Testing (A/B Testing)

-   T‑Tests\
-   Chi‑Squared Tests\
-   ANOVA

Validates assumptions like:

-   Are some provinces riskier?
-   Does gender affect claim severity?

------------------------------------------------------------------------

### 3️⃣ Predictive Modeling

Models:

-   Linear Regression\
-   Random Forest\
-   XGBoost

Metrics:

-   RMSE\
-   MAE\
-   R² Score

Explainability: **SHAP**

------------------------------------------------------------------------

### 4️⃣ Data Version Control (DVC)

``` bash
dvc init
dvc add data/insurance_claims.csv
dvc remote add -d storage remote_path
dvc push
```

------------------------------------------------------------------------

## 🔄 CI/CD Pipeline (GitHub Actions)

-   Flake8 linting\
-   Pytest testing

Run locally:

``` bash
pytest tests/
```

------------------------------------------------------------------------

## ⚙️ Installation & Setup

``` bash
git clone https://github.com/Mulat-K/insurance_analytics.git
cd insurance_analytics
```

### Create virtual environment

``` bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate   # Windows
```

### Install dependencies

``` bash
pip install -r requirements.txt
```

### Pull data via DVC

``` bash
dvc pull
```

------------------------------------------------------------------------

## 🏁 Running the Project

Open notebooks:

``` bash
jupyter notebook notebooks/01_eda.ipynb
```

------------------------------------------------------------------------

## 🧪 Testing & Git Best Practices

-   Atomic commits\
-   Feature branches\
-   WIP commits for long tasks\
-   Run CI checks before pushing

------------------------------------------------------------------------

## 📜 License

MIT License

------------------------------------------------------------------------

## 📧 Contact

**Developer:** Mulatie Kindie\
Email: mulatiekinde@gmail.com
