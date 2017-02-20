'''
----------------------------------------
TASK 20 from http://www.practicepython.org/
----------------------------------------
Write a function that takes an ordered list of numbers (a list where the elements are in order from smallest
to largest) and another number. The function decides whether or not the given number is inside the list and
returns (then prints) an appropriate boolean.

Extras:
1. Use binary search.
'''

# SOLUTION
# created by Kostya
# on 20 Feb 2017
# Time spent: 3 min without extra + 6 mins for extra

def find_number( l, n ):
    if n in l:
        return True

    return False


#===============================================================================
# binary search
#===============================================================================
def binary_simple( l, n ):

    start = 1
    end = len( l ) - 1


    while True:

        middle = int( ( end - start ) / 2 )

        if middle < 0 or middle > end or middle < start:
            return False

        if n == l[middle]:
            return True

        elif middle > n:
            start = middle
        else:
            end = middle


if __name__ == '__main__':

    l = [2, 4, 6, 8, 10]
    n = 4

    print( find_number( l, n ) )

#===============================================================================
# binary search
#===============================================================================




    print( binary_simple( l, n ) )

