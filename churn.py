import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("WA_Fn-UseC_-Telco-Customer-Churn.csv")



churn_count = df['Churn'].value_counts()

plt.figure()
plt.bar(churn_count.index, churn_count.values)
plt.xlabel("Churn")
plt.ylabel("Number of Customers")
plt.title("Customer Churn Distribution")
plt.show()