'''
----------------------------------------
TASK 7 from http://www.practicepython.org/
----------------------------------------
ALet’s say I give you a list saved in a variable: a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100].
Write one line of Python that takes this list a and makes a new list that has only the even
elements of this list in it.

'''

#
# SOLUTION
# created by Kostya
# on 4 Jan 2017
# Time spent: 1 min
#


if __name__ == '__main__':

    a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

    b = [item for item in a if item % 2 == 0]
    print( b )
