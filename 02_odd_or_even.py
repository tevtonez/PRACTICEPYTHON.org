'''
----------------------------------------
TASK 2 from http://www.practicepython.org/
----------------------------------------
Ask the user for a number. Depending on whether the number is even or odd, print out
an appropriate message to the user. Hint: how does an even / odd number react
differently when divided by 2?

Extras:
1. If the number is a multiple of 4, print out a different message.
2. Ask the user for two numbers: one number to check (call it num) and one number to
divide by (check). If check divides evenly into num, tell that to the user. If not,
print a different appropriate message.

'''

#
# SOLUTION
# created by Kostya
# on 21 Dec 2016
# Time spent: zz min
#

if __name__ == '__main__':

    num = int( input( 'Enter a number: ' ) )

    if __name__ == '__main__':
        if num % 4 == 0 :
            print( num, ' is a multiple of 4!' )

        elif num % 2 == 0:
            print( num, ' is Even!' )

        else:
            print( num, ' is Odd.' )

        check = int( input( 'Now enter 2nd number, please: ' ) )

        if num % check == 0:
            print( 'Oh! {} is divided evenly by {}'.format( num, check ) )
        else:
            print( 'Number {} is NOT divided evenly by {}'.format( num, check ) )
