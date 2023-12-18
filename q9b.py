# -*- coding: utf-8 -*-
"""
Created on Sun Dec 17 01:51:36 2023

@author: SYED ZAHEER HOSSAIN
"""

#importing required datasets
import pandas as pd
import random

df=pd.DataFrame()
pd.set_option('display.max_columns',8)

global size
size=5

def binary_to_decimal(x):
    return int(x,2)

#Uniform Crossover
#x1,x4    x2,x3
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

def iteration(x,df):
    def fitness_fun(x):
        fitness_func=2*x**2+3*x+1
        return fitness_func
    def decimal_to_binary(x):
        ch=bin(x).replace('0b','')
        if len(ch)<size:
            ch='0'+ch
        return ch

    #encoding
    string=[]
    initial_population=[]
    fitness=[]
    for i in range(len(x)):
        string.append('x{}'.format(i+1))
        initial_population.append(decimal_to_binary(x[i]))
        fitness.append(fitness_fun(x[i]))
    total_val_fitness=sum(fitness)
    avg_val_fitness=total_val_fitness/len(x)
    def probability_ExpectedCount(x,y):
        return x/y
    probability=[]
    expected_count=[]
    fx = []
    for i in x:
        fx.append(fitness_fun(i))
    for i in fitness:
        probability.append(probability_ExpectedCount(i,total_val_fitness))
        expected_count.append(probability_ExpectedCount(i,avg_val_fitness))
    df['String']=string
    df['Initial_Population']=initial_population
    df['x']=x
    df['f(x)']=fx
    df['Fitness']=fitness
    df['Probability']=probability
    df['Expected_Count']=expected_count
    df['Actual_Count']=round(df['Expected_Count'])
    return df

#given
x=[9,11,13,15]
max_gen=2
df=iteration(x,df)

print(df)

for j in range(max_gen):
    offsprings=[]
    offsprings.extend(crossover(df['Initial_Population'][2],df['Initial_Population'][3]))
    offsprings.extend(crossover(df['Initial_Population'][1],df['Initial_Population'][0]))

    off_x=[]
    for i in offsprings:
        off_x.append(binary_to_decimal(i))
        
    df=pd.DataFrame()
    df=iteration(off_x,df)
    print(df)

# offsprings=[]
# offsprings.extend(crossover(df['Initial_Population'][2],df['Initial_Population'][3]))
# offsprings.extend(crossover(df['Initial_Population'][1],df['Initial_Population'][0]))

# off_x=[]
# for i in offsprings:
#     off_x.append(binary_to_decimal(i))

# df1=pd.DataFrame()
# df1=iteration(off_x,df1)
# print(df1)

# offsprings2=[]
# offsprings2.extend(crossover(df1['Initial_Population'][2],df1['Initial_Population'][3]))
# offsprings2.extend(crossover(df1['Initial_Population'][1],df1['Initial_Population'][0]))
# off_x2=[]
# for i in offsprings2:
#     off_x2.append(binary_to_decimal(i))
    
# df2=pd.DataFrame()
# df2=iteration(off_x2,df2)
# print(df2)

