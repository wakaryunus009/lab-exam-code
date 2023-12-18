# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 17:16:21 2023

@author: SYED ZAHEER HOSSAIN
"""

import pandas as pd
import statistics
import matplotlib.pyplot as plt
import sklearn.preprocessing as preprocessing
from sklearn.preprocessing import StandardScaler
import numpy as np

df = pd.read_csv("E:\SEMESTER 7 BTECH CSE\iris.csv",delimiter=',')
# print(df)

# q1

# print("Mean is")
# print()
# print(df.mean())
# print()
# print("Median is")
# print()
# print(df.median())
# print()
# print("Mode is")
# print()
# print(df.mode().head(1))
# print()
# print("Variance is")
# print()
# print(df.var())
# print()
# print("Standard deviation is")
# print()
# print(df.std())

#q2 

iris_setosa = df[df['Species'] == 'Iris-setosa']
iris_versicolor = df[df['Species'] == 'Iris-versicolor']
iris_virginica = df[df['Species'] == 'Iris-virginica']

# print(f"Iris-setosa shape: {iris_setosa.shape}")
# print(f"Iris-versicolor shape: {iris_versicolor.shape}")
# print(f"Iris-virginica shape: {iris_virginica.shape}")
# print(f"size of whole dataset :{df.shape}")

#q3

# std = df.std()

# x_axis = np.arange(len(df.columns[:df.shape[1]-1]))

plt.bar(df.columns[:df.shape[1]-1], iris_setosa.std())
# plt.xlabel("Features")
# plt.ylabel("Standard Deviation")
# plt.title("Features and Standard Deviation plot setosa")
# plt.show()

# plt.bar(df.columns[:df.shape[1]-1], iris_versicolor.std())
# plt.xlabel("Features")
# plt.ylabel("Standard Deviation")
# plt.title("Features and Standard Deviation plot versicolor")
# plt.show()

# plt.bar(df.columns[:df.shape[1]-1], iris_virginica.std(), )
plt.xlabel("Features")
plt.ylabel("Standard Deviation")
plt.title("Features and Standard Deviation plot")

plt.show()

# 5.5cm

#q4

# normalizer = preprocessing.Normalizer(norm="l2").fit(df[df.columns[:4]])

# iris_normalized = normalizer.transform(df[df.columns[:4]])
# iris_pd = pd.DataFrame(iris_normalized,columns=['SepalLengthCm','SepalWidthCm','PetalLengthCm','PetalWidthCm'])
# # iris_pd.insert( 4,"Species",df[df.columns[4]])
# print(iris_normalized)
# print(iris_pd)

# plt.bar(df.columns[:df.shape[1]-1], iris_pd.var())
# plt.bar(iris_pd.columns, iris_pd.var())
# plt.xlabel("Features")
# plt.ylabel("Variance")
# plt.title("Normalization and variance plot")
# plt.show()

# scaler = StandardScaler()
# df_std = pd.DataFrame(scaler.fit_transform(df[df.columns[:4]]), columns=df.columns[:4])

# print(df_std)




# # print(statistics.pstdev(df[1]))
# std = df.std()
# print(std)

# dff = df[df.columns[:df.shape[1]-1]]
# print(dff.mode)

# print(df.mode().head(1))

# print(df.shape[1])

# plt.bar(df.columns[:df.shape[1]-1], df.std())

# plt.show()

# print(df[df.columns[4]])

# normalizer = preprocessing.Normalizer(norm="l2").fit(df[df.columns[:4]])

# iris_normalized = normalizer.transform(df[df.columns[:4]])
# iris_pd = pd.DataFrame(iris_normalized,columns=['sepalw','sepalh','petalw','petall'])
# # iris_pd.insert( 4,"Species",df[df.columns[4]])
# print(iris_normalized)
# print(iris_pd)
# print(iris_pd.var())
# # print(df.columns)

# std = df.std()

# x_axis = np.arange(len(df.columns[:df.shape[1]-1]))

# plt.bar(x_axis+.20, iris_setosa.std(), width=0.2,label='setosa')
# plt.xlabel("Features")
# plt.ylabel("Standard Deviation")
# plt.title("Features and Standard Deviation plot setosa")
# plt.show()

# plt.bar(x_axis+.20*2, iris_versicolor.std(), width=0.2,label='versicolor')
# plt.xlabel("Features")
# plt.ylabel("Standard Deviation")
# plt.title("Features and Standard Deviation plot versicolor")
# plt.show()

# plt.bar(x_axis+.20*3, iris_virginica.std(), width=0.2,label='virginica')
# plt.xlabel("Features")
# plt.ylabel("Standard Deviation")
# plt.title("Features and Standard Deviation plot")
# plt.xticks(x_axis,df.columns[:df.shape[1]-1])
# plt.legend()
# plt.show()
