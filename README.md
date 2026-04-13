# Car Price Prediction Web App

This is a full-stack Machine Learning project that predicts the selling price of used cars based on several features like present price, kilometers driven, fuel type, and age.

##  Project Overview
The goal of this project was to build a predictive model and deploy it as an interactive web application using **Flask**. The model helps users estimate the fair market value of a car before buying or selling.

##  Tech Stack
* **Language:** Python 3.x
* **Machine Learning:** Scikit-learn, Pandas, NumPy
* **Web Framework:** Flask
* **Frontend:** HTML5, CSS3
* **Tools:** Joblib (Model Serialization), Git/GitHub

##  Machine Learning Workflow

### 1. Data Preprocessing & Feature Engineering
* **Log Transformation:** Applied `log1p` to the 'Driven_Kms' feature to handle skewed data and improve model performance.
* **Categorical Encoding:** Converted categorical variables (Fuel Type, Seller Type, Transmission) into numerical format using manual encoding for better control in deployment.
* **Feature Scaling:** Standardized numerical features using `StandardScaler` to ensure all features contribute equally to the model.

## 2. Model Development & Evaluation
Algorithms Tested: Compared Linear Regression and Random Forest Regressor to find the best fit for the data.

Winning Model: Random Forest Regressor was selected as the final model due to its superior performance.

Performance Metrics: * Training Accuracy: 94.85%

R-squared Score (Test): 84.38% (Significant improvement over the Linear Regression baseline).

Mean Absolute Error (MAE): 0.72, indicating high precision in price estimation.

Robustness: Successfully handled outliers through log transformation and ensured the model generalizes well without overfitting.

##  Web Application Features
* **Interactive UI:** A clean, responsive two-column form for data entry.
* **Live Prediction:** Real-time price estimation after clicking the "Predict" button.
* **Input Validation:** * **Frontend:** HTML5 constraints to prevent negative numbers or empty fields.
    * **Backend:** Python logic to handle invalid inputs and prevent server crashes.
* **State Persistence:** The form retains user inputs even after submission for a better user experience.

##  Project Structure
```text
├── static/           # CSS files for styling
├── templates/        # HTML templates (index.html)
├── app.py            # Flask application logic
├── Car_model.pkl     # Trained Random Forest model
├── scaler.pkl        # Fitted StandardScaler object
└── requirements.txt  # Project dependencies

