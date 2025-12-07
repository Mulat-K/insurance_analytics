import pandas as pd
import scipy.stats as stats

def test_risk_across_provinces(df):
    """
    H0: There are no risk differences across provinces.
    Metric: TotalClaims (Numerical) -> ANOVA
    """
    print("\n--- Testing Risk Differences Across Provinces (ANOVA) ---")
    groups = [group['TotalClaims'].values for name, group in df.groupby('Province')]
    
    f_stat, p_value = stats.f_oneway(*groups)
    
    print(f"F-Statistic: {f_stat}, P-Value: {p_value}")
    if p_value < 0.05:
        print("Result: Reject Null Hypothesis. Significant risk differences exist between provinces.")
    else:
        print("Result: Fail to Reject Null Hypothesis.")

def test_margin_zipcodes(df):
    """
    H0: There is no significant margin difference between zip codes.
    Metric: Margin (TotalPremium - TotalClaims)
    Note: Testing all zipcodes via ANOVA is computationally heavy. 
    We filter for top 20 zipcodes by volume.
    """
    print("\n--- Testing Margin Differences Across Top ZipCodes ---")
    top_zips = df['PostalCode'].value_counts().head(20).index
    df_filtered = df[df['PostalCode'].isin(top_zips)]
    
    groups = [group['Margin'].values for name, group in df_filtered.groupby('PostalCode')]
    f_stat, p_value = stats.f_oneway(*groups)
    
    print(f"F-Statistic: {f_stat}, P-Value: {p_value}")
    if p_value < 0.05:
        print("Result: Reject Null Hypothesis. Margins differ significantly by ZipCode.")

def test_risk_gender(df):
    """
    H0: There is no significant risk difference between Women and Men.
    Metric: TotalClaims (T-Test)
    """
    print("\n--- Testing Risk Differences: Women vs Men ---")
    women = df[df['Gender'] == 'Female']['TotalClaims']
    men = df[df['Gender'] == 'Male']['TotalClaims']
    
    t_stat, p_value = stats.ttest_ind(women, men, equal_var=False)
    
    print(f"T-Statistic: {t_stat}, P-Value: {p_value}")
    if p_value < 0.05:
        print("Result: Reject Null Hypothesis. Risk differs by Gender.")
    else:
        print("Result: Fail to Reject Null Hypothesis.")