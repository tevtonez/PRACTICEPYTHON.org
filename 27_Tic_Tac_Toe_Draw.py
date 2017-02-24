'''
----------------------------------------
TASK 27 from http://www.practicepython.org/
http://www.practicepython.org/exercise/2015/11/26/27-tic-tac-toe-draw.html
----------------------------------------
When a player (say player 1, who is X) wants to place an X on the screen, they can’t just click on a terminal.
So we are going to approximate this clicking simply by asking the user for a coordinate of where they want to
place their piece.
'''

#
# SOLUTION
# created by Kostya
# on 23 Feb 2017
# Time spent: 120 min
#

import os, copy

if __name__ == '__main__':

    def generate_board( colls = 3, rows = 3 ):
        '''Returns a dictionary with lines that form the game board'''
        board = {}

        # forming line of cells
        line = []
        for i in range( colls ):
            line.append( "|   " )
        line.append( "|" )

        # forming dictionary 'board'
        for i in range( rows ):
            board[i + 1] = copy.deepcopy( line )
            board["sep{}".format( i )] = " --- --- ---"

        return board


    def print_board( board, colls = 3, rows = 3 ):
        '''Takes game board dictionary and prints it'''
        for i in range( rows ):
            print( board["sep{}".format( i )] )
            cell_row = ""
            for cell in board[i + 1]:
                cell_row += cell
            print( cell_row )
        print( board["sep0"] )


    def update_board( board, move_col, move_row, symbol ):
        '''Updates game board dictionary with user's move'''
        board[move_row][move_col - 1] = '| ' + symbol + ' '
        return board


    #===========================================================================
    # Execution
    #===========================================================================
    os.system( 'clear' )
    print( "Welcome to Tic Tac Toe game v0001" )
    print( "\nPlayer One is always 'x' and Player Two is always 'o'\n" )

    # printing game board
    game_board = generate_board()
    print_board( game_board )

    player = 1
    symbol = "x"


    # organizing Players' moves
    while True:

        # getting row and col numbers from user
        print( "Player ", player )
        user_move_col = int( input( "Enter column number: " ) )
        user_move_row = int( input( "Enter row number: " ) )

        # clear screen
        os.system( 'clear' )

        # update the board with user move
        game_board = update_board( game_board, user_move_col, user_move_row, symbol )
        print_board( game_board )

        # change player and symbol
        if player == 1:
            player = 2
            symbol = "o"
        else:
            player = 1
            symbol = "x"


