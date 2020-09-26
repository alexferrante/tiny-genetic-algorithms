ACTION_DICT = {
    0: "MoveUp",
    1: "MoveRight",
    2: "MoveDown",
    3: "MoveLeft",
    4: "MoveRandom",
    5: "PickUp",
    6: "DoNothing"
}

N_ACTIONS = 243

BOARD_STATE_DICT = {
    0: "Empty",
    1: "Can",
    2: "Wall"
}

BOARD_X_DIMENSION = 10
BOARD_Y_DIMENSION = 10

LOCATION_STATE_DICT = {
    "North": 0,
    "East": 1,
    "South": 2,
    "West": 3
}

N_FITNESS_TRIALS = 100

def get_action(action_id):
    try:
        return ACTION_DICT[action_id]
    except KeyError:
        raise Exception(f"Unknown action id {action_id}")

def get_location_state_encoding(direction_id):
    try:
        return LOCATION_STATE_DICT[direction_id]
    except KeyError:
        raise Exception(f"Unknown direction id {direction_id}")

def get_state_encoding(state_id):
    try:
        return BOARD_STATE_DICT[state_id]
    except KeyError:
        raise Exception(f"Unknown state id {state_id}")

def get_board_loc_state(board, x_pos, y_pos):
    loc_state_encoding = [] # NORTH, EAST, SOUTH, WEST, CURRENT
    if x_pos == 0:
        loc_state_encoding[get_location_state_encoding("South")] = get_state_encoding("Wall")
    if y_pos == 0: 
        loc_state_encoding[get_location_state_encoding("West")] = get_state_encoding("Wall")
    if x_pos == (BOARD_X_DIMENSION - 1):
        loc_state_encoding[get_location_state_encoding("East")] = get_state_encoding("Wall")
    if y_pos == (BOARD_Y_DIMENSION - 1):
        loc_state_encoding[get_location_state_encoding("North")] = get_state_encoding("Wall")

    # TO DO: continue

def get_score(board, agent_str):
    #


