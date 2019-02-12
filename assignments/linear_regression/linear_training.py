from sklearn.model_selection import train_test_split
import pandas as pd

def trainme(file):
    dataset = pd.read_csv(file)
    X,Y = dataset['X'],dataset['Y']
    # [:, 0: 1].flatten().reshape(-1, 1)
    X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.33,
                                                        random_state=42)
    return X_train, X_test, y_train, y_test

