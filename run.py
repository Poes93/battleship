import random
import sys
from colorama import Fore, init
init(autoreset=True)


class BattleshipGame:
    """
    Whole game class, contains all the game logic
    """
    def __init__(self, grid_size, num_of_ships):
        """
        initialize the game parameters with grid size and number of ships
        """
        self.grid_size = grid_size
        self.num_of_ships = num_of_ships

        if self.num_of_ships > self.grid_size * self.grid_size:
            raise ValueError(
                Fore.RED + "Number of ships can't exceed the grid size"
                )

        # fill the board with 0's
        self.player_board = (
            [["0"] * self.grid_size for _ in range(self.grid_size)]
            )
        self.computer_board = (
            [["0"] * self.grid_size for _ in range(self.grid_size)]
            )

        # place the ships on the board
        self.place_ships(self.player_board)
        self.place_ships(self.computer_board)

    def print_board(self):
        """
        Starting the game and printing the board
        """
        print("Let's play Battleship!")
        print("Player Board:")
        for row in self.player_board:
            print(" ".join(row))

        # Computer's board
        print("Computer Board:")
        for row in self.computer_board:
            print(" ".join(['0' if cell == 'X' else cell for cell in row]))

    def place_ships(self, board):
        """
        Places the ships on the board
        """
        for _ in range(self.num_of_ships):
            # generate a random row and column
            row = random.randint(0, self.grid_size - 1)
            col = random.randint(0, self.grid_size - 1)

            # check if the position is already occupied
            while board[row][col] == "X":
                row = random.randint(0, self.grid_size - 1)
                col = random.randint(0, self.grid_size - 1)

            # place the ship
            board[row][col] = "X"

    def player_guess(self, row, col):
        """
        Check if the player has already guessed this spot
        """
        if self.computer_board[row][col] in ["H", "M"]:
            print(Fore.RED + "You already guessed that spot, try again")
            return False

        # Process the player's guess
        if self.computer_board[row][col] == "X":
            print(Fore.RED + "Hit!")
            self.computer_board[row][col] = "H"
        else:
            print(Fore.BLUE + "Miss!")
            self.computer_board[row][col] = "M"
        return True

    def computer_guess(self):
        """
        Process the computer's guess
        """
        while True:
            row = random.randint(0, self.grid_size - 1)
            col = random.randint(0, self.grid_size - 1)
            # Checks so the computer wont check the same spot twice
            if self.player_board[row][col] not in ["H", "M"]:
                break
        if self.player_board[row][col] == "X":
            print(
                Fore.RED + f"Computer has hit your ship at ({row}, {col})"
                )
            self.player_board[row][col] = "H"
        else:
            print(
                Fore.BLUE + f"Computer has missed your ship at ({row}, {col})"
                )
            self.player_board[row][col] = "M"

    def play(self):
        """
        Game loop, player and computer take turns guessing
        """
        while True:
            self.print_board()

            while True:
                try:
                    guess_row = int(
                        input(f"Guess a row (0-{self.grid_size - 1}): ")
                        )
                    guess_col = int(
                        input(f"Guess a column (0-{self.grid_size - 1}): ")
                        )

                    # To warn if the player guesses outside the grid
                    if (
                        guess_row < 0
                        or guess_row >= self.grid_size
                        or guess_col < 0
                        or guess_col >= self.grid_size
                    ):
                        print(Fore.RED + "That's outside the grid")
                        continue

                    if self.player_guess(guess_row, guess_col):
                        break
                except ValueError:
                    print(Fore.RED + "Please enter a number")

            # Check if the player has won
            if not any("X" in row for row in self.computer_board):
                print(Fore.GREEN + "You sank the computers ships!")
                break

            # Computer's turn
            print("\nComputer's Turn")
            self.computer_guess()

            # Check if the computer has won
            if not any("X" in row for row in self.player_board):
                print(Fore.RED + "The computer has sunken all your ships!")
                break


if __name__ == "__main__":
    # Print a welcome message and instructions
    print(Fore.YELLOW + "===================================")
    print(Fore.YELLOW + "Welcome to the Battleship game!")
    print(Fore.YELLOW + "===================================")
    print(Fore.CYAN + """
    Instructions:
    1. You will be asked to enter the grid size and number of ships.
    2. Take turns to guess the position of each other's ships.
    3. You can guess a position by entering the row and column number
    where 0 is the first row/column.
    4. The aim is to sink all the enemy's ships before they sink yours.
    5. 'X' represents a ship.
    6. 'H' represents a hit.
    7. 'M' represents a miss.
    8. '0' represents an unknown position.
    """)

    while True:
        try:
            size = int(input("Enter the grid size: "))
            if size <= 0:   # check if the size is valid
                print(Fore.RED + "Grid size should be greater than 0.")
                continue
            break
        except ValueError:
            print(Fore.RED + "Please enter a number")

    while True:
        try:
            num_of_ships = int(input("Enter the number of ships: "))
            game = BattleshipGame(size, num_of_ships)
            break
        except ValueError as e:
            if "Number of ships can't exceed the grid size" in str(e):
                print(Fore.RED + "You have entered more ships than the grid!")
            else:
                print(Fore.RED + "Please enter a number")

    while True:
        game.play()
        # Ask if the player wants to play again
        play_again = input("Do you want to play again? (yes/no): ")
        if play_again.lower() == "yes":
            while True:
                try:
                    size = int(input("Enter the new grid size: "))
                    break
                except ValueError:
                    print(Fore.RED + "Please enter a number")
            # Check if the size is valid for the next game
            while True:
                try:
                    num_of_ships = (
                        int(input("Enter the new number of ships: "))
                        )
                    game = BattleshipGame(size, num_of_ships)
                    break
                except ValueError as e:
                    if "Number of ships can't exceed the grid size" in str(e):
                        print(Fore.RED + (
                            "You have entered more ships than the grid!")
                              )
                    else:
                        print(Fore.RED + "Please enter a number")
        else:
            break
        sys.exit()
