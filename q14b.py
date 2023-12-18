# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 08:28:16 2023

@author: SYED ZAHEER HOSSAIN
"""

import pandas as pd
import random as ran

def fitness_fun(val):
    # decimal sum
    d_sum=0
    for i in val:
        d_sum += int(str(i), 8)
    # decimal to octal
    o_sum = oct(d_sum)
    o_sum= o_sum.replace('0o','')
    return int(o_sum)

df=pd.DataFrame()
df_main=pd.DataFrame()

def crossover(x,y):
    x=list(x)
    y=list(y)
    cut=ran.choice([1,2,3,4,5,6])
    x1=x[:cut]+y[cut:]
    y1=y[:cut]+x[cut:]
    return (x1,y1)

def code(df,df_main):
    total_fit=sum(df['fitness_val'])
    df['probability']=df['fitness_val']/total_fit
    avg_val_fitness=total_fit/len(df)
    df['expected_count']=df['fitness_val']/avg_val_fitness
    df['actual_count']=round(df['expected_count'])
    offsprings=[]
    df=df.sort_values(by='expected_count')
    df=df.reset_index()
    df=df.drop(['index'],axis=1)
    offsprings.extend(crossover(df['population'][2],df['population'][3]))
    fitness=[]
    for i in offsprings:
        fitness.append(fitness_fun(i))
    df_main=df_main.sort_values(by='fitness_val')
    df_main=df_main.reset_index()
    df_main=df_main.drop(['index'],axis=1)
    fit=fitness.copy()
    fit=sorted(fit,reverse=True)
    for i in fitness:
        for row,j in enumerate(df_main['fitness_val']):
            if j<i:
                # df_main.loc[row]=[list(offsprings[fitness.index(i)]),i]
                df_main.at[row, 'population'] = list(offsprings[fitness.index(i)])
                df_main.at[row, 'fitness_val'] = i
                break
    return df,df_main

#population
population=[]
total_population=10
gene=8
for _ in range(total_population):
    pop=[]
    for _ in range(gene):
            pop.append(ran.choice(['1','2','3','4','5','6','7','0']))
    population.append(pop)

fitness=[]
for i in population:
    fitness.append(fitness_fun(i))

df['population']=population
df['fitness_val']=fitness
df_main=df.copy()

print(df)

generation=100
for _ in range(generation):
    df,df_main=code(df,df_main)
    df=df_main.copy()

print(df)