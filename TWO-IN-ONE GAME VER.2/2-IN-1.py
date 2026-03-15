import random
import string
def generate_maze(width, height):
    maze = [['#'] * width for _ in range(height)]
    stack = []
    start_x, start_y = 1, 1
    maze[start_y][start_x] = ' '
    stack.append((start_x, start_y))

    directions = [(-2, 0), (2, 0), (0, -2), (0, 2)]

    while stack:
        x, y = stack[-1]
        random.shuffle(directions)
        carved = False
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 1 <= nx < width-1 and 1 <= ny < height-1 and maze[ny][nx] == '#':
                maze[ny][nx] = ' '
                maze[y + dy//2][x + dx//2] = ' '
                stack.append((nx, ny))
                carved = True
                break
        if not carved:
            stack.pop()
    maze[1][1] = 'S'
    maze[height-2][width-2] = 'E'
    return maze

def print_maze(maze, position):
    for y, row in enumerate(maze):
        line = ''
        for x, cell in enumerate(row):
            if (x, y) == position:
                line += 'P'
            else:
                line += cell
        print(line)
    print()

def find_start(maze):
    for y, row in enumerate(maze):
        for x, cell in enumerate(row):
            if cell == 'S':
                return (x, y)
    return (1, 1)

def play_maze_game():
    width, height = 21, 11
    maze = generate_maze(width, height)
    player_pos = find_start(maze)
    moves = {'w': (0, -1), 's': (0, 1), 'a': (-1, 0), 'd': (1, 0)}
    print("Maze Game! Use WASD to move. Reach 'E' to win.")
    while True:
        print_maze(maze, player_pos)
        move = input("Move (WASD): ").lower()
        if move in moves:
            dx, dy = moves[move]
            nx, ny = player_pos[0] + dx, player_pos[1] + dy
            if maze[ny][nx] != '#':
                player_pos = (nx, ny)
            if maze[ny][nx] == 'E':
                print_maze(maze, player_pos)
                print("Congratulations! You reached the end!")
                break
        else:
            print("Invalid move. Use W, A, S, D.")

def create_board(size):
    return [['~'] * size for _ in range(size)]

def print_board(board, hide_ships=False):
    print('  ' + ' '.join(string.ascii_uppercase[:len(board)]))
    for i, row in enumerate(board):
        line = []
        for cell in row:
            if hide_ships and cell == 'S':
                line.append('~')
            else:
                line.append(cell)
        print(f"{i+1:2} " + ' '.join(line))
    print()

def place_ship(board, size):
    while True:
        x = random.randint(0, len(board)-1)
        y = random.randint(0, len(board)-1)
        direction = random.choice(['H', 'V'])
        if direction == 'H':
            if x + size > len(board):
                continue
            if any(board[y][x+i] == 'S' for i in range(size)):
                continue
            for i in range(size):
                board[y][x+i] = 'S'
            break
        else:
            if y + size > len(board):
                continue
            if any(board[y+i][x] == 'S' for i in range(size)):
                continue
            for i in range(size):
                board[y+i][x] = 'S'
            break

def get_move(size):
    while True:
        move = input("Enter move (e.g. A5): ").upper().strip()
        if len(move) < 2:
            print("Invalid input.")
            continue
        col = move[0]
        row = move[1:]
        if col in string.ascii_uppercase[:size] and row.isdigit():
            x = string.ascii_uppercase.index(col)
            y = int(row) - 1
            if 0 <= x < size and 0 <= y < size:
                return x, y
        print("Invalid input.")

def battleship_game():
    size = 6
    ship_sizes = [3, 2]
    player_board = create_board(size)
    computer_board = create_board(size)
    for s in ship_sizes:
        place_ship(player_board, s)
        place_ship(computer_board, s)
    print("Welcome to Battleship!")
    turns = 0
    hits = 0
    total_ship_cells = sum(ship_sizes)
    while hits < total_ship_cells:
        print("Your board:")
        print_board(player_board)
        print("Enemy board:")
        print_board(computer_board, hide_ships=True)
        x, y = get_move(size)
        if computer_board[y][x] == 'S':
            print("Hit!")
            computer_board[y][x] = 'X'
            hits += 1
        elif computer_board[y][x] in ('X', 'O'):
            print("Already tried there.")
        else:
            print("Miss.")
            computer_board[y][x] = 'O'
        turns += 1
    print("You sank all the ships in", turns, "turns!")

def main():
    print("welcome to this 2-in-1 game! You can play either the Maze Game or Battleship Game.")
    print("1. Maze Game")
    print("2. Battleship Game")
    choice = input("Enter your choice (1 or 2): ")
    if choice == "1":
        play_maze_game()
    elif choice == "2":
        battleship_game()
    else:
        print("Invalid choice.")

main()