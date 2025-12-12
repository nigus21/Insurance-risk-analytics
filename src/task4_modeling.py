# task4_modeling.py

"""
Task 4: Predictive Modeling & Risk-Based Premium
- Claim Severity Prediction (Regression)
- Risk-Based Premium (Optional Classification)
- Model Evaluation (RMSE, R2)
- Feature Importance (SHAP)
"""

import os
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier
import xgboost as xgb
from sklearn.metrics import mean_squared_error, r2_score
import shap
import joblib

# -----------------------------
# 1. Load and Prepare Data
# -----------------------------
def load_and_prepare_data(file_path):
    df = pd.read_csv(file_path, low_memory=False)

    # Keep only policies with claims
    df_claims = df[df["TotalClaims"] > 0].copy()

    # List numeric columns that likely exist
    numeric_cols = ['Cylinders', 'cubiccapacity', 'Kilowatts', 'NumberOfDoors', 
                    'CustomValueEstimate', 'CapitalOutstanding', 'NumberOfVehiclesInFleet', 
                    'SumInsured', 'CalculatedPremiumPerTerm', 'TotalPremium', 'TotalClaims']

    # Convert numeric columns and fill missing values
    for col in numeric_cols:
        if col in df_claims.columns:
            df_claims[col] = pd.to_numeric(df_claims[col], errors='coerce')
            df_claims[col] = df_claims[col].fillna(df_claims[col].median())

    # Encode categorical columns
    categorical_cols = df_claims.select_dtypes(include=['object']).columns
    df_claims = pd.get_dummies(df_claims, columns=categorical_cols, drop_first=True)

    # Train-test split
    X = df_claims.drop(columns=["TotalClaims", "CalculatedPremiumPerTerm"], errors='ignore')
    y = df_claims["TotalClaims"]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    return X_train, X_test, y_train, y_test

# -----------------------------
# 2. Build Models
# -----------------------------
def build_models(X_train, y_train):
    models = {}

    # Linear Regression
    lr = LinearRegression()
    lr.fit(X_train, y_train)
    models['LinearRegression'] = lr

    # Random Forest Regressor
    rf = RandomForestRegressor(n_estimators=100, random_state=42)
    rf.fit(X_train, y_train)
    models['RandomForest'] = rf

    # XGBoost Regressor
    xgb_model = xgb.XGBRegressor(objective='reg:squarederror', n_estimators=100, random_state=42)
    xgb_model.fit(X_train, y_train)
    models['XGBoost'] = xgb_model

    return models

# -----------------------------
# 3. Evaluate Models
# -----------------------------
def evaluate_models(models, X_test, y_test):
    for name, model in models.items():
        y_pred = model.predict(X_test)
        rmse = np.sqrt(mean_squared_error(y_test, y_pred))
        r2 = r2_score(y_test, y_pred)
        print(f"{name} - RMSE: {rmse:.2f}, R2: {r2:.2f}")

# -----------------------------
# 4. SHAP Feature Importance
# -----------------------------
def explain_model(model, X_test):
    explainer = shap.Explainer(model)
    shap_values = explainer(X_test)
    shap.summary_plot(shap_values, X_test, max_display=10)

# -----------------------------
# 5. Optional: Risk-Based Premium
# -----------------------------
def risk_based_premium(df, xgb_model):
    df['HasClaim'] = (df['TotalClaims'] > 0).astype(int)
    X_class = pd.get_dummies(df.drop(columns=['TotalClaims', 'CalculatedPremiumPerTerm'], errors='ignore'), drop_first=True)
    y_class = df['HasClaim']

    X_train_c, X_test_c, y_train_c, y_test_c = train_test_split(X_class, y_class, test_size=0.2, random_state=42)
    clf = RandomForestClassifier(n_estimators=100, random_state=42)
    clf.fit(X_train_c, y_train_c)

    # Predicted claim probability
    prob_claim = clf.predict_proba(X_test_c)[:,1]

    # Predicted claim severity using XGBoost model
    # Align columns if needed
    common_cols = X_test_c.columns.intersection(xgb_model.get_booster().feature_names)
    pred_claim_severity = xgb_model.predict(X_test_c[common_cols])

    # Example premium = probability * severity + expense/profit
    predicted_premium = prob_claim * pred_claim_severity + 50
    return predicted_premium

# -----------------------------
# 6. Save Models
# -----------------------------
def save_models(models):
    os.makedirs("models", exist_ok=True)
    for name, model in models.items():
        joblib.dump(model, f"models/{name}.pkl")
    print("Models saved in 'models/' directory.")

# -----------------------------
# Main Execution
# -----------------------------
if __name__ == "__main__":
    X_train, X_test, y_train, y_test = load_and_prepare_data("data/processed/clean_data.csv")
    models = build_models(X_train, y_train)
    evaluate_models(models, X_test, y_test)
    explain_model(models['XGBoost'], X_test)

    # Optional: calculate risk-based premium
    df = pd.read_csv("data/processed/clean_data.csv", low_memory=False)
    premium_predictions = risk_based_premium(df, models['XGBoost'])
    print("Sample risk-based premiums:", premium_predictions[:5])

    # Save models
    save_models(models)
