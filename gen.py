import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("WA_Fn-UseC_-Telco-Customer-Churn.csv")

plt.figure()
plt.bar(
    df['gender'].value_counts().index,
    df['gender'].value_counts().values
)
plt.xlabel("Gender")
plt.ylabel("Number of Customers")
plt.title("Male vs Female Customers")
plt.show()


