from random import randint
from .models import N_ACTIONS, N_FITNESS_TRIALS, BOARD_X_DIMENSION, BOARD_Y_DIMENSION, get_score

def init_agents(n_agents):
    list_of_agents = []
    for i in range(n_agents):
        agent_str_list = []
        for j in range(N_ACTIONS):
            agent_str_list.append(randint(0, 6))
        agent_str = "".join([str(e) for e in agent_str_list])
        list_of_agents.append(agent_str)
    return list_of_agents

def get_random_board():
    board = []
    for x in range(BOARD_X_DIMENSION):
        row_xi = []
        for y in range(BOARD_Y_DIMENSION):
            random_board_state_yj = randint(0, 1)
            row_xi.append(random_board_state_yj)
        board.append(row_xi)
    return board

def compute_fitness(agent_str):
    fitness_score = 0
    for i in range(N_FITNESS_TRIALS):
        board = get_random_board()
        score = get_score(board, agent_str)
        fitness_score += score
    return fitness_score / N_FITNESS_TRIALS

def evolve_population(agent_str_list, fitness_list):
    for i in range(len(agent_str_list)):
        # choose, probabilistically, from fitness list


def run_evolution(n_epochs):
    n_agents = 100
    population = init_agents(n_agents)
    for i in range(n_epochs):
        fitness_store_i = []
        for agent_idx in range(len(population)):
            agent_j = population[agent_idx]
            fitness_j = compute_fitness(agent_j)
            fitness_store_i.append(fitness_j)
        evolve_population(population, fitness_store_i)





def main():

if __name__ == "__main__":
    main()