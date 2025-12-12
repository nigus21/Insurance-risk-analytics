# Task 3 – A/B Hypothesis Testing & Risk Analysis

## Overview
This analysis evaluates the key risk drivers in AlphaCare Insurance's portfolio.  
We quantified "risk" using two metrics:
- **Claim Frequency:** Proportion of policies with at least one claim
- **Claim Severity:** Average claim amount given a claim occurred

Additionally, **Margin** was defined as:


We tested the following **Null Hypotheses (H₀):**

1. No risk differences across provinces  
2. No risk differences between ZIP codes  
3. No significant margin (profit) difference between ZIP codes  
4. No significant risk difference between Women and Men  

Significance threshold: **α = 0.05**

---

## 1️⃣ Province Risk Differences
- **Test Used:** Chi-Square  
- **p-value:** 5.93 × 10⁻¹⁹  
- **Decision:** Reject H₀  

**Interpretation:**  
There is a statistically significant difference in claim risk across provinces. Some provinces have higher claim frequencies.  

**Business Recommendation:**  
Adjust premiums based on province risk. Higher-risk provinces may require higher premiums to maintain profitability.

---

## 2️⃣ ZIP Code Risk Differences
- **ZIP Codes Compared:** 2000 vs 122  
- **Test Used:** Chi-Square  
- **p-value:** 0.058  
- **Decision:** Fail to Reject H₀  

**Interpretation:**  
No statistically significant difference in claim frequency between the two ZIP codes tested.  

**Business Recommendation:**  
No ZIP-based pricing adjustments are required for these two ZIP codes. Additional ZIP codes can be analyzed to refine segmentation.

---

## 3️⃣ ZIP Code Margin Differences
- **ZIP Codes Compared:** 2000 vs 122  
- **Test Used:** t-test  
- **p-value:** 0.244  
- **Decision:** Fail to Reject H₀  

**Interpretation:**  
Margins (TotalPremium − TotalClaims) are similar between these ZIP codes.  

**Business Recommendation:**  
Profitability is consistent between the two ZIP codes; no pricing adjustment is needed.

---

## 4️⃣ Gender Risk Differences
- **Test Used:** Chi-Square  
- **p-value:** 0.951  
- **Decision:** Fail to Reject H₀  

**Interpretation:**  
There is no significant difference in claim risk between male and female policyholders.  

**Business Recommendation:**  
Gender-based pricing is not justified based on claim frequency.

---

## ✅ Summary Table

| Test | p-value | Decision | Business Insight |
|------|---------|---------|----------------|
| Province vs Claim Risk | 5.93e-19 | Reject H₀ | Adjust premiums per province |
| ZIP vs Claim Risk | 0.058 | Fail to Reject H₀ | No ZIP-based risk adjustment |
| ZIP vs Margin | 0.244 | Fail to Reject H₀ | Margins similar; no pricing change |
| Gender vs Claim Risk | 0.951 | Fail to Reject H₀ | Gender-based pricing not needed |

---

## Conclusion
This analysis identifies **provinces as a key driver of risk**. ZIP codes and gender do not show significant differences in risk or profitability in this dataset.  
Premium strategies should therefore focus on **geographic segmentation**, while other demographic adjustments are not supported by the data.  
Future analyses could explore additional features such as vehicle type, age, and coverage type for finer-grained pricing optimization.
