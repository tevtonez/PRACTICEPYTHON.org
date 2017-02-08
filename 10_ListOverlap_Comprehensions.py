'''
----------------------------------------
TASK 10 from http://www.practicepython.org/
----------------------------------------
This week’s exercise is going to be revisiting an old exercise (see Exercise 5),
except require the solution in a different way.

Take two lists, say for example these two:

    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]


and write a program that returns a list that contains only the elements that are
common between the lists (without duplicates). Make sure your program works on
two lists of different sizes. Write this in one line of Python using at least
one list comprehension. (Hint: Remember list comprehensions from Exercise 7).

The original formulation of this exercise said to write the solution using one
line of Python, but a few readers pointed out that this was impossible to do
without using sets that I had not yet discussed on the blog, so you can either
choose to use the original directive and read about the set command in Python 3.3,
or try to implement this on your own and use at least one list comprehension in
the solution.

Extra:
Randomly generate two lists to test this

'''

# SOLUTION
# created by Kostya
# on 8 Feb 2017
# Time spent: 12 min

from random import sample

if __name__ == '__main__':

    def generate_lists():
        """generates 2 list with random numbers"""

        l1 = sample( range( 15 ), 11 )
        l2 = sample( range( 15 ), 13 )

        return l1, l2


    l1, l2 = generate_lists()
    result_list = [elem for elem in set( l2 ) if elem in set( l1 )]

    print ( result_list )



