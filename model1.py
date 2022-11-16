import pandas as pd
import pickle
import numpy as np
import sklearn
import matplotlib.pyplot as plt
import seaborn as sb

from sklearn import datasets

iris_data = pd.read_csv('iris-data-clean.csv')
df = pd.DataFrame(iris_data)

# def myfunction(x):
#     if x == "Setosa":
#         return 0
#     elif x == "Virginica":
#         return 1
#     else:
#         return 2
    
# df["class"] = df["class"].apply(myfunction)

X = df.iloc[:,0:4]
y = df['class']


from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state = 42)



logReg = LogisticRegression(solver = 'lbfgs', multi_class = 'multinomial', random_state = 42)
logReg.fit(X_train.values, y_train)


# deploy to the flask server
# flask server need to be started
pickle.dump(logReg, open('model1.pkl', 'wb'))  #serialize the object