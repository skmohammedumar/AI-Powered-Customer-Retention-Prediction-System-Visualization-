# AI-Powered-Customer-Retention-Prediction-System-Visualization-
📊 Project Overview

This project analyzes a telecom company's customer data to understand customer churn patterns. The goal is to identify factors that influence churn and visualize trends using Python.

🗂 Dataset

The dataset contains customer information with attributes such as:

gender – Customer gender

SeniorCitizen – Whether the customer is a senior citizen (1 = Yes, 0 = No)

MonthlyCharges – Monthly subscription amount

TotalCharges – Total billed amount

Churn – Whether the customer has churned (Yes/No)

PaymentMethod – Payment method used by the customer

…and other service-related features

Note: Some columns were converted to numeric (e.g., TotalCharges) to handle missing or non-numeric values.

🛠 Tools Used

Python 3.x

Pandas

Matplotlib & Seaborn

Jupyter Notebook

🔍 Analysis Performed

Data Cleaning – Converted non-numeric columns, handled missing values.

Exploratory Data Analysis (EDA) –

Distribution of MonthlyCharges and TotalCharges.

Customer churn counts and percentages (overall, gender-wise).

Senior citizen distribution.

Churn analysis by PaymentMethod.

Visualizations –

Histograms for numeric distributions

Bar charts for categorical distributions

Pie charts for churn percentages

📈 Key Insights

Monthly charges and total charges vary widely across customers.

Senior citizens have a higher churn tendency compared to non-senior customers.

Certain payment methods are associated with higher churn rates.

Female and male customers show different churn percentages.

🔗 How to Run

Clone the repository:

git clone https://github.com/yourusername/churn-analysis.git


Navigate to the project folder:

cd churn-analysis


Install dependencies:

pip install -r requirements.txt


Open the Jupyter Notebook and run the analysis:

jupyter notebook churn_analysis.ipynb

📂 Folder Structure
churn-analysis/
│
├── data/                  # Excel/CSV dataset
├── notebooks/             # Jupyter notebooks
├── plots/                 # Saved plots
├── requirements.txt       # Python dependencies
└── README.md              # Project documentation

📌 Future Work

Build predictive machine learning models to predict churn.

Explore additional features influencing churn, like tenure, contract type, and services used.

Perform feature engineering and model optimization.

💻 Author

Shaik Kamalapuram Mohammed Umar

Passionate about data analysis and machine learning

B.Tech in ECE with focus on Embedded Systems and Industrial IoT
