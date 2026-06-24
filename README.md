# Customer Churn Prediction App

## Overview

This project is a Machine Learning-based Customer Churn Prediction application developed using Python and Streamlit. The model predicts whether a customer is likely to churn based on customer demographics, subscription details, usage patterns, and spending behavior.

## Features

* User-friendly Streamlit interface
* Real-time customer churn prediction
* Data preprocessing using Scikit-learn
* Machine Learning model integration
* Interactive input fields for customer information

## Technologies Used

* Python
* Streamlit
* Pandas
* NumPy
* Scikit-learn
* Joblib

## Project Structure

```
project/
│
├── app.py                # Streamlit application
├── model.pkl             # Trained machine learning model
├── scaler.pkl            # Saved scaler
├── encoder.pkl           # Saved encoder
├── dataset.csv           # Dataset
├── requirements.txt      # Required libraries
└── README.md             # Project documentation
```

## Installation

1. Clone the repository:

```
git clone <repository_link>
```

2. Navigate to the project directory:

```
cd project
```

3. Create a virtual environment:

```
python -m venv .venv
```

4. Activate the virtual environment:

Windows:

```
.venv\Scripts\activate
```

5. Install dependencies:

```
pip install -r requirements.txt
```

## Run the Application

```
streamlit run app.py
```

## Input Features

* Age
* Gender
* Tenure
* Usage Frequency
* Support Calls
* Payment Delay
* Subscription Type
* Contract Length
* Total Spend

## Model Performance

The trained model achieved approximately 99% cross-validation accuracy on the dataset.

## Author

Chandni Kumari
Machine Learning Intern
