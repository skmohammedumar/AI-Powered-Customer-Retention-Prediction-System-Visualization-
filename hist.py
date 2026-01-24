import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("WA_Fn-UseC_-Telco-Customer-Churn.csv")


plt.figure()
plt.hist(df['MonthlyCharges'])
plt.xlabel("Monthly Charges")
plt.ylabel("Frequency")
plt.title("Histogram: Monthly Charges Distribution")
plt.show()