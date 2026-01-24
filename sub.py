import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("WA_Fn-UseC_-Telco-Customer-Churn.csv")


df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')

churn_count = df['Churn'].value_counts()

plt.figure()

plt.subplot(1, 2, 1)
plt.hist(df['MonthlyCharges'])
plt.title("Monthly Charges")

plt.subplot(1, 2, 2)
plt.bar(churn_count.index, churn_count.values)
plt.title("Churn Count")

plt.show()