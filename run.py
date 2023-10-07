import random


class battleshipgame:
    def __init__(self):
        #initialize the game parameters with grid size and number of ships
        self.grid_size = 10
        self.num_of_ships = 5

        # fill the board with 0's
        self.player_board = [['0'] * self.grid_size for i in range(self.grid_size)]
        self.computer_board = [['0'] * self.grid_size for i in range(self.grid_size)]

        # place the ships on the board
        self.place_ships(self.player_board)
        self.place_ships(self.computer_board)


main()
    game = battleshipgame()    
    game.play()    


    #starting the game and printing the board
print "Let's play Battleship!"