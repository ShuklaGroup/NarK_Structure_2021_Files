"""
       	Run as:
       	<codename> <ITERATION NUMBER> <PATH TO set_2 file without score> <input file>
"""

import random
import time
import sys
from geneticAlgoFunc import *


#populationSize=5
#percentMutation=50
#percentCrossover=1

if __name__ == "__main__":
       	ITERATION=int(sys.argv[1])
       	set2_file=sys.argv[2]
       	prev_population_file='iter_'+str(ITERATION-1)+'_output_sets.txt'
       	output_sets_file = 'iter_'+str(ITERATION)+'_input_sets.txt'

       	random.seed(time)

       	## Reading input file
       	f_log=open("generateSets.log","wb")
        if len(sys.argv)==4:
       		input_file = sys.argv[3]
                f=open(input_file,'rb')
                for line in f:
                        exec line
                f.close()
        else:
                print "This script needs exactly "+str(len(sys.argv)-1)+" arguments, aborting"
                f_log.write("This script needs exactly "+str(len(sys.argv)-1)+" arguments, aborting\n")
                sys.exit()

       	nMutation = percentMutation*populationSize/100
       	nCrossover = percentCrossover*populationSize/100

       	## Read the compatible size 2 sets file: set_2.txt
       	fitness_set_2=[]
       	set_2=[]
       	f=open(set2_file,'rb')
       	for line in f:
       		columns=line.strip().split('\t')
       		set_2.append([int(item) for item in columns[:]])
       	f.close()

       	## Population
       	## For the first iteration, the population is all the sets of size 2
       	if (ITERATION==1):
       		population_old=set_2[:]
       		fitness_old=[1]*len(population_old)
       		scaled_fitness_old=[1]*len(population_old)
       	else:
       		population_old=[]
       		fitness_old=[]
       		scaled_fitness_old=[]
       		f=open(prev_population_file,'rb')
       		for line in f:
       			columns=line.strip().split('\t')
       			if len(columns)==5:
       				population_old.append([int(item) for item in columns[3:]])
       				fitness_old.append(float(columns[2]))
       				scaled_fitness_old.append(float(columns[2]))
       			else:
       				temp_set=[]
       				n=(len(columns)-3)/2   	## Number of sets, you can scale the fitness using this number
       				count=3		## keep track of column number
       				for i in range(n):
       					temp=[]
       					temp.append(int(columns[count]))
       					temp.append(int(columns[count+1]))
       					temp_set.append(temp)
       					count +=2
       				population_old.append(temp_set)
       				scaled_fitness = ((100-n+1-5) * float(columns[2]))/100
       				fitness_old.append(float(columns[2]))  	## Scaled fitness
       				scaled_fitness_old.append(scaled_fitness)
       		f.close()

       	## Natural Selection
       	## Select populationSize from the above population using roulette wheel on the scaled fitness scores
       	population=weighted_random_choice(population_old[:],scaled_fitness_old[:],populationSize)

       	## Choose which sets to mutate
       	mutation_sets = random.sample(population,nMutation)
       	mutations = mutation(population[:],mutation_sets[:],set_2[:],populationSize)

       	## Update population after mutation
       	for i in range(len(mutations)):
       		population[population.index(mutation_sets[i])] = mutations[i]

       	## Uptil now the population size remains populationSize
       	## Next it will change during crossovers

       	## Crossover
       	population = crossover(population[:],nCrossover)

       	f=open(output_sets_file,'wb')
       	for i in range(len(population)):
       		if isinstance(population[i][0],list):
       			for j in range(len(population[i])):
       				for k in range(len(population[i][j])):
       					f.write(str(population[i][j][k])+'\t')
       			f.write('\n')
       		else:
       			for j in range(len(population[i])):
       				f.write(str(population[i][j])+'\t')
       			f.write('\n')
       	f.close()
       	f_log.close()
