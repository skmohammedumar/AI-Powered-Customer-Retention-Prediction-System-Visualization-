import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("WA_Fn-UseC_-Telco-Customer-Churn.csv")

# Count senior citizens
counts = df['SeniorCitizen'].value_counts()

# Plot
plt.figure()
plt.bar(['Not Senior Citizen', 'Senior Citizen'], counts.values)

plt.xlabel("Customer Type")
plt.ylabel("Number of Customers")
plt.title("Senior Citizen Distribution")

plt.show()
