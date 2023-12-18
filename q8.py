# -*- coding: utf-8 -*-
"""
Created on Sun Dec 17 01:37:50 2023

@author: SYED ZAHEER HOSSAIN
"""
#declaration of fuzzy set
a,b=[],[]
fuzzy_sets=[a,b]

#user input to fuzzy set
for i in range(2):
    print("Insert for fuzzy set number : ",i+1)
    for j in range(3):
        print('Membership value of x{}'.format(j+1))
        x=float(input())
        fuzzy_sets[i].append(('x{}'.format(j+1),x))
        
a=fuzzy_sets[0]
b=fuzzy_sets[1]
print("The fuzzy sets are "+ str(a)+ "and " + str(b) + "\n")

def fuzzy_operation(a,b):
    result=[]
    for j in range(3):
        result.append(('x{}'.format(j+1),(a[j][1]*b[j][1])/(a[j][1]+b[j][1])))
    return result

result = fuzzy_operation(a, b)

print("The result of the operation is " + str(result))