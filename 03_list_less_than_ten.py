'''
----------------------------------------
TASK 3 from http://www.practicepython.org/
----------------------------------------
Take a list, say for example this one:
  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
and write a program that prints out all the elements of the list that are less than 5.

EXTRAS:
1. Instead of printing the elements one by one, make a new list that has all the elements
less than 5 from this list in it and print out this new list.

2. Write this in one line of Python.

3. Ask the user for a number and return a list that contains only elements from the
original list a that are smaller than that number given by the user.

'''

#
# SOLUTION
# created by Kostya
# on 21 Dec 2016
# Time spent: 4 min
#

if __name__ == '__main__':

    a_list = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

    user_num = int( input( 'please, enter a number: ' ) )
    b_list = [item for item in a_list if item > user_num]
    print ( b_list )
