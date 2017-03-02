'''
----------------------------------------
TASK 29 from http://www.practicepython.org/
http://www.practicepython.org/exercise/2016/08/03/29-tic-tac-toe-game.html
----------------------------------------
The next step is to put all these three components together to make a two-player Tic Tac Toe game! Your challenge in this exercise is to use the functions from those previous exercises all together in the same program to make a two-player game that you can play with a friend. There are a lot of choices you will have to make when completing this exercise, so you can go as far or as little as you want with it.

Here are a few things to keep in mind:

You should keep track of who won - if there is a winner, show a congratulatory message on the screen.
If there are no more moves left, don’t ask for the next player’s move!
As a bonus, you can ask the players if they want to play again and keep a running tally of who won more - Player 1 or Player 2.
'''

#
# SOLUTION
# created by Kostya
# on 24 Feb 2017
# Time spent: 00- min
#

import os, copy



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



def check_winner( board, colls = 3, rows = 3 ):
    '''Takes game board dictionary and checks if there are winning combinations'''
    winner = None
    check_set = {"|   "}

    # checking rows
    for i in range( rows ):
        if "|   " not in board[i + 1]:
            row_set = set( board[i + 1] )
            check_set = row_set


    # checking columns
    for i in range( colls ):
        cells_list = []
        for r in range( rows ):
            cells_list.append( board[r + 1][i] )

        coll_set = set( cells_list )
        if "|   " not in coll_set:
            check_set = coll_set


    # checking diagonals
    # HARDCODED!!!
    diagonals = [ [ board[1][0], board[2][1], board[3][2] ], [ board[3][0], board[2][1], board[1][2] ] ]
    for diagonal in diagonals:
        diagonal_set = set( diagonal )
        if "|   " not in diagonal_set:
            if ( "| x " not in diagonal_set ) or ( "| o " not in diagonal_set ):
                check_set = diagonal_set



    if "|   " not in check_set:
        if "| x " in check_set and "| o " in check_set:
            pass

        elif "| x " not in check_set:
            winner = 2
            print( "Player2 wins!" )

        elif "| o " not in check_set:
            winner = 1
            print( "Player1 wins!" )

    return winner

if __name__ == '__main__':

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

        # checking if we have a winner:
        if check_winner( game_board ):
            break


        # checking if there are empty cells
        lines = game_board.values()
        empty_cell = 0

        for cell_line in lines:
            for cell in cell_line:
                if "|   " in cell:
                    empty_cell += 1

        if empty_cell == 0:
            print( "No moves left, game over and it seems to be a tie!" )
            break


        # getting row and col numbers from user
        print( "Player ", player )
        user_move_col = int( input( "Enter column number: " ) )
        user_move_row = int( input( "Enter row number: " ) )

        # clear screen
        os.system( 'clear' )

        # checking if chosen cell is empty
        if game_board[user_move_row][user_move_col - 1] == "|   ":
            # update the board with user move
            game_board = update_board( game_board, user_move_col, user_move_row, symbol )
            print_board( game_board )
            # print( game_board )

            # change player and symbol
            if player == 1:
                player = 2
                symbol = "o"
            else:
                player = 1
                symbol = "x"
        else:
            print( "You may pick only empty cells. This one isn't empty. Try again. \n" )


