'''
----------------------------------------
TASK 11 from http://www.practicepython.org/
----------------------------------------
Ask the user for a number and determine whether the number is prime or not.
(For those who have forgotten, a prime number is a number that has no divisors.).
You can (and should!) use your answer to Exercise 4 to help you. Take this opportunity
to practice using functions, described below.
'''

# SOLUTION
# created by Kostya
# on 8 Feb 2017
# Time spent: 10 min


if __name__ == '__main__':

    def ask_for_number( text = "Please, enter a number: " ):
        return int( input( text ) )


    def check_if_prime( num ):
        divisors_list = [number for number in range( 2, num ) if num % number == 0]
        if len( divisors_list ) > 0:
            print( "Not a PRIME number!" )
        else:
            print( "Yay, the number is PRIME number." )


    check_if_prime( ask_for_number() )


