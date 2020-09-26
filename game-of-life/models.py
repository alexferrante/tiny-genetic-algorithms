import pandas as pd

POSSIBLE_STATE_DICT = {
    0: "Off",
    1: "On",
    "Off": 0,
    "On": 1
}

def get_possible_state(state_id):
    try:
        return POSSIBLE_STATE_DICT[state_id]
    except KeyError:
        raise Exception(f"Invalid state id {state_id}")

def is_birth(board, x_pos, y_pos):
    state_list = pd.Series()
    if get_board_pos_state(board, x_pos, y_pos + 1):
        state_list[0] = 1
    if get_board_pos_state(board, x_pos + 1, y_pos):
        state_list[1] = 1
    if get_board_pos_state(board, x_pos, y_pos - 1):
        state_list[1] = 1
    if get_board_pos_state(board, x_pos - 1, y_pos):
        state_list[3] = 1
    
        


def get_board_pos_state(board, x_pos, y_pos):
    if x_pos == 1 or 