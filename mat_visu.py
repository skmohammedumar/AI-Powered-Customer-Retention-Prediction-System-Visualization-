import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("WA_Fn-UseC_-Telco-Customer-Churn.csv")

df = df.drop(['customerID'],axis=1)
print(df.head())
print(df.shape)
print(df.columns)

print(df['gender'].value_counts())
gender_churn = df.groupby(['gender', 'Churn']).size().unstack()
print(gender_churn)

df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')






