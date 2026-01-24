📊 Customer Churn Analysis
📌 Project Description

This project analyzes a telecom customer dataset to understand customer churn behavior.
It focuses on data cleaning, exploratory data analysis (EDA), visualization, and feature encoding to prepare the data for machine learning models.

📁 Dataset Information

The dataset contains customer details such as:

gender

SeniorCitizen

Partner

Dependents

MonthlyCharges

TotalCharges

PaymentMethod

Contract

InternetService

Churn (Target Variable)

🛠️ Technologies Used

Python

Pandas

Matplotlib

Jupyter Notebook

🔧 Data Preprocessing Steps

Converted TotalCharges to numeric values

Handled missing values

Converted Churn from Yes/No → 1/0

Applied One-Hot Encoding to categorical columns

Prepared dataset for analysis and modeling

📊 Exploratory Data Analysis (EDA)

The following analyses were performed:

Distribution of MonthlyCharges and TotalCharges

Overall Churn distribution

Gender-wise churn analysis

Senior Citizen distribution

Payment Method vs Churn

Visualizations using:

Bar charts

Histograms

Pie charts

Subplots

📈 Key Insights

Monthly and total charges vary significantly across customers

Certain payment methods show higher churn rates

Senior citizens tend to churn more than non-senior customers

Gender-wise churn percentages show noticeable differences

▶️ How to Run the Project

Clone the repository:

git clone https://github.com/your-username/customer-churn-analysis.git


Install required libraries:

pip install pandas matplotlib


Open and run the Jupyter Notebook:

jupyter notebook

📂 Project Structure
customer-churn-analysis/
│
├── data/            # Dataset (Excel / CSV)
├── notebook.ipynb   # Analysis notebook
├── plots/           # Generated visualizations
└── README.md        # Project documentation

🚀 Future Enhancements

Build machine learning models to predict churn

Feature selection and model optimization

Add accuracy, confusion matrix, and ROC curve

👤 Author

Shaik Kamalapuram Mohammed Umar


B.Tech in ECE with focus on Embedded Systems and Industrial IoT
