import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("WA_Fn-UseC_-Telco-Customer-Churn.csv")


df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')


churn_count = df['Churn'].value_counts()

plt.figure()
plt.pie(churn_count.values, labels=churn_count.index, autopct='%1.1f%%')
plt.title("Churn Percentage")
plt.show()
