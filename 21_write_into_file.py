'''
----------------------------------------
TASK 21 from http://www.practicepython.org/
----------------------------------------
This exercise is Part 1 of 4 of the Tic Tac Toe exercise series.
The other exercises are: Part 2, Part 3, and Part 4.

Time for some fake graphics! Let’s say we want to draw game boards that look like this:

 --- --- ---
|   |   |   |
 --- --- ---
|   |   |   |
 --- --- ---
|   |   |   |
 --- --- ---
This one is 3x3 (like in tic tac toe). Obviously, they come in many other sizes
(8x8 for chess, 19x19 for Go, and many more).

Ask the user what size game board they want to draw, and draw it for them to the
screen using Python’s print statement.

Extras:

Ask the user to specify the name of the output file that will be saved.

'''

#
# SOLUTION
# created by Kostya
# on 14 Feb 2017
# Time spent: 20 min
#

def draw_line( cols, rows ):

    a = " ---"
    b = "|   "

    for row in range( int( rows ) ):
        print( a * int( cols ) )
        print( b * int( cols ) + "|" )
        print( a * int( cols ) )



if __name__ == '__main__':

    cols = input( "Enter number of columns: " )
    rows = input( "Enter number of rows: " )

    draw_line( cols, rows )

