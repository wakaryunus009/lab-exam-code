# -*- coding: utf-8 -*-
"""
Created on Sun Dec 17 17:01:10 2023

@author: SYED ZAHEER HOSSAIN
"""

def crossover(x,y):
    x=list(x)
    y=list(y)
    for i in range(len(x)):
        #tossing coin
        if i%2==0:
            pass
        else:
            t=x[i]
            x[i]=y[i]
            y[i]=t
    x=''.join(x)
    y=''.join(y)
    return (x,y)

def iteration(x):
    def fitness_fun(x):
        fitness_func=(int(x[0])+int(x[1]))-(int(x[2])+int(x[3]))+(int(x[4])+int(x[5]))-(int(x[6])+int(x[7]))
        return fitness_func
    #encoding
    string=[]
    fitness=[]
    for i in range(len(x)):
        string.append('x{}'.format(i+1))
        fitness.append(fitness_fun(x[i]))
    total_val_fitness=sum(fitness)
    val1=zip(string,x,fitness)
    val=list(val1)
    val=sorted(val,key=lambda x:x[2])[::-1]
    return val
x=['65413532','87126601','23921285','41852094']
val1=iteration(x)

print("phenotype before performing cross over \n")
for i in val1:
    print(str(i) + "\n")

#cross-over with best fitted middle point
best1=val1[0][1]
best2=val1[1][1]

off_1=best1[:int(len(best1)/2)]+best2[int(len(best2)/2):]
off_2=best2[:int(len(best2)/2)]+best1[int(len(best1)/2):]

best3=val1[2][1]

#cross-over with 2nd and 3rdbest fitted from 2nd and 6th position
off_3=best2[:2]+best3[2:6]+best2[6:]
off_4=best3[:2]+best2[2:6]+best3[6:]

off_5,off_6=crossover(best1,best3)

offspring=[off_1,off_2,off_3,off_4,off_5,off_6]

new_gen=iteration(offspring)

print("phenotype after performing cross over \n")
for i in new_gen:
    print(str(i) + "\n")