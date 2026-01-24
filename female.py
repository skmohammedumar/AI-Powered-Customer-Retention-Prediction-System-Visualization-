import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("WA_Fn-UseC_-Telco-Customer-Churn.csv")

plt.figure()
plt.pie(
    df[df['gender'] == 'Female']['Churn'].value_counts(),
    labels=df[df['gender'] == 'Female']['Churn'].value_counts().index,
    autopct='%1.1f%%'
)
plt.title("Female Customer Churn Percentage")
plt.show()
