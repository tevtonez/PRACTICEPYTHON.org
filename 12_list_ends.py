'''
----------------------------------------
TASK 12 from http://www.practicepython.org/
----------------------------------------
Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25])
and makes a new list of only the first and last elements of the given list.
For practice, write this code inside a function.

'''

#
# SOLUTION
# created by Kostya
# on 4 Jan 2017
# Time spent: 3 min
#


if __name__ == '__main__':

    def first_n_last( l ):
        new_list = []
        new_list.extend( ( l[0], l[-1] ) )
        print( new_list )

a = [5, 10, 15, 20, 25]
first_n_last( a )
