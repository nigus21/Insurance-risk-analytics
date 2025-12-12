#  This file prepares the data for hypothesis testing.

import pandas as pd

# Load the processed dataset (from task 1)
df = pd.read_csv("data/processed/clean_data.csv")

# --- KPI 1: Claim Frequency ---
df["has_claim"] = df["TotalClaims"] > 0

# --- KPI 2: Claim Severity ---
df["claim_severity"] = df["TotalClaims"].where(df["TotalClaims"] > 0)

# --- KPI 3: Margin ---
df["margin"] = df["TotalPremium"] - df["TotalClaims"]

# Export for Task 3 tests
df.to_csv("data/processed/task3_data.csv", index=False)

print("Task 3 KPIs created successfully!")
