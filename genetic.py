import random

def generate_population(size, length):
    return [ [random.randint(0,1) for _ in range(length)] for _ in range(size) ]

def fitness(individual):
    return sum(individual)  

def selection(population):
    return sorted(population, key=fitness, reverse=True)[:2]

def crossover(parent1, parent2):
    point = random.randint(1, len(parent1)-1)
    return parent1[:point] + parent2[point:], parent2[:point] + parent1[point:]

def mutate(individual, mutation_rate=0.01):
    return [bit if random.random() > mutation_rate else 1 - bit for bit in individual]

population_size = 100
bit_length = 20
iterations = 150

population = generate_population(population_size, bit_length)

for generation in range(iterations):
    new_population = []
    for _ in range(population_size // 2):
        p1, p2 = selection(population)
        child1, child2 = crossover(p1, p2)
        new_population += [mutate(child1), mutate(child2)]
    population = new_population

best = max(population, key=fitness)
print("Best Individual (max sum):", best)
print("Fitness:", fitness(best))
