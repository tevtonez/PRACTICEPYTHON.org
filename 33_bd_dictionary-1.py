'''
----------------------------------------
TASK 33 from http://www.practicepython.org/
----------------------------------------
For this exercise, we will keep track of when our friend’s birthdays are, and be able to find that
information based on their name. Create a dictionary (in your file) of names and birthdays. When
you run your program it should ask the user to enter a name, and return the birthday of that person
back to them. The interaction should look something like this:

>>> Welcome to the birthday dictionary. We know the birthdays of:
Albert Einstein
Benjamin Franklin
Ada Lovelace
>>> Who's birthday do you want to look up?
Benjamin Franklin
>>> Benjamin Franklin's birthday is 01/17/1706.



'''

#
# SOLUTION
# created by Kostya
# on 4 Mar 2017
# Time spent: 13 min
#

import os

def read_file( file ):

    if os.stat( file ).st_size == 0:
        print( 'File is empty.' )
        quit()

    else:
        print( 'We know the birthdays of' )
        with open( file, 'r' ) as bd_file:
            for line in bd_file:
                print( line.split( ':' )[0] )

def get_bd( name ):

    bd_dictionary = {}

    with open( file, 'r' ) as bd_file:
         for line in bd_file:
            bd_dictionary[line.split( ':' )[0]] = line.split( ':' )[1]

    bd_date = bd_dictionary[name]
    print( "{}'s birthday is {}".format( name, bd_date ) )


if __name__ == '__main__':

    print( "Welcome to the birthday dictionary!" )

    file = 'task_33_birthdays.txt'
    read_file( file )

    user_input = input( "Who's birthday do you want to look up? " )

    get_bd( user_input )
