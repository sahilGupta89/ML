# Predict the onset of diabetes based on diagnostic measures
import pandas as pd
import matplotlib.pyplot as plt
plt.rc("font", size=14)
from sklearn.linear_model import LogisticRegression
from sklearn.cross_validation import train_test_split
from sklearn import metrics
import numpy as np

# Predict variable (desired target):
dataset = pd.read_csv('diabetes.csv')
print(dataset.shape)

feature_cols = ['Pregnancies', 'Glucose', 'BloodPressure', 'Insulin','BMI','DiabetesPedigreeFunction','Age']
X = dataset[feature_cols]
y = dataset['Outcome']

#Test and Train data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)

LR = LogisticRegression(C=1e5, solver='lbfgs')
LR.fit(X, y)
# Taking the Prdeicted value
y_pred=LR.predict(X_test)


# Model Evaluation using Confusion Matrix
cnf_matrix = metrics.confusion_matrix(y_test, y_pred)
cnf_matrix

print("Accuracy:",metrics.accuracy_score(y_test, y_pred))
print("Precision:",metrics.precision_score(y_test, y_pred))