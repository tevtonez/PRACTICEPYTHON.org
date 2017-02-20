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
# Time spent: 3 min without extra

def find_number( l, n ):
    if n in l:
        print ( "True" )
        return True
    print( "False" )
    return False

if __name__ == '__main__':

    l = [2, 4, 6, 8, 10]
    n = 3

    find_number( l, n )

