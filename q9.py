# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 20:25:58 2023

@author: SYED ZAHEER HOSSAIN
"""

# x = int(input("Enter the value of x"))

# func = (2*x**2)+(3*x)+1

# print(func)

import random

def fitness(chromosome):
    return sum([2*x**2 + 3*x + 1 for x in chromosome])
    # return sum([x**2])

def tournament_selection(population, k):
    return max(random.sample(population, k), key=fitness)

def single_point_crossover(parent1, parent2):
    # crossover_point = random.randint(1, len(parent1) - 1)
    crossover_point = 2
    child1 = parent1[:crossover_point] + parent2[crossover_point:]
    child2 = parent2[:crossover_point] + parent1[crossover_point:]
    return child1, child2

# def bit_flip_mutation(chromosome, p):
#     mutated_chromosome = chromosome.copy()
#     for i in range(len(mutated_chromosome)):
#         if random.random() < p:
#             mutated_chromosome[i] = 15 - mutated_chromosome[i]
#     return mutated_chromosome

def genetic_algorithm(population_size, num_generations):
    population = [[9, 11, 13, 15] for _ in range(population_size)]
    # population = [[13, 24, 8, 19] for _ in range(population_size)]
    for generation in range(num_generations):
        fitnesses = [fitness(chromosome) for chromosome in population]
        new_population = []
        for _ in range(population_size):
            parent1 = tournament_selection(population, 3)
            parent2 = tournament_selection(population, 3)
            print(parent1,parent2)
            child1, child2 = single_point_crossover(parent1, parent2)
            # child1 = bit_flip_mutation(child1, 0.01)
            # child2 = bit_flip_mutation(child2, 0.01)
            new_population.extend([child1, child2])
        population = new_population
    best_chromosome = max(population, key=fitness)
    return fitness(best_chromosome)

print(genetic_algorithm(4, 1))