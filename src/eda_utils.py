import matplotlib.pyplot as plt
import seaborn as sns

def plot_loss_ratio_by_province(df):
    plt.figure(figsize=(12, 6))
    # Aggregate Loss Ratio
    agg = df.groupby('Province')[['TotalClaims', 'TotalPremium']].sum()
    agg['LossRatio'] = agg['TotalClaims'] / agg['TotalPremium']
    
    sns.barplot(x=agg.index, y=agg['LossRatio'], palette='viridis')
    plt.title('Loss Ratio by Province')
    plt.ylabel('Loss Ratio')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def plot_premium_distribution(df):
    plt.figure(figsize=(10, 6))
    sns.histplot(df['TotalPremium'], bins=50, kde=True, color='blue')
    plt.title('Distribution of Total Premium')
    plt.xlim(0, df['TotalPremium'].quantile(0.95)) # Remove outliers for viz
    plt.show()

def plot_claims_vs_premium_scatter(df):
    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=df, x='TotalPremium', y='TotalClaims', alpha=0.3)
    plt.title('Total Premium vs Total Claims')
    plt.show()