import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("WA_Fn-UseC_-Telco-Customer-Churn.csv")

plt.figure()
plt.pie(
    df[df['gender'] == 'Male']['Churn'].value_counts(),
    labels=df[df['gender'] == 'Male']['Churn'].value_counts().index,
    autopct='%1.1f%%'
)
plt.title("Male Customer Churn Percentage")
plt.show()
