import pandas as pd
import numpy as np
from sklearn.neighbors import KNeighborsClassifier , KNeighborsRegressor
from sklearn.model_selection import train_test_split
# import  datetime
import matplotlib.dates as mdates
myFmt = mdates.DateFormatter('%d')


import matplotlib.pyplot as plt   # Import matplotlib

names=['TIME','PREV_CLOSE' ,'OPEN_PRICE','BID_PRICE','OFFER_PRICE','OUTCOME']
stock = pd.read_csv('yahoo.csv',names=names)

replacements = {
   'OUTCOME': {
      'up': 1,
      'down': 0
   }
}

import datetime as dt

stock.replace(replacements,inplace=True)
# print(type(stock['TIME'][0]))

# print('hi',pd.to_numeric(stock['OUTCOME']))
print('ll',stock.head())

X1 = stock.iloc[0:,1:5]
Y = stock.iloc[0:,5:]
# print('Y',Y['OUTCOME'],)

X_train, X_test, y_train, y_test = train_test_split(X1, Y['OUTCOME'], test_size=0.4, random_state=0)

neigh = KNeighborsClassifier(n_neighbors=3)
cluster = KNeighborsRegressor(n_neighbors=5)
neigh.fit(X1, Y['OUTCOME'])
cluster.fit(X1,Y['OUTCOME'])
print('>>>>>.',neigh.predict(X_test))
print('>>>>>.',cluster.predict(X_test))

y_pred=neigh.predict(X_test)

# Model Evaluation using Confusion Matrix

from sklearn import metrics

cnf_matrix = metrics.confusion_matrix(y_test, y_pred)
cnf_matrix

print("Accuracy:",metrics.accuracy_score(y_test, y_pred))

ax = plt.subplots()
ax.xaxis.set_major_formatter(myFmt)
plt.plot(stock['TIME'],stock['OFFER_PRICE'])
# line_down, = plt.plot(stock['TIME'].iloc[0:20], label='Line 2')
# plt.legend()


plt.show()