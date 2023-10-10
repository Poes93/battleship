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


if __name__ == "__main__":
    game = battleshipgame()
    game.play()
