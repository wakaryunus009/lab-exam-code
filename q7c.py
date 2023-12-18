# -*- coding: utf-8 -*-
"""
Created on Sun Dec 17 01:28:38 2023

@author: SYED ZAHEER HOSSAIN
"""

#importing required packages
import math
import matplotlib.pyplot as plt

#Gaussian
c=int(input('Center Value: '))
s=int(input('Width Value: '))
m=int(input('Fuzzification Value: '))

def gaussian(x,c,s,m):
    m_value=math.exp(-(1/2)*(abs((x-c)/s))**m)
    return m_value

fuzzy_set=[]
for i in range(c*2+1):
    m_value=math.exp(-(1/2)*(abs((i-c)/s))**m)
    fuzzy_set.append((i,m_value))
    
x=[]
u=[]
for i in fuzzy_set:
    x.append(i[0])
    u.append(i[1])
    
# plt.plot(x,u,color='black')
# plt.show()

i=float(input('Enter number: '))
val=gaussian(i,c,s,m)

print('Resultant value is: ',val)

plt.plot(x,u,color='black')
plt.scatter(i,val,color='red')
plt.show()