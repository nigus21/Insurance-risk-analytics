import pandas as pd
from scipy import stats

df = pd.read_csv("data/processed/task3_data.csv")

results = {}

# ---------------------------------------------------------
# 1. PROVINCE RISK DIFFERENCE (Claim Frequency)
# ---------------------------------------------------------
province_table = pd.crosstab(df["Province"], df["has_claim"])
chi2, p1, dof, expected = stats.chi2_contingency(province_table)

results["province_risk"] = {
    "test": "Chi-Square",
    "p_value": p1,
    "decision": "Reject H0" if p1 < 0.05 else "Fail to Reject H0"
}

# ---------------------------------------------------------
# 2. ZIP CODE RISK DIFFERENCE (Claim Frequency)
# ---------------------------------------------------------

# Use top 2 most common zip codes
top_zips = df["PostalCode"].value_counts().index[:2]

zip_df = df[df["PostalCode"].isin(top_zips)]
zip_table = pd.crosstab(zip_df["PostalCode"], zip_df["has_claim"])
chi2, p2, dof, expected = stats.chi2_contingency(zip_table)

results["zipcode_risk"] = {
    "test": "Chi-Square",
    "zip_codes_tested": list(top_zips),
    "p_value": p2,
    "decision": "Reject H0" if p2 < 0.05 else "Fail to Reject H0"
}

# ---------------------------------------------------------
# 3. ZIP CODE MARGIN DIFFERENCE (Numerical t-test)
# ---------------------------------------------------------

zip1_margin = df[df["PostalCode"] == top_zips[0]]["margin"]
zip2_margin = df[df["PostalCode"] == top_zips[1]]["margin"]

t_stat, p3 = stats.ttest_ind(zip1_margin, zip2_margin, equal_var=False)

results["zipcode_margin"] = {
    "test": "t-test",
    "zip_codes_tested": list(top_zips),
    "p_value": p3,
    "decision": "Reject H0" if p3 < 0.05 else "Fail to Reject H0"
}

# ---------------------------------------------------------
# 4. GENDER RISK DIFFERENCE (Claim Frequency)
# ---------------------------------------------------------

gender_df = df[df["Gender"].isin(["Male", "Female"])]
gender_table = pd.crosstab(gender_df["Gender"], gender_df["has_claim"])
chi2, p4, dof, expected = stats.chi2_contingency(gender_table)

results["gender_risk"] = {
    "test": "Chi-Square",
    "p_value": p4,
    "decision": "Reject H0" if p4 < 0.05 else "Fail to Reject H0"
}

# ---------------------------------------------------------
# SAVE RESULTS
# ---------------------------------------------------------

import json
with open("reports/task3_results.json", "w") as f:
    json.dump(results, f, indent=4)

print("Task 3 tests completed!")
print(results)
