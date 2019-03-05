import  pandas as pd
import  numpy as np
import matplotlib.pyplot as plt
from  sklearn.linear_model import LinearRegression,LogisticRegression

dataset = pd.read_csv('../../datasets/typhoid_fever/US.4834000.csv')
print(dataset.head(), dataset.shape)

plt.show()