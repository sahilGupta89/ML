import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

testdata = pd.read_csv('test.csv')
x_data = testdata['x'].values
y_data = testdata['y'].values
x_mean = x_data.mean()
y_mean = y_data.mean()
Y_pred = []
numer = 0
denom = 0

print(x_data,y_data)
for i in range(len(x_data)):
    numer += (x_data[i] - x_mean)*(y_data[i] - y_mean)
    denom += (x_data[i]-x_mean)**2

SLOP = numer/denom
COFFI = y_mean - (SLOP*x_mean)

def linearRegression():
    plt.scatter(x_data,y_data)
    plt.scatter(testdata['x'],testdata['y'])
    plt.xlim([0, testdata['x'].max()])
    plt.ylim([0, testdata['y'].max()])
    plt.ylabel('Y')
    plt.ylabel('X')
    plt.title('linear regression on test dataset')
    plt.plot(x_data,Y_pred)
    plt.show()

def predict(m,c):
    for j in range(len(x_data)):
        Y_pred.append((m*x_data[j])+c)

# RSS,TSS
def accuracy():
    rss, tss = 0, 0
    for k in range(len(x_data)):
        rss += (y_data[k] - Y_pred[k]) ** 2
        tss += (y_data[k] - y_mean) ** 2
    rse = (rss / len(x_data))**.5
    r_squar = 1 - (rss / tss)
    print('RSE and R square:',rse,r_squar)

def predict2(x):
    return SLOP*x + COFFI

predict(SLOP,COFFI)
print("predicted",predict2(8))
linearRegression()
accuracy()
