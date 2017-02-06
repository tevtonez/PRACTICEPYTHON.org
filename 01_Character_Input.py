'''
----------------------------------------
TASK 1 from http://www.practicepython.org/
----------------------------------------
Create a program that asks the user to enter their name and their age. Print out a
message addressed to them that tells them the year that they will turn 100 years old.

Extras:
1. Add on to the previous program by asking the user for another number and printing
out that many copies of the previous message. (Hint: order of operations exists in Python)
2. Print out that many copies of the previous message on separate lines. (Hint: the
string "\n is the same as pressing the ENTER button)

'''

#
# SOLUTION
# created by Kostya
# on 21 Dec 2016
# Time spent: 7 min
#

if __name__ == '__main__':

    import datetime
    now = datetime.datetime.now()

    username = input( 'Enter your name: ' )
    userage = int( input( 'Enter your age: ' ) )

    one_hundred = int( now.year ) + 100 - userage

    print_string = "Dear {}, you'll be 100 years old on {}".format( username, one_hundred )

    print( print_string )

    # extra 1 and 2
    repetitions = int( input( 'Now enter the number of repetitions you\'d like to repeat last sentence: ' ) )
    print ( ( print_string + '\n' ) * repetitions )
