import math
import numpy as np

from random import randint
from .models import N_EPOCHS, N_AGENTS_PER_EPOCH, LATTICE_LENGTH, N_TIME_STEPS, get_score

def init_agents():
    list_of_agents = []
    for i in range(N_AGENTS_PER_EPOCH):
        agent_str_list = []
        agent_str = get_random_agent_encoding()
        list_of_agents.append(agent_str)
    return list_of_agents

def get_random_agent_encoding():
    encoding_size = math.pow(2, LATTICE_LENGTH)
    agent_str_list = []
    for i in range(encoding_size):
        agent_str_list.append(randint(0, 1))
    agent_str = "".join([str(e) for e in agent_str_list])
    return agent_str

def get_random_init_state():
    init_lattice = np.empty(LATTICE_LENGTH)
    for x in range(LATTICE_LENGTH):
        state_xi = randint(0,1)
        init_lattice.append(state_xi)
    return init_lattice

def compute_fitness(agent_str):
    fitness_score = 0
    for i in range(N_FITNESS_TRIALS):
        init_state = get_random_init_state()
        score = get_score(init_state, agent_str)
        fitness_score += score
    return fitness_score / N_FITNESS_TRIALS

def evolve_population(agent_str_list, fitness_list):
    for i in range(len(agent_str_list)):
        # choose, probabilistically, from fitness list


def run_evolution():
    population = init_agents()
    for i in range(N_EPOCHS):
        fitness_store_i = []
        for agent_idx in range(len(population)):
            agent_j = population[agent_idx]
            fitness_j = compute_fitness(agent_j)
            fitness_store_i.append(fitness_j)
        evolve_population(population, fitness_store_i)





def main():

if __name__ == "__main__":
    main()