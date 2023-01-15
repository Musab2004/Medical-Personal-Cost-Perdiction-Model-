# -*- coding: utf-8 -*-
"""Untitled5.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1wlFA9y4QclzYb6T3wrGVpwA6YMsBaP4W
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
path = '/insurance.csv'
data_df=pd.read_csv(path)

categorical_columns = ['sex','children', 'smoker', 'region']
df_encode = pd.get_dummies(data = data_df, prefix = 'OHE', prefix_sep='_',
               columns = categorical_columns,
               drop_first =True,
              dtype='int8')
df_encode

corrmat = df_encode.corr()
corrmat["charges"].sort_values(ascending=True)

y=df_encode["charges"]
X=df_encode.drop(["charges"],axis = 1)
X_train, X_test, y_train, y_test=\
        train_test_split( \
                         X, y, \
                         test_size = 0.25, \
                         random_state = 0)
from sklearn.linear_model import LinearRegression
lin_reg = LinearRegression()
lin_reg.fit(X_train,y_train)
y_pred_sk = lin_reg.predict(X_test)
R_square_sk = lin_reg.score(X_test,y_test)
R_square_sk
# f,ax = plt.subplots(1,1,figsize=(14,6))
# import scipy as sp
# _,(_,_,r)= sp.stats.probplot((y_test - y_pred_sk),fit=True,plot=ax)
# ax.set_title('Actual vs Predicted values: \nQ-Q Plot')

# def costfunction(theta,X,y):
#     y_pred_norm =  np.matmul(X,theta)
#     cost=np.sum((y_pred_norm-y)**2)/X.shape[0]
#     # print(cost)
#     return cost
# theta=[1,1,1,1,1,1,1,1,1,1,1,1]

# def gradientdescent(iteration,step,theta,X1,y1):
#    X=X1.to_numpy()
#    y=y1.to_numpy()
#   #  print(costfunction(theta,X_train,y_train)) 
#    for i in range(0,iteration):
#      y_pred_norm =  np.matmul(X,theta)
#      print(y)
#      print(y_pred_norm)
#   #  print(X.transpose()*y_pred_norm)
#     # print(y_pred_norm-y)
#      value=np.matmul((y_pred_norm-y).transpose(),X)
#     #  value=(y_pred_norm-y).transpose()*
#     # print(value)
#     # print((step*value)/X.shape[0])
#   #  value=X.transpose()*(y_pred_norm-y
#     # print("value is :",value)
#     # print(theta)
#     # print(np.matmul(X,theta))
#     # print(value)
#      theta=theta-step*value/X.shape[0] 
#     #  print(theta)
#   #  print((y_pred_norm-y))

#     # print(np.matmul(X,theta))
#     #  print(costfunction(theta,X_train,y_train)) 
#   #  return theta
# costfunction(theta,X_train,y_train)
# gradientdescent(1000000,0.0007,theta,X_train,y_train)