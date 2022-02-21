import copy
import sys

dim_err = "Invalid dimensions!"
start_err = 'Invalid position!'
move_err = "Invalid move! "

while True:
    try:
        dimensions = [int(x) for x in input("Enter your board dimensions: ").split()]
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
        start_pos = [int(x) for x in input("Enter the knight's starting position: ").split()]
    except ValueError:
        print(start_err)
        continue
    else:
        if len(start_pos) != 2 or (not 1 <= start_pos[0] <= dimensions[0] or not 1 <= start_pos[1] <= dimensions[1]):
            print(start_err)
            continue

    break

turns = 0

visited = [start_pos]

cell_size = len(str(dimensions[0] * dimensions[1]))

grid = [[cell_size * '_' for x in range(dimensions[0])] for y in range(dimensions[1])]

while True:

    attempt = input("Do you want to try the puzzle? (y/n): ").lower()

    if attempt not in ('y', 'n'):
        print("Invalid input!")
        continue

    break

while True:

    turns += 1

    grid[start_pos[1] - 1][start_pos[0] - 1] = f"{(cell_size - 1) * ' '}X"

    possible_moves = [

        [start_pos[0] + 1, start_pos[1] + 2],
        [start_pos[0] + 2, start_pos[1] + 1],
        [start_pos[0] + 2, start_pos[1] - 1],
        [start_pos[0] + 1, start_pos[1] - 2],
        [start_pos[0] - 1, start_pos[1] - 2],
        [start_pos[0] - 2, start_pos[1] - 1],
        [start_pos[0] - 2, start_pos[1] + 1],
        [start_pos[0] - 1, start_pos[1] + 2],

    ]


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


    def get_possible_moves(board, start):

        moves = [

            [start[0] + 1, start[1] + 2],
            [start[0] + 2, start[1] + 1],
            [start[0] + 2, start[1] - 1],
            [start[0] + 1, start[1] - 2],
            [start[0] - 1, start[1] - 2],
            [start[0] - 2, start[1] - 1],
            [start[0] - 2, start[1] + 1],
            [start[0] - 1, start[1] + 2],

        ]

        pos_moves = 0

        for possible in moves:
            try:
                if (possible[1] - 1 >= 0 and possible[0] - 1 >= 0) \
                        and 'X' not in grid[possible[1] - 1][possible[0] - 1] \
                        and '*' not in grid[possible[1] - 1][possible[0] - 1]:

                    board[possible[1] - 1][possible[0] - 1] = cell_size * '_'
                    pos_moves += 1

            except IndexError:
                continue

        return ''.join(((cell_size - 1) * ' ', str(pos_moves)))

    grid_cop = copy.deepcopy(grid)

    for move in possible_moves:
        try:
            if (move[1] - 1 >= 0 and move[0] - 1 >= 0) and '*' not in grid[move[1] - 1][move[0] - 1]:
                grid_cop[move[1] - 1][move[0] - 1] = get_possible_moves(grid_cop, move)
        except IndexError:
            continue

    print_grid(dimensions, grid_cop)

    grid[start_pos[1] - 1][start_pos[0] - 1] = f"{(cell_size - 1) * ' '}*"

    print()

    grid_flatten = ''.join(elem for grid in grid_cop for elem in grid)

    if '_' not in grid_flatten:
        print("\nWhat a great tour! Congratulations!")
        sys.exit()
    elif not any(x.isdigit() for x in grid_flatten):
        print("\nNo more possible moves!")
        print(f"Your knight visited {turns} squares!")
        sys.exit()

    if attempt == 'y':

        while True:

            try:
                start_pos = [int(x) for x in input("Enter your next move: ").split()]

                if start_pos not in possible_moves:
                    print(move_err, end='')
                    continue

            except IndexError:
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
