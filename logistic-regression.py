import pandas as pd
import statsmodels.api as sm
from sklearn.preprocessing import LabelEncoder

try:
    data = pd.read_csv('./titanic.csv')
except FileNotFoundError:
    print("Error: The file 'titanic.csv' was not found. Please check your file name and path.")
    exit()

data['Fare'] = data['Fare'].fillna(data['Fare'].median())

# Dependent Variable (Y): Survived (The outcome we predict)
Y_log = data['Survived']

# Independent Variables (X): Our predictors (Fare and Sex_Numeric)
X_log = data[['Fare', 'Sex']]

# Add the constant (intercept) term for the regression equation
X_log = sm.add_constant(X_log)

# Initialize the Logistic Regression (Logit) model
logit_model = sm.Logit(Y_log, X_log)

logit_results = logit_model.fit()

print(logit_results.summary())
