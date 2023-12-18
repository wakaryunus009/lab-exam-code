# -*- coding: utf-8 -*-
"""
Created on Sun Dec 17 17:19:16 2023

@author: SYED ZAHEER HOSSAIN
"""

#importing required packages
import random

# 3 ta plane  
# 5 ta crew a,b,c,d,e
# a b c  000
# c d e  100
# a d e  011
# a b c  100
# d b c  011
# d a e  100
# b a e  011
# b d c  100

# a b c  1 1 1 0 0  3
# c d e  0 0 2 1 1  4
# a d e  1 0 0 2 2  5
# a b c  2 1 1 0 0  4
# d b c  0 0 2 1 1  4
# d a e  1 0 0 2 2  5
# b a e  2 1 1 0 0  4
# b d c  0 0 2 1 1  4

def fitness(crew,work_days_count):
    for i in crew:
        work_days_count[i]+=1
    penalty = sum(max(0, work_days_count[crew] - MAX_WORK_DAYS) for crew in work_days_count)
    return 1 / (1 + penalty)

def crossover(parent1, parent2):
    crossover_point = random.randint(1, NUM_DAYS - 1)
    child = parent1[:crossover_point] + parent2[crossover_point:]
    if len(set(child))!=len(child):
        for i in set(child):
            dup=0
            for j in child:
                if i==j:
                    dup+=1
                    if dup==2:
                        x=list(work_count.values())
                        found=False
                        while not found:
                            for k in range(5):
                                if list(work_count.keys())[k] not in child and work_count[list(work_count.keys())[k]]<=1:
                                    child[child.index(j)]= list(work_count.keys())[k]
                            found=True

    return child

def crew_fun(crew,work_count,generation):
    for _ in range(generation):
        fit_score=[]
        for i in combi:
            work_days_count=work_count.copy()
            fit_score.append(fitness(i,work_days_count))
        parents = [combi[i] for i in range(len(fit_score)) if random.random() < fit_score[i]]

        try:
            parent1, parent2 = random.sample(parents, 2)
            child = crossover(parent1, parent2)
            min1=min(fit_score)
            combi.remove(combi[fit_score.index(min1)])
            combi.insert(fit_score.index(min1),child)
            fit_score.remove(min1)

        except:
            pass
        fit_score=[]
        for i in combi:
            work_days_count=work_count.copy()
            fit_score.append(fitness(i,work_days_count))
        best_solution = combi[fit_score.index(max(fit_score))]
        combi.remove(best_solution)
        new_combi=[]
        complete=[]
        al=['a','b','c','d','e']
        for i in best_solution:
            work_count[i]+=1
        for i in al:
            if i not in best_solution:
                work_count[i]=0
        for i in work_count:
            if work_count[i]>=2:
                complete.append(i)
        for i in al:
            if i not in complete:
                new_combi.append(i)
        if len(new_combi)>3:
            new_combi=new_combi[:3]
        combi.append(new_combi)
    return best_solution

global work_count,MAX_WORK_DAYS
work_count={'a':0,'b':0,'c':0,'d':0,'e':0}
POPULATION_SIZE = 8
MAX_WORK_DAYS=2

combi=[]
for _ in range(8):
    crew=['a','b','c','d','e']
    c=[]
    for _ in range(3):
        s=random.choice(crew)
        crew.remove(s[0])
        c.append(s[0])
    combi.append(c)
    
generation=20
for i in range(10):
    print(crew_fun(combi,work_count,generation))

print(work_count)