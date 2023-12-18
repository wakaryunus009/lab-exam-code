# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 22:30:54 2023

@author: SYED ZAHEER HOSSAIN
"""

#genetic algorithm

def fitness(chromosome):
    return (2*chromosome**2+3*chromosome+1)

# def DecimalToBinary(num,nump):
#     if num >= 1:
#         DecimalToBinary(num // 2)
#     nump+=str(num%2,n)
#     return int(nump)

def convert_pop_to_binary(population,chromosome_size) :
    binr = [bin(population[i])[2:] for i in range(len(population))]
    for i in range(len(binr)):
        if len(binr[i])<chromosome_size:
            for j in range(chromosome_size - len(binr[i])):
                binr[i] = str("0") + binr[i]
    return(binr)

def binaryToDecimal(n):
    return int(n,2)

def single_crossover(parent1,parent2,point):
    child1 = parent1[:point] + parent2[point:]
    child2 = parent2[:point] + parent1[point:]
    return child1,child2
    
if __name__ == '__main__':
    max_gen=100
    chromosome_size=5
    # population= [13,24,8,19]
    population = [9,11,13,15]
    binpop = convert_pop_to_binary(population, chromosome_size)
    for i in range(max_gen):
        fitness_values = [fitness(chr) for chr in population]
        sum=0
        for i in fitness_values:
            sum += i 
        avg=sum/len(fitness_values)
        actual_count = [round(i/avg) for i in fitness_values]
        # actual_count = [2,2,1,1,1]
        child = []
        double = []
        single = []
        for i,values in enumerate(actual_count):
            if values == 2:
                double.append(i)
            elif values == 1:
                single.append(i)
                
        # print(double,single)
        # if(len(double)>=2):
        #     print(double[0],double[1])
        #     print(double[0],double[1])
        # elif(len(double) == 1 and len(single)==1):
        #     print(double[0],single[0])
        # elif(len(double) == 1 and len(single)==2):
        #     print(double[0],single[0])
        #     print(double[0],single[1])
        # elif(len(single)>=2):
        #     for i in range(len(single)-len(single)%2):
        #         if i%2 == 0:
        #             print(single[i],single[i+1])
        
        if(len(double)>=2):
            child1,child2 = single_crossover(binpop[double[0]], binpop[double[1]], 2) # print(double[0],double[1])
            child3,child4 = single_crossover(binpop[double[0]], binpop[double[1]], 2) # print(double[0],double[1])
            child.append(child1)
            child.append(child2)
            child.append(child3)
            child.append(child4)
        elif(len(double) == 1 and len(single)==1):
            child2,child2 = single_crossover(binpop[double[0]], binpop[single[0]], 2) # print(double[0],single[0])
            child.append(child1)
            child.append(child2)
        elif(len(double) == 1 and len(single)==2):
            child1,child2 = single_crossover(binpop[double[0]], binpop[single[0]], 4) # print(double[0],single[0])
            child3,child4 = single_crossover(binpop[double[0]], binpop[single[1]], 2)# print(double[0],single[1])
            child.append(child1)
            child.append(child2)
            child.append(child3)
            child.append(child4)
        elif(len(single)>=2):
            for i in range(len(single)-len(single)%2):
                if i%2 == 0:
                    child1,child2 = single_crossover(binpop[single[i]], binpop[single[i+1]], 2) # print(single[i],single[i+1])
                    child.append(child1)
                    child.append(child2)
        population = [binaryToDecimal(i) for i in child]
        # print(binpop[single[1]])
    # child.append(single_crossover(binpop[double[0]], binpop[single[0]], 4))
    # print(child[0])
    print(actual_count)
    print(fitness_values)
    print(max(fitness_values))
    # print(convert_pop_to_binary(population, chromosome_size))
    # x = [i for i in population]
    