# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 11:35:59 2023

@author: SYED ZAHEER HOSSAIN
"""

import random

# Define the number of genes (crews)
num_genes = 5

# Define the number of airplanes
num_airplanes = 3

# Define the number of days
num_days = 7

# Define the population size
population_size = 100

# Define the maximum number of generations
max_generations = 1000

# Define the mutation probability
mutation_probability = 0.1

# Define the fitness function
def fitness_function(chromosome):
    # print(chromosome)
    # Check if each airplane is assigned only one crew
    for i in range(num_airplanes):
        if len(set(chromosome[i*num_genes:(i+1)*num_genes])) != 1:
            return 0
    
    # Check if each crew works for at most two days
    for i in range(num_genes):
        if chromosome.count(i) > 2*num_days:
            return 0
    
    # Check if all airplanes are used every day
    for i in range(num_days):
        if set(chromosome[i*num_airplanes:(i+1)*num_airplanes]) != set(range(num_airplanes)):
            return 0
    
    return 1

# Define the selection operator
def selection_operator(population, fitness_values):
    # Select two parents using tournament selection
    parent1 = population[fitness_values.index(max(fitness_values))]
    parent2 = population[fitness_values.index(max(random.sample(fitness_values, 2)))]

    return parent1, parent2

# Define the crossover operator
def crossover_operator(parent1, parent2):
    # Perform one-point crossover
    crossover_point = random.randint(1, num_genes*num_airplanes-1)
    child1 = parent1[:crossover_point] + parent2[crossover_point:]
    child2 = parent2[:crossover_point] + parent1[crossover_point:]

    return child1, child2

# Define the mutation operator
def mutation_operator(chromosome):
    # Mutate a random gene with a random value
    mutated_gene = random.randint(0, num_genes*num_airplanes-1)
    mutated_value = random.randint(0, num_genes-1)
    chromosome[mutated_gene] = mutated_value

    return chromosome

# Define the main function
def main():
    # Initialize the population
    population = [[random.randint(0, num_genes-1) for _ in range(num_genes*num_airplanes)] for _ in range(population_size)]
    # print(population)

    # Iterate over the generations
    for generation in range(max_generations):
        # Evaluate the fitness of each chromosome
        fitness_values = [fitness_function(chromosome) for chromosome in population]

        # Select the parents
        parents = [selection_operator(population, fitness_values) for _ in range(population_size//2)]

        # Perform crossover
        offspring = [crossover_operator(parent1, parent2) for parent1, parent2 in parents]
        
        # print(offspring)
        # print(parents)

        # Flatten the offspring list
        offspring = [gene for chromosome in offspring for gene in chromosome]
        # print(offspring)

        # Perform mutation
        for i in range(len(offspring)):
            if random.random() < mutation_probability:
                offspring[i] = mutation_operator(offspring[i])

        # Replace the worst chromosomes with the offspring
        fitness_values = [fitness_function(chromosome) for chromosome in population]
        worst_indices = sorted(range(len(fitness_values)), key=lambda k: fitness_values[k])[:len(offspring)]
        # print(population)
        for i, offspring_chromosome in enumerate(offspring):
            population[worst_indices[i]] = offspring_chromosome

    # Print the best chromosome
    fitness_values = [fitness_function(chromosome) for chromosome in population]
    best_chromosome = population[fitness_values.index(max(fitness_values))]
    print(best_chromosome)

if __name__ == '__main__':
    main()