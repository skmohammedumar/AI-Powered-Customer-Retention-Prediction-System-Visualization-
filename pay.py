import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("WA_Fn-UseC_-Telco-Customer-Churn.csv")

payment_churn = df.groupby(['PaymentMethod', 'Churn']).size().unstack()

payment_churn.plot(kind='bar')
plt.xlabel("Payment Method")
plt.ylabel("Number of Customers")
plt.title("Payment Method vs Churn")
plt.show()
