import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("WA_Fn-UseC_-Telco-Customer-Churn.csv")

gender_churn = df.groupby(['gender', 'Churn']).size().unstack()

print(gender_churn)

gender_churn.plot(kind='bar')
plt.xlabel("Gender")
plt.ylabel("Number of Customers")
plt.title("Gender-wise Churn Analysis")
plt.show()

