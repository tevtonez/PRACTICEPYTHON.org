'''
----------------------------------------
TASK 14 from http://www.practicepython.org/
----------------------------------------
Write a program (function!) that takes a list and returns a new list that contains all
the elements of the first list minus all the duplicates.

Extras:
1. Write two different functions to do this - one using a loop and constructing a list,
and another using sets.
2. Go back and do Exercise 5 using sets, and write the solution for that in a different
function.

'''

# SOLUTION
# created by Kostya
# on 9 Feb 2017
# Time spent: 20 min


from random import randrange

if __name__ == '__main__':

    def list_to_set( _list ):
        """takes a list and makes set"""
        return set( _list )

    def generate_list( n ):
        """generates list with repeatalbe random numbers"""
        l1 = []
        for _ in range( n ):
            num = randrange( n )
            l1.append( num )
        return l1

    print ( list_to_set( generate_list( 20 ) ) )
    print( "\n\n" )

#===============================================================================
# extra
#===============================================================================
    def list_to_set_2( _list ):
        """takes a list and makes set"""
        new_list = []
        for i in _list:
            if i not in new_list:
                new_list.append( i )

        return sorted( new_list )


    print ( list_to_set_2( generate_list( 20 ) ) )

