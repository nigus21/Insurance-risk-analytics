Predictive Modeling & Risk-Based Pricing

**Insurance Risk Analytics Project for AlphaCare Insurance Solutions**

---

## 🧠 Overview

Here the focus is on building **predictive machine learning models** that form the foundation of a **dynamic, risk-based insurance pricing system**.

Using historical policy and claims data, we model:

* **Claim severity** (financial risk)
* **Claim occurrence probability** (risk likelihood)
* **Risk-based premium estimation**

The workflow follows **industry best practices** used in regulated domains such as **insurance and finance**, emphasizing:

* Reproducibility
* Auditability
* Model interpretability
* Business-driven evaluation

---

## 🎯 Business Objective

The primary business objective is to move away from static, rule-based premiums toward a **data-driven, risk-adjusted pricing framework** that:

* Accurately estimates **expected claim costs**
* Differentiates **high-risk vs low-risk policies**
* Supports **fair, explainable premium decisions**
* Improves **loss ratio and profitability**

---

## 📦 Data Description

### Source

* **Raw data:** `MachineLearningRating_v3.txt`
* **Processed data:** `data/processed/clean_data.csv`

### Key Variables

* **Target Variables**

  * `TotalClaims` → Claim severity (regression target)
  * `CalculatedPremiumPerTerm` → Reference premium
* **Policy & Vehicle Features**

  * Vehicle age, value, engine size, coverage type, etc.
* **Customer Features**

  * Gender, marital status, province, postal code
* **Financial Metrics**

  * TotalPremium, TotalClaims, LossRatio

---

## 🏗️ Project Structure

```text
week3-insurance-risk-analytics/
│
├── data/
│   ├── raw/
│   │   └── MachineLearningRating_v3.txt
│   └── processed/
│       └── clean_data.csv
│
├── src/
│   └── task4_modeling.py
│
├── models/
│   ├── LinearRegression.pkl
│   ├── RandomForest.pkl
│   └── XGBoost.pkl
│
├── .venv/
├── README.md
└── requirements.txt
```

---

## 🔍 Modeling Goals

### 1️⃣ Claim Severity Prediction (Regression)

**Goal:**
Estimate the **expected claim amount**, conditional on a claim occurring.

* **Target:** `TotalClaims` (where `TotalClaims > 0`)
* **Metrics:**

  * Root Mean Squared Error (RMSE)
  * R² (Coefficient of Determination)

### 2️⃣ Risk-Based Premium Framework

A conceptual pricing formula:

```
Risk-Based Premium =
(Predicted Probability of Claim × Predicted Claim Severity)
+ Expense Loading
+ Profit Margin
```

This approach aligns with **actuarial pricing theory** and modern **ML-driven underwriting**.

---

## 🧪 Data Preparation

### ✔ Handling Missing Data

* Numeric features: median imputation
* Invalid entries coerced using `errors='coerce'`

### ✔ Feature Engineering

* Removal of non-informative identifiers
* Derived financial indicators (loss behavior)
* Filtering to claim-positive policies for severity modeling

### ✔ Encoding

* One-Hot Encoding for categorical variables
* `drop_first=True` to avoid multicollinearity

### ✔ Train-Test Split

* 80% Training
* 20% Testing
* Fixed random seed for reproducibility

---

## 🤖 Models Implemented

### 🔹 Linear Regression

* Baseline statistical model
* High interpretability
* Used for benchmarking

### 🔹 Random Forest Regressor

* Captures non-linear relationships
* Robust to noise and feature interactions

### 🔹 XGBoost Regressor (Best Performer)

* Gradient boosting framework
* Handles complex interactions efficiently
* Strong predictive accuracy on claim severity

---

## 📈 Model Evaluation

Each model is evaluated using:

| Metric | Description                       |
| ------ | --------------------------------- |
| RMSE   | Penalizes large prediction errors |
| R²     | Measures explanatory power        |

Results are printed during execution and used to select the **best-performing model**.

---

## 🔍 Model Interpretability (SHAP)

To ensure transparency and regulatory compliance:

* **SHAP (SHapley Additive exPlanations)** is used
* Identifies **top 5–10 most influential features**
* Explains both **direction** and **magnitude** of impact

### Example Insight:

> SHAP analysis shows that vehicle value and vehicle age are the strongest drivers of claim severity. Older and higher-value vehicles significantly increase expected claim amounts, supporting age- and value-based premium adjustments.

---

## 💰 Risk-Based Premium Logic

An **optional classification model** is used to:

* Predict the **probability of a claim**
* Combine it with predicted severity

This creates a **forward-looking premium** that:

* Reflects individual risk
* Supports fair and defensible pricing
* Improves underwriting decisions

---

## 💾 Model Persistence

All trained models are saved to disk using `joblib`:

```text
models/
├── LinearRegression.pkl
├── RandomForest.pkl
└── XGBoost.pkl
```

This enables:

* Reuse without retraining
* Auditable model artifacts
* Deployment readiness

---

## ⚙️ How to Run

Activate environment:

```bash
.venv\Scripts\activate
```

Run Task 4:

```bash
python src/task4_modeling.py
```

---

## 🧾 Key Outcomes

* Built multiple predictive models for claim severity
* Selected best model using objective metrics
* Applied explainability techniques (SHAP)
* Designed a conceptual risk-based pricing framework
* Followed industry-grade ML workflow standards

---

## 🏁 Conclusion

Week 04 delivers the **core intelligence** behind modern insurance pricing.
By combining **predictive accuracy**, **interpretability**, and **business logic**, the project demonstrates how machine learning can be responsibly applied in **regulated financial environments**.

---

## 👤 Author

**Nigus Dibekulu**
Insurance Risk Analytics & Machine Learning
