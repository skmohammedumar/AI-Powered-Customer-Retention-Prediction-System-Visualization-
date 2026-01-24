import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("WA_Fn-UseC_-Telco-Customer-Churn.csv")

# Data cleaning (VERY IMPORTANT)
df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')

# Create figure
plt.figure(figsize=(14, 6))

# Subplot 1: Monthly Charges
plt.subplot(1, 2, 1)
plt.hist(df['MonthlyCharges'], bins=30)
plt.title("Monthly Charges Distribution", fontsize=14)
plt.xlabel("Monthly Charges Amount")
plt.ylabel("Number of Customers")
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Subplot 2: Total Charges
plt.subplot(1, 2, 2)
plt.hist(df['TotalCharges'].dropna(), bins=30)
plt.title("Total Charges Distribution", fontsize=14)
plt.xlabel("Total Charges Amount")
plt.ylabel("Number of Customers")
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Adjust layout
plt.tight_layout()
plt.show()

