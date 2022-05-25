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


def gen_board(src):
    moves = get_moves(src)
    rows = []
    for row in range(BOARD_SIZE):
        output_row = ["▢"] * BOARD_SIZE
        for col in range(BOARD_SIZE):
            current = row * BOARD_SIZE + col
            if src == current:
                output_row[col] = "▲"
            if current in moves:
                output_row[col] = "◉"
        rows.append(output_row)
    return rows


def print_board(board):
    print("\n".join("".join(row) for row in board))


def add_move(q, path, move):
    newpath = path[:]
    newpath.append(move)
    q.append(newpath)


def solution(src, dst):
    if src == dst:
        return [src]
    visited = set()
    q = deque()
    q.append([src])
    while q:
        path = q.popleft()
        current = path[-1]
        visited.add(current)
        moves = get_moves(current)
        if dst in moves:
            path.append(dst)
            return path
        for move in moves:
            if move in visited:
                continue
            add_move(q, path, move)

