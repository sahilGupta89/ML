import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

features = ['variance','skewness','curtosis','entropy','class']
bankdata = pd.read_csv("data_banknote_authentication.txt",names = features)


bankdata.shape
bankdata.head()

X = bankdata.drop('class', axis=1)
y = bankdata['class']

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.5)

print(X_train.T.shape,y_train[:1].shape)

# plt.scatter(X_train[:0],y_train[:1])
# plt.show()


from sklearn.svm import SVC
svclassifier = SVC(kernel='rbf',C=25.0)
svclassifier.fit(X_train, y_train)

y_pred = svclassifier.predict(X_test)
# plt.plot(X_test,y_pred)
# plt.show()

from sklearn.metrics import classification_report, confusion_matrix
print(confusion_matrix(y_test,y_pred))
print(classification_report(y_test,y_pred))