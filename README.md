
# Customer Churn Prediction

## Project Overview

This project uses machine learning to predict whether a telecommunications customer is likely to discontinue their service.

The objective is to identify customers at risk of leaving so that businesses can make better customer-retention decisions.

## Dataset

- **Dataset:** Telco Customer Churn
- **Records:** 7,043 customers
- **Features:** 21 columns
- **Target variable:** Churn

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Seaborn
- Streamlit
- Joblib

## Machine Learning Models

- Logistic Regression
- Random Forest Classifier

## Model Evaluation

Models are evaluated using:

- Accuracy
- Precision
- Recall
- Confusion Matrix

Recall for the churn class is particularly important because the project aims to identify customers likely to leave.

## Streamlit Application

The application allows users to enter customer details and receive a churn prediction with its estimated probability.

## Project Structure

```text
Customer-Churn-Prediction/
├── models/
├── customer_churn.ipynb
├── streamlit_app.py
├── requirements.txt
└── README.md
```

## Author

**DerexDcoder**
