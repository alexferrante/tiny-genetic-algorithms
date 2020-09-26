import numpy as np

LATTICE_LENGTH = 7
N_EPOCHS = 100
N_AGENTS_PER_EPOCH = 100
N_TIME_STEPS = 24

STATE_DICT = {
    np.array([0,0,0,0,0,0,0]).tobytes(): 0,
    np.array([0,0,0,0,0,0,1]).tobytes(): 1,
    np.array([0,0,0,0,0,1,0]).tobytes(): 2,
    np.array([0,0,0,0,0,1,1]).tobytes(): 3,
    np.array([0,0,0,0,1,0,0]).tobytes(): 4,
    np.array([0,0,0,0,1,0,1]).tobytes(): 5,
    np.array([0,0,0,0,1,1,0]).tobytes(): 6,
    np.array([0,0,0,0,1,1,1]).tobytes(): 7,
    np.array([0,0,0,1,0,0,0]).tobytes(): 8,
    np.array([0,0,0,1,0,0,1]).tobytes(): 9,
    np.array([0,0,0,1,0,1,0]).tobytes(): 10,
    np.array([0,0,0,1,0,1,1]).tobytes(): 11,
    np.array([0,0,0,1,1,0,0]).tobytes(): 12,
    np.array([0,0,0,1,1,0,1]).tobytes(): 13,
    np.array([0,0,0,1,1,1,0]).tobytes(): 14,
    np.array([0,0,0,1,1,1,1]).tobytes(): 15,
    np.array([0,0,1,0,0,0,0]).tobytes(): 16,
    np.array([0,0,1,0,0,0,1]).tobytes(): 17,
    np.array([0,0,1,0,0,1,0]).tobytes(): 18,
    np.array([0,0,1,0,0,1,1]).tobytes(): 19,
    np.array([0,0,1,0,1,0,0]).tobytes(): 20,
    np.array([0,0,1,0,1,0,1]).tobytes(): 21,
    np.array([0,0,1,0,1,1,0]).tobytes(): 22,
    np.array([0,0,1,0,1,1,1]).tobytes(): 23,
    np.array([0,0,1,1,0,0,0]).tobytes(): 24,
    np.array([0,0,1,1,0,0,1]).tobytes(): 25,
    np.array([0,0,1,1,0,1,0]).tobytes(): 26,
    np.array([0,0,1,1,0,1,1]).tobytes(): 27,
    np.array([0,0,1,1,1,0,0]).tobytes(): 28,
    np.array([0,0,1,1,1,0,1]).tobytes(): 29,
    np.array([0,0,1,1,1,1,0]).tobytes(): 30,
    np.array([0,0,1,1,1,1,1]).tobytes(): 31,
    np.array([0,1,0,0,0,0,0]).tobytes(): 32,
    np.array([0,1,0,0,0,0,1]).tobytes(): 33,
    np.array([0,1,0,0,0,1,0]).tobytes(): 34,
    np.array([0,1,0,0,0,1,1]).tobytes(): 35,
    np.array([0,1,0,0,1,0,0]).tobytes(): 36,
    np.array([0,1,0,0,1,0,1]).tobytes(): 37,
    np.array([0,1,0,0,1,1,0]).tobytes(): 38,
    np.array([0,1,0,0,1,1,1]).tobytes(): 39,
    np.array([0,1,0,1,0,0,0]).tobytes(): 40,
    np.array([0,1,0,1,0,0,1]).tobytes(): 41,
    np.array([0,1,0,1,0,1,0]).tobytes(): 42,
    np.array([0,1,0,1,0,1,1]).tobytes(): 43,
    np.array([0,1,0,1,1,0,0]).tobytes(): 44,
    np.array([0,1,0,1,1,0,1]).tobytes(): 45,
    np.array([0,1,0,1,1,1,0]).tobytes(): 46,
    np.array([0,1,0,1,1,1,1]).tobytes(): 47,
    np.array([0,1,1,0,0,0,0]).tobytes(): 48,
    np.array([0,1,1,0,0,0,1]).tobytes(): 49,
    np.array([0,1,1,0,0,1,0]).tobytes(): 50,
    np.array([0,1,1,0,0,1,1]).tobytes(): 51,
    np.array([0,1,1,0,1,0,0]).tobytes(): 52,
    np.array([0,1,1,0,1,0,1]).tobytes(): 53,
    np.array([0,1,1,0,1,1,0]).tobytes(): 54,
    np.array([0,1,1,0,1,1,1]).tobytes(): 55,
    np.array([0,1,1,1,0,0,0]).tobytes(): 56,
    np.array([0,1,1,1,0,0,1]).tobytes(): 57,
    np.array([0,1,1,1,0,1,0]).tobytes(): 58,
    np.array([0,1,1,1,0,1,1]).tobytes(): 59,
    np.array([0,1,1,1,1,0,0]).tobytes(): 60,
    np.array([0,1,1,1,1,0,1]).tobytes(): 61,
    np.array([0,1,1,1,1,1,0]).tobytes(): 62,
    np.array([0,1,1,1,1,1,1]).tobytes(): 63,
    np.array([1,0,0,0,0,0,0]).tobytes(): 64,
    np.array([1,0,0,0,0,0,1]).tobytes(): 65,
    np.array([1,0,0,0,0,1,0]).tobytes(): 66,
    np.array([1,0,0,0,0,1,1]).tobytes(): 67,
    np.array([1,0,0,0,1,0,0]).tobytes(): 68,
    np.array([1,0,0,0,1,0,1]).tobytes(): 69,
    np.array([1,0,0,0,1,1,0]).tobytes(): 70,
    np.array([1,0,0,0,1,1,1]).tobytes(): 71,
    np.array([1,0,0,1,0,0,0]).tobytes(): 72,
    np.array([1,0,0,1,0,0,1]).tobytes(): 73,
    np.array([1,0,0,1,0,1,0]).tobytes(): 74,
    np.array([1,0,0,1,0,1,1]).tobytes(): 75,
    np.array([1,0,0,1,1,0,0]).tobytes(): 76,
    np.array([1,0,0,1,1,0,1]).tobytes(): 77,
    np.array([1,0,0,1,1,1,0]).tobytes(): 78,
    np.array([1,0,0,1,1,1,1]).tobytes(): 79,
    np.array([1,0,1,0,0,0,0]).tobytes(): 80,
    np.array([1,0,1,0,0,0,1]).tobytes(): 81,
    np.array([1,0,1,0,0,1,0]).tobytes(): 82,
    np.array([1,0,1,0,0,1,1]).tobytes(): 83,
    np.array([1,0,1,0,1,0,0]).tobytes(): 84,
    np.array([1,0,1,0,1,0,1]).tobytes(): 85,
    np.array([1,0,1,0,1,1,0]).tobytes(): 86,
    np.array([1,0,1,0,1,1,1]).tobytes(): 87,
    np.array([1,0,1,1,0,0,0]).tobytes(): 88,
    np.array([1,0,1,1,0,0,1]).tobytes(): 89,
    np.array([1,0,1,1,0,1,0]).tobytes(): 90,
    np.array([1,0,1,1,0,1,1]).tobytes(): 91,
    np.array([1,0,1,1,1,0,0]).tobytes(): 92,
    np.array([1,0,1,1,1,0,1]).tobytes(): 93,
    np.array([1,0,1,1,1,1,0]).tobytes(): 94,
    np.array([1,0,1,1,1,1,1]).tobytes(): 95,
    np.array([1,1,0,0,0,0,0]).tobytes(): 96,
    np.array([1,1,0,0,0,0,1]).tobytes(): 97,
    np.array([1,1,0,0,0,1,0]).tobytes(): 98,
    np.array([1,1,0,0,0,1,1]).tobytes(): 99,
    np.array([1,1,0,0,1,0,0]).tobytes(): 100,
    np.array([1,1,0,0,1,0,1]).tobytes(): 101,
    np.array([1,1,0,0,1,1,0]).tobytes(): 102,
    np.array([1,1,0,0,1,1,1]).tobytes(): 103,
    np.array([1,1,0,1,0,0,0]).tobytes(): 104,
    np.array([1,1,0,1,0,0,1]).tobytes(): 105,
    np.array([1,1,0,1,0,1,0]).tobytes(): 106,
    np.array([1,1,0,1,0,1,1]).tobytes(): 107,
    np.array([1,1,0,1,1,0,0]).tobytes(): 108,
    np.array([1,1,0,1,1,0,1]).tobytes(): 109,
    np.array([1,1,0,1,1,1,0]).tobytes(): 110,
    np.array([1,1,0,1,1,1,1]).tobytes(): 111,
    np.array([1,1,1,0,0,0,0]).tobytes(): 112,
    np.array([1,1,1,0,0,0,1]).tobytes(): 113,
    np.array([1,1,1,0,0,1,0]).tobytes(): 114,
    np.array([1,1,1,0,0,1,1]).tobytes(): 115,
    np.array([1,1,1,0,1,0,0]).tobytes(): 116,
    np.array([1,1,1,0,1,0,1]).tobytes(): 117,
    np.array([1,1,1,0,1,1,0]).tobytes(): 118,
    np.array([1,1,1,0,1,1,1]).tobytes(): 119,
    np.array([1,1,1,1,0,0,0]).tobytes(): 120,
    np.array([1,1,1,1,0,0,1]).tobytes(): 121,
    np.array([1,1,1,1,0,1,0]).tobytes(): 122,
    np.array([1,1,1,1,0,1,1]).tobytes(): 123,
    np.array([1,1,1,1,1,0,0]).tobytes(): 124,
    np.array([1,1,1,1,1,0,1]).tobytes(): 125,
    np.array([1,1,1,1,1,1,0]).tobytes(): 126,
    np.array([1,1,1,1,1,1,1]).tobytes(): 127,
}

def get_correct_end_state(init_state):
    state_val = np.sum(init_state)
    correct_end_state = False
    if state_val > 3:
        correct_end_state = True
    return correct_end_state

def apply_agent_rule(state, agent_idx, population):
    agent_str = population[agent_idx]
    try:
        rule_idx = STATE_DICT[state.tobytes()]
    except:
        raise Exception(f"Invalid lattice state {state}")
    rule_value = agent_idx[rule_idx]
    state[agent_idx] = rule_value
    return state

def get_score(init_state, population):
    state = init_state
    correct_end_state = get_correct_end_state(init_state)
    for i in range(0, N_TIME_STEPS):
        for agent in range(0, LATTICE_LENGTH):
            state = apply_agent_rule(state, agent_str)

