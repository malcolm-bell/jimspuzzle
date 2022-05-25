from itertools import chain

BOARD_SIZE = 8

RC_LEFT_1 = ((2, -1), (-2, -1))
RC_LEFT_2 = ((1, -2), (-1, -2))
RC_RIGHT_1 = ((2, 1), (-2, 1))
RC_RIGHT_2 = ((1, 2), (-1, 2))
RC_ALL_MOVES = list(chain(RC_LEFT_1, RC_LEFT_2, RC_RIGHT_1, RC_RIGHT_2))


def get_moves(src):
    # Using rows and columns to avoid thinking - easy bounds checking this way,
    # Can just test result isn't negative and is less than the board width.
    src_row = src // BOARD_SIZE
    src_col = src % BOARD_SIZE
    allowed_moves = []
    for move in RC_ALL_MOVES:
        row = src_row + move[0]
        col = src_col + move[1]
        if 0 <= row < BOARD_SIZE and 0 <= col < BOARD_SIZE:
            allowed_moves.append(row * BOARD_SIZE + col)
    return allowed_moves
