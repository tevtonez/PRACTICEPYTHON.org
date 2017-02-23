'''
----------------------------------------
TASK 21 from http://www.practicepython.org/
----------------------------------------
Ask the user what size game board they want to draw, and draw it for them to the screen using Python’s print statement.

'''

#
# SOLUTION
# created by Kostya
# on 23 Feb 2017
# Time spent: 20 min
#


if __name__ == '__main__':

    # size = input( "Enter size of the board in row, columns (eg. 3,4 ): " )
    # size = size.strip().split( sep = "," )

    """
    a = '---'.join( '    ' )
    b = '   '.join( '||||' )
    print( '\n'.join( ( a, b, a, b, a, b, a ) ) )
    """


    cols = 4
    rows = 3

    a = "aaa"
    a_sp = " " * ( cols + 1 )
    a_ready = a.join( a_sp )

    b = "   "
    b_sp = "|" * ( cols + 1 )
    b_ready = b.join( b_sp )

    line_part = [a_ready]

    for i in range( rows ):
        line_part.append( b_ready )
        line_part.append( a_ready )


    print( "\n" .join( ( line_part ) ) )
