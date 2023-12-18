# -*- coding: utf-8 -*-
"""
Created on Sun Dec 17 01:06:03 2023

@author: SYED ZAHEER HOSSAIN
"""

# importing required packages
import matplotlib.pyplot as plt

def triangular(x,fuzzy):
    if fuzzy[1][1]!=1 and fuzzy[0][1]!=0 and fuzzy[2][0]!=0:
        return 'not triangular'
    if x<fuzzy[0][0]:
        return 0
    elif x>fuzzy[2][0]:
        return 0
    elif x>=fuzzy[0][0] and x<=fuzzy[1][0]:
        val=(x-fuzzy[0][0])/(fuzzy[1][0]-fuzzy[0][0])
        return val
    elif x>=fuzzy[1][0] and x<=fuzzy[2][0]:
        val=(fuzzy[2][0]-x)/(fuzzy[2][0]-fuzzy[1][0])
        return val

# Implementing Triangular Membership Function
#let fuzzy set be
a=[(3,0),(8,0),(6,1)]
a.sort()

x=[]
u=[]
for i in a:
    x.append(i[0])
    u.append(i[1])

# plt.plot(x,u)
# plt.show()

    
i=float(input('Enter number: '))
val=triangular(i,a)

print('Resultant value is: ',val)

plt.plot(x,u,color='black')
plt.scatter(i,val,color='red')
plt.show()