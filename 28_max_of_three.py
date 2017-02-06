'''
----------------------------------------
TASK 28 from http://www.practicepython.org/
----------------------------------------
Implement a function that takes as input three variables, and returns the
largest of the three. Do this without using the Python max() function!
The goal of this exercise is to think about some internals that Python
normally takes care of for us. All you need is some variables and if statements!

'''

#
# SOLUTION
# created by Kostya
# on 5 Jan 2017
# Time spent: 3 min
#

def max_of_three( a, b, c ):

    if a > b and a > c:
        max_num = a
    elif b > a and b > c:
        max_num = b
    else:
        max_num = c

    print( max_num )

if __name__ == '__main__':

    max_of_three( 200, 100, 1900 )

