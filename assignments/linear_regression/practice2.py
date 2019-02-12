from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import pandas as pd

digits = load_diabetes()
X,Y = digits.data , digits.target
dataset = pd.read_csv('train.csv')

print(dataset.head())
# X_train,X_test,y_train,y_test = train_test_split(X[:,0:1].flatten().reshape(-1,1),Y,test_size=0.33, random_state=42)
#
# model = LinearRegression()
# model.fit(X_train,y_train)
#
# y_pred = model.predict(X_test)
# plt.scatter(X_test[:,0:1].flatten().reshape(-1,1),y_test)
# plt.xlim([0, X_test[:,0:1].flatten().reshape(-1,1).max()])
# plt.ylim([0, y_test.max()])
# plt.ylabel('Y')
# plt.ylabel('X')
# plt.title('linear regression on test dataset')
# plt.plot(X_test[:,0:1].flatten().reshape(-1,1),y_pred)
# # print(X_test[:,0],y_test)
# plt.show()
#
# score = model.score(X_test,y_pred)
#
# print(score,model.intercept_)