import random

def weighted_random_choice(population,fitness,populationSize):
       	new_population=[]
       	for j in range(populationSize):
       		max = sum(fitness)
       		pick = random.uniform(0, max)
       		current = 0
       		for i in range(len(fitness)):
       			current += fitness[i]
       			if current > pick:
       				new_population.append(population[i])
       				break;
       		population.pop(i)
       		fitness.pop(i)
       	return new_population

def mutation(population,mutation_sets,set_2,populationSize):
       	possible_mutations=set_2[:]
       	for i in range(populationSize):
       		if isinstance(population[i][0], list):
       			for j in range(len(population[i])):
       				if population[i][j] in possible_mutations:
       					possible_mutations.pop(possible_mutations.index(population[i][j]))
       		else:
       			if population[i] in possible_mutations:
       				possible_mutations.pop(possible_mutations.index(population[i]))

       	after_mutation=[]
       	for i in range(len(mutation_sets)):
       		pick = random.randrange(0,len(possible_mutations))
       		mutate_to = possible_mutations[pick]
       		possible_mutations.pop(pick)
       		if isinstance(mutation_sets[i][0], list):
       			temp = mutation_sets[i][:]
       			item_to_mutate = random.randrange(0,len(temp))
       			temp.pop(item_to_mutate)
       			temp.append(mutate_to)
       			after_mutation.append(temp)
       		else:
       			after_mutation.append(mutate_to)
       	return after_mutation

def crossover(population,nCrossover):
       	possible_crossover=population[:]
       	crossover_of_sets = random.sample(population,nCrossover)
       	for i in range(len(crossover_of_sets)):
       		possible_crossover.pop(possible_crossover.index(crossover_of_sets[i]))
       	crossover_with_sets = random.sample(possible_crossover,nCrossover)

       	for i in range(nCrossover):
       		if isinstance(crossover_of_sets[i][0],list) and isinstance(crossover_with_sets[i][0],list):
       			population.append(crossover_of_sets[i]+crossover_with_sets[i])
       		elif isinstance(crossover_of_sets[i][0],list) and not isinstance(crossover_with_sets[i][0],list):
       			population.append(crossover_of_sets[i]+[crossover_with_sets[i]])
       		elif not isinstance(crossover_of_sets[i][0],list) and isinstance(crossover_with_sets[i][0],list):
       			population.append([crossover_of_sets[i]]+crossover_with_sets[i])
       		if not isinstance(crossover_of_sets[i][0],list) and not isinstance(crossover_with_sets[i][0],list):
       			population.append([crossover_of_sets[i]]+[crossover_with_sets[i]])

       	return population
