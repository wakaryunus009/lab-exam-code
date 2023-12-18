# -*- coding: utf-8 -*-
"""
Created on Sat Dec 16 22:48:50 2023

@author: SYED ZAHEER HOSSAIN
"""

#declaration of fuzzy set
a,b,c=[],[],[]
fuzzy_sets=[a,b,c]

#user input to fuzzy set
for i in range(3):
    print("Insert for fuzzy set number : ",i+1)
    for j in range(3):
        x=float(input('Membership value of x{}'.format(j+1)))
        fuzzy_sets[i].append(('x{}'.format(j+1),x))
        
print("The fuzzy sets are : " + str(fuzzy_sets) + "\n")

#performing union operation
result1=[]
for j in range(3):
    result1.append(('x{}'.format(j+1),max(fuzzy_sets[0][j][1],fuzzy_sets[1][j][1],fuzzy_sets[2][j][1])))
    
print("Result after performing union operation are " + str(result1) + "\n")

#performing intersection operation
result2=[]
for j in range(3):
    result2.append(('x{}'.format(j+1),min(fuzzy_sets[0][j][1],fuzzy_sets[1][j][1],fuzzy_sets[2][j][1])))
    
print("Result after performing union operation are " + str(result2)+ "\n")