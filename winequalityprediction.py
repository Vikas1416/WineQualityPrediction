# -*- coding: utf-8 -*-
"""WineQualityPrediction.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1udGrduoKrCI02Hyar3aN8kA7FPnhuTJa

Importing Libraries
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
import seaborn as sns
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

wine_data = pd.read_csv('winequality-red.csv')

wine_data.head()

wine_data.shape

wine_data.isnull().sum()

"""Data analysis and visulaization"""

wine_data.describe() #for statical analysis

# number of values for each quality
sns.catplot(x = 'quality', data = wine_data, kind = 'count')

# volatile acidity vs quality
plot = plt.figure(figsize = (5,5))
sns.barplot(x='quality' , y = 'volatile acidity', data = wine_data)

plot = plt.figure(figsize = (5,5))
sns.barplot(x = 'quality', y= 'citric acid', data = wine_data)

"""Correlation
1. Positive correlation
2. Negative correlation
"""

correlation = wine_data.corr()

# heatmap to understand the correlation
plt.figure(figsize=(10,10))
sns.heatmap(correlation, cbar=True , square = True, fmt= '.1f', annot = True , annot_kws = {'size':8}, cmap = "Blues")

"""Data PreProcessing
(Separating data)
"""

X = wine_data.drop('quality', axis = 1)

print(X)

"""Label binary session(Binarization)"""

Y = wine_data['quality'].apply(lambda y_value: 1 if y_value>=7 else 0)

print(Y)

"""Spliting data into training and test data"""

X_train,X_test, Y_train,Y_test = train_test_split(X,Y, test_size = 0.2 , random_state = 2)

print(X_train)

print(Y_test)

print(Y.shape, Y_train.shape)

"""traing model"""

model = RandomForestClassifier()

model.fit(X_train, Y_train)

# accuracy score
X_test_prediction = model.predict(X_test)
test_data_accuarcy = accuracy_score(X_test_prediction,Y_test )

print(test_data_accuarcy)

input_data = (7.4,0.7,0.0,1.9,0.076,11.0,34.0,0.9978,3.51,0.56,9.4)
# changing the input_data into numpy array
input_data_as_numpy_array = np.asarray(input_data)
# reshape
input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

prediction = model.predict(input_data_reshaped)
print(prediction)

if (prediction[0]==1):
  print('Good Quality Wine')
else:
  print('Bad Quality Wine')

