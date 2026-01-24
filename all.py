import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("WA_Fn-UseC_-Telco-Customer-Churn.csv")

# Clean TotalCharges (good practice)
df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')


# Convert tenure into categories
df['TenureGroup'] = pd.cut(
    df['tenure'],
    bins=[0, 12, 24, 48, 72],
    labels=['0-1 Year', '1-2 Years', '2-4 Years', '4-6 Years']
)

# Categorical columns to plot
columns = [
    'PhoneService',
    'MultipleLines',
    'InternetService',
    'OnlineSecurity',
    'OnlineBackup',
    'DeviceProtection',
    'gender',
    'TenureGroup'
]

# Loop through each column
for col in columns:
    counts = df[col].value_counts()


    # PIE CHART
    plt.figure(figsize=(6, 4))
    plt.pie(counts.values, labels=counts.index.astype(str), autopct='%1.1f%%')
    plt.title(f"{col} Distribution (Pie Chart)")
    plt.show()