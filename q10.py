# -*- coding: utf-8 -*-
"""
Created on Sun Dec 17 02:38:35 2023

@author: SYED ZAHEER HOSSAIN
"""

import pandas as pd
import random as ran

df=pd.DataFrame(columns=['a','b','c','d','e','f'])

def unique(x,y):
    if x[:2]!=y[:2]:
        t=y[0]
        y[0]=x[0]
        for i in range(1,len(y)):
            if y[i]==y[0]:
                y[i]=t
        y[1]=x[1]
        for i in range(2,len(y)):
            if y[i]==y[1]:
                y[i]=t
    x=['a']+x+['a']
    y=['a']+y+['a']
    return [x,y]

def tsp_d(df,iteration_df):
    distance=[]
    print(df)
    for i in iteration_df['paths']:
        add=0
        for j in range(len(i)-1):
            add+=df.loc[i[j]][i[j+1]]
        distance.append(add)
    iteration_df['distance']=distance
    print(iteration_df)
    return iteration_df

def tsp(iteration_df):
    total_fitness=sum(iteration_df['distance'])
    iteration_df['relative_fitness']=total_fitness/iteration_df['distance']
    total_relative_fitness=sum(iteration_df['relative_fitness'])
    iteration_df['probability']=iteration_df['relative_fitness']/total_relative_fitness
    cdf=[]
    s=0
    for i in iteration_df['probability']:
        s+=i
        cdf.append(s)
    iteration_df['cdf']=cdf
    
#city table
df['a']=[0,5,6,8,2,1]
df['b']=[5,0,6,3,2,3]
df['c']=[1,6,0,4,4,5]
df['d']=[4,6,8,0,2,1]
df['e']=[3,6,8,2,0,3]
df['f']=[2,5,6,7,2,0]

df.index=['a','b','c','d','e','f']

df=df.transpose()

print(df)

paths=[]
for i in range(4):
    path=['a']
    roots=['b','c','d','e','f']
    for j in range(5):
        v=ran.choices(roots)
        roots.remove(v[0])
        path.append(v[0])
    path.append('a')
    paths.append(path)
    
print(path)

iteration_df=pd.DataFrame()
iteration_df['paths']=paths
print(iteration_df)

iteration_df=tsp_d(df,iteration_df)
print(iteration_df)

df1=iteration_df.copy()
tsp(iteration_df)
print(iteration_df)

#parents
parents=[]
j=-1
while len(parents)<2:
    random_number=ran.random()
    for row,i in enumerate(iteration_df['cdf']):
        if i>random_number:
            if j!=row:
                parents.append(iteration_df.iloc[row].paths)
            if j==-1:
                j=row
            break
            
print(parents)

parent_ready=unique(parents[0][1:-1],parents[1][1:-1])
print(parent_ready)
print(parents)

#swap
off1=[]
off1.append(parent_ready[0][:2]+parent_ready[1][2:])
off1.append(parent_ready[1][:2]+parent_ready[0][2:])
print(off1)

off_distance=[]
for i in off1:
    add=0
    for j in range(len(i)-1):
        add+=df.loc[i[j]][i[j+1]]
    off_distance.append(add)
print(off_distance)

for d in range(len(off_distance)):
    for row,i in enumerate(iteration_df['distance']):
        if off_distance[d]<i:
            df1.iloc[row]=[off1[d],off_distance[d]]
            break
            
print(iteration_df)
print(df1)

iteration_df=df1.copy()
tsp(iteration_df)
print(iteration_df)