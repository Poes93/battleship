import random


class battleshipgame:
    def __init__(self):
        # initialize the game parameters with grid size and number of ships
        self.grid_size = 10
        self.num_of_ships = 5

        # fill the board with 0's
        self.player_board = [['0'] * self.grid_size for i in range(self.grid_size)]
        self.computer_board = [['0'] * self.grid_size for i in range(self.grid_size)]

        # place the ships on the board
        self.place_ships(self.player_board)
        self.place_ships(self.computer_board)


    def print_board(self):
        # print the board
        # starting the game and printing the board
        print("Let's play Battleship!")
        print("Player Board:")
        for row in self.player_board:
            print(" ".join(row))

        print("Computer Board:")
        for row in self.computer_board:
            print(" ".join(row))


    def place_ships(self, board):
        # place the ships on the board
        for i in range(self.num_of_ships):
            # generate a random row and column
            row = random.randint(0, self.grid_size - 1)
            col = random.randint(0, self.grid_size - 1)

            # check if the position is already occupied
            while board[row][col] == 'X':
                row = random.randint(0, self.grid_size - 1)
                col = random.randint(0, self.grid_size - 1)

            # place the ship
            board[row][col] = 'X'


    def player_guess(self, row, col):
        # Check if the player has already guessed this spot
        if self.computer_board[row][col] in ['H', 'M']:
            print("You already guessed that spot.")
            return False


        # Process the player's guess
        if self.computer_board[row][col] == 'X':
            print("Hit!")
            self.computer_board[row][col] = 'H'
        else:
            print("Miss!")
            self.computer_board[row][col] = 'M'


    def computer_guess(self):
        # Process the computer's guess
        while True:
            row = random.randint(0, self.grid_size - 1)
            col = random.randint(0, self.grid_size - 1)
            # Checks so the computer wont check the same spot twice
            if self.player_board[row][col] not in ['H', 'M']:
                break
        if self.player_board[row][col] == 'X':
            print(f"Computer has hit your ship at ({row}, {col})")
            self.player_board[row][col] = 'H'
        else:
            print(f"Computer has missed your ship at ({row}, {col})")
            self.player_board[row][col] = 'M'


def play(self):
    # Game loop, player and computer take turns guessing
    while True:
        self.print_board()
        guess_row = int(input(f"Guess a row (0-{self.grid_size - 1}): "))
        guess_col = int(input(f"Guess a column (0-{self.grid_size - 1}): "))
        
        # To warn if the player guesses outside the grid
        if guess_row < 0 or guess_row >= self.grid_size or guess_col < 0 or guess_col >= self.grid_size:
            print("That's outside the grid")
            continue

        self.player_guess(guess_row, guess_col)

        # Check if the player has won
        if not any('X' in row for row in self.computer_board):
            print("You sank the computers ships!")
            break


        # Conputer's turn
        print("\nComputer's Turn")
        self.computer_guess()

        # Check if the computer has won
        if not any('X' in row for row in self.player_board):
            print("The computer has sunken all your ships!")
            break


if __name__ == "__main__":
    game = battleshipgame(size, num_of_ships)
    game.play()
