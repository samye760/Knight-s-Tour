import copy
import sys
from typing import List

dim_err: str = "Invalid dimensions!"
start_err: str = 'Invalid position!'
move_err: str = "Invalid move! "

while True:
    try:
        dimensions: List[int] = [int(x) for x in input("Enter your board dimensions: ").split()]
    except ValueError:
        print(dim_err)
        continue
    else:
        if len(dimensions) != 2 or not all(x > 0 for x in dimensions):
            print(dim_err)
            continue

    break

while True:
    try:
        start_pos: List[int] = [int(x) for x in input("Enter the knight's starting position: ").split()]
    except ValueError:
        print(start_err)
        continue
    else:
        if len(start_pos) != 2 or (not 1 <= start_pos[0] <= dimensions[0] or not 1 <= start_pos[1] <= dimensions[1]):
            print(start_err)
            continue

    break

turns: int = 0

visited: List[list] = [start_pos]

cell_size: int = len(str(dimensions[0] * dimensions[1]))

grid: List[list] = [[cell_size * '_' for _ in range(dimensions[0])] for _ in range(dimensions[1])]


def print_grid(dims, board):

    if dims[0] * dims[1] < 100:
        lines = ''.join((' ', '-' * (dims[0] * 3 + 3)))
        print(lines)
        for idx in range(dims[1], 0, -1):
            print(f"{idx}| {' '.join(board[idx - 1])} |")
        print(lines)
        print(f"    {'  '.join(str(x) for x in range(1, dims[0] + 1))}")

    else:
        lines = ''.join(('  ', '-' * (dims[0] * (cell_size + 1) + 3)))
        print(lines)
        for idx in range(dims[1], 0, -1):
            print(f"{str(idx).rjust(2)}| {' '.join(board[idx - 1])} |")
        print(lines)
        print(f"      {'   '.join(str(x) for x in range(1, dims[0] + 1))}")


def get_possible_moves(board: List[list], start: List[int]) -> str:

    board_copy: List[list] = copy.deepcopy(board)

    moves: List[list] = [

        [start[0] + 1, start[1] + 2],
        [start[0] + 2, start[1] + 1],
        [start[0] + 2, start[1] - 1],
        [start[0] + 1, start[1] - 2],
        [start[0] - 1, start[1] - 2],
        [start[0] - 2, start[1] - 1],
        [start[0] - 2, start[1] + 1],
        [start[0] - 1, start[1] + 2],

    ]

    pos_moves: int = 0

    for possible in moves:
        try:
            if (possible[1] - 1 >= 0 and possible[0] - 1 >= 0) \
                    and 'X' not in grid[possible[1] - 1][possible[0] - 1] \
                    and '*' not in grid[possible[1] - 1][possible[0] - 1]:

                board_copy[possible[1] - 1][possible[0] - 1] = cell_size * '_'
                pos_moves += 1

        except IndexError:
            continue

    return f"{(cell_size - 1) * ' '}{str(pos_moves)}"


def solver(board: List[list], start: List[int], count: int = 1):

    board[start[1] - 1][start[0] - 1] = str(count).rjust(2)

    board_flatten: str = ''.join(elem for lst in board for elem in lst)

    if '_' not in board_flatten:
        return True

    moves: List[tuple] = [

        (start[0] + 1, start[1] + 2),
        (start[0] + 2, start[1] + 1),
        (start[0] + 2, start[1] - 1),
        (start[0] + 1, start[1] - 2),
        (start[0] - 1, start[1] - 2),
        (start[0] - 2, start[1] - 1),
        (start[0] - 2, start[1] + 1),
        (start[0] - 1, start[1] + 2),

    ]

    move_list: dict = {}

    for pos in moves:
        try:
            if (pos[1] - 1 >= 0 and pos[0] - 1 >= 0) and '_' in board[pos[1] - 1][pos[0] - 1]:
                move_list[pos] = int(get_possible_moves(board, start).strip())
        except IndexError:
            continue

    start: List[tuple] = sorted(move_list, key=lambda x: move_list[x], reverse=True)

    if not move_list:
        return False

    for lst in start:
        if solver(board, lst, count + 1):
            return True

        board[lst[1] - 1][lst[0] - 1] = cell_size * '_'

    return False


while True:

    attempt: str = input("Do you want to try the puzzle? (y/n): ").lower()

    if attempt not in ('y', 'n'):
        print("Invalid input!")
        continue

    break


if attempt == 'n':
    if solver(grid, start_pos):
        print("\nHere's the solution!")
        print_grid(dimensions, grid)
    else:
        print("No solution exists!")

    sys.exit()

rec_copy = copy.deepcopy(grid)

if not solver(rec_copy, start_pos):
    print("No solution exists!")
    sys.exit()

while True:

    turns += 1

    grid[start_pos[1] - 1][start_pos[0] - 1] = f"{(cell_size - 1) * ' '}X"

    possible_moves: List[list] = [

        [start_pos[0] + 1, start_pos[1] + 2],
        [start_pos[0] + 2, start_pos[1] + 1],
        [start_pos[0] + 2, start_pos[1] - 1],
        [start_pos[0] + 1, start_pos[1] - 2],
        [start_pos[0] - 1, start_pos[1] - 2],
        [start_pos[0] - 2, start_pos[1] - 1],
        [start_pos[0] - 2, start_pos[1] + 1],
        [start_pos[0] - 1, start_pos[1] + 2],

    ]

    grid_cop: List[list] = copy.deepcopy(grid)

    for move in possible_moves:
        try:
            if (move[1] - 1 >= 0 and move[0] - 1 >= 0) and '*' not in grid[move[1] - 1][move[0] - 1]:
                grid_cop[move[1] - 1][move[0] - 1] = get_possible_moves(grid_cop, move)
        except IndexError:
            continue

    print_grid(dimensions, grid_cop)

    grid[start_pos[1] - 1][start_pos[0] - 1] = f"{(cell_size - 1) * ' '}*"

    print()

    grid_flatten: str = ''.join(elem for grid in grid_cop for elem in grid)

    if '_' not in grid_flatten:
        print("\nWhat a great tour! Congratulations!")
        sys.exit()
    elif not any(x.isdigit() for x in grid_flatten):
        print("\nNo more possible moves!")
        print(f"Your knight visited {turns} squares!")
        sys.exit()

    while True:

        try:
            start_pos: List[int] = [int(x) for x in input("Enter your next move: ").split()]

            if start_pos not in possible_moves:
                print(move_err, end='')
                continue

        except ValueError:
            print(move_err, end='')
            continue
        else:
            if len(start_pos) != 2 \
                    or (not 1 <= start_pos[0] <= dimensions[0] or not 1 <= start_pos[1] <= dimensions[1]) \
                    or start_pos in visited:

                print(move_err, end='')
                continue

        visited.append(start_pos)

        break
