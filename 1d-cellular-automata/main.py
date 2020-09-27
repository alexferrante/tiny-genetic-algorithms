import math
import numpy as np

from random import randint
from .models import N_EPOCHS, N_AGENTS_PER_EPOCH, LATTICE_LENGTH, N_TIME_STEPS, N_FITNESS_TRIALS, get_score, get_random_agent_encoding

def init_agent_rules():
    list_of_agents = []
    for i in range(N_AGENTS_PER_EPOCH):
        agent_str = get_random_agent_encoding()
        list_of_agents.append(agent_str)
    return list_of_agents

def get_random_init_state():
    init_lattice = np.empty(LATTICE_LENGTH)
    for x in range(LATTICE_LENGTH):
        state_xi = randint(0,1)
        init_lattice = np.append(init_lattice, state_xi)
    return init_lattice

def compute_fitness(population, target_cell_idx):
    fitness_score = 0
    for i in range(N_FITNESS_TRIALS): # Number of random configurations to evaluate agent fitness on
        init_state = get_random_init_state()
        score = get_score(init_state, population, target_cell_idx)
        fitness_score += score
    return fitness_score / N_FITNESS_TRIALS

def run_evolution():
    population = init_agent_rules()
    for i in range(N_EPOCHS): # Rounds of evolution
        fitness_store_i = []
        for agent_rule_idx in range(len(population)): # Compute fitness of each agent in the population
            rule_j_fitness = compute_fitness(population, agent_rule_idx)
            fitness_store_i.append(rule_j_fitness)
        evolve_population(population, fitness_store_i) # Update the population

def evolve_population(agent_str_list, fitness_list):
    for i in range(len(agent_str_list)):
        new_population = []
        chosen_parents = np.random.choice(agent_str_list, size=2, replace=False, p=fitness_list) # Probabilistic choice of parents
        

# My initial thoughts: didn't consider that the lattice was 7 individual cells, didn't consider prospect of quantifying interactions
# Later evolved thought: need to consider every cell at every update. I assume that each cell is a member of the population and each cell is thus an initially randomly generated, independent entity, with its own rules
# Above thought => problem with sequence of updating state, problem with quantifying the fitness of each cell => its not obvious how one can determine the contribution of cell i's rule to the overall fitness (which is presumably an average of all n cells) versus cell i+1's rule
# Final evolved thought: Every cell has the same rule. Duh!
# Next thought: every cell does not have the same rule. Otherwise, evolution would not do anything.
# => the question: how do I evaluate fitness 
# I'm getting the sense that I need to keep in mind the other cell rules while moving forward in the time steps.
# I'm confused because it seems like I'm ignoring the contributuons of the other rules to the success of the system.

def main():
    run_evolution()

if __name__ == "__main__":
    main()