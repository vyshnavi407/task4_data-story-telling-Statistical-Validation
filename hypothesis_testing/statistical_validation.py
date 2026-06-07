## Statistical Validation

### Hypothesis Testing

**Null Hypothesis (H₀):**
Discount has no significant relationship with Profit.

**Alternative Hypothesis (H₁):**
Discount has a significant relationship with Profit.

A Pearson Correlation Test is performed to determine whether discounts significantly affect profit.

  
# Hypothesis Testing: Discount vs Profit

from scipy.stats import pearsonr

# Calculate correlation and p-value
correlation, p_value = pearsonr(df["Discount"], df["Profit"])

print("Pearson Correlation Coefficient:", round(correlation, 4))
print("P-value:", p_value)

# Decision
alpha = 0.05

if p_value < alpha:
    print("\nResult: Reject the Null Hypothesis (H₀)")
    print("Conclusion: There is a statistically significant relationship between Discount and Profit.")
else:
    print("\nResult: Fail to Reject the Null Hypothesis (H₀)")
    print("Conclusion: There is no statistically significant relationship between Discount and Profit.")

### Interpretation

The p-value obtained from the Pearson Correlation Test is compared against a significance level of 0.05.

- If p-value < 0.05, the null hypothesis is rejected.
- If p-value ≥ 0.05, the null hypothesis is not rejected.

This helps determine whether discount strategies have a statistically significant impact on profitability.

