'''
----------------------------------------
TASK 4 from http://www.practicepython.org/
----------------------------------------
Create a program that asks the user for a number and then prints out a list of all the
divisors of that number. (If you don’t know what a divisor is, it is a number that
divides evenly into another number. For example, 13 is a divisor of 26 because 26 / 13
has no remainder.)

EXTRAS:
1.

'''

#
# SOLUTION
# created by Kostya
# on 21 Dec 2016
# Time spent: 5 min
#

if __name__ == '__main__':

    # getting the number from user
    user_num = int( input( 'Please enter a number: ' ) )

    # getting the divisors:
    div_list = [number for number in range( 2, user_num ) if user_num % number == 0]
    print ( div_list )
