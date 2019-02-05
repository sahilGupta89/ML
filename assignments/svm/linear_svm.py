import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn import svm

digits = datasets.load_digits()
# print(digits.data)
# print(digits.target)
# print(digits.images[0])

clf = svm.SVC(gamma=0.001, C=100)
x,y = digits.data[:-1],digits.target[:-1]
clf.fit(x,y)
print(digits.data[-1])
data = [digits.data[-1]]
print(data)
p = clf.predict(data)

print(clf.score(x,y))

print('prediction',p)
plt.imshow(digits.images[-1],cmap=plt.cm.gray_r ,interpolation="nearest")
plt.show()