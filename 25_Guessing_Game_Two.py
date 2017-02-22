'''
----------------------------------------
TASK 25 from http://www.practicepython.org/
----------------------------------------
You, the user, will have in your head a number between 0 and 100. The program will guess a number, and
you, the user, will say whether it is too high, too low, or your number.

At the end of this exchange, your program should print out how many guesses it took to get your number.
'''

#
# SOLUTION
# created by Kostya
# on 22 Feb 2017
# Time spent: 25 min
#

import time

if __name__ == '__main__':

    print( 'Think of a number between 0 and 100. Computer will try to guess it.' )
    time.sleep( 3 )
    print( "Let's start!" )


    start_range = 0
    end_range = 100
    range_nums = list( range( 100 ) )

    comp_guess = range_nums[int( len( range_nums ) / 2 )]

    tries = 0

    while True:



        print( "My guess the number is: {}".format( comp_guess ) )
        user_answer = input( "Type 'To big', 'To small' or 'Correct': " )

        if user_answer.lower() == "to big":
            end_range = comp_guess
            range_nums = range( start_range, comp_guess )
            comp_guess = range_nums[int( len( range_nums ) / 2 )]
            tries += 1


        elif user_answer.lower() == "to small":
            start_range = comp_guess
            range_nums = range( comp_guess, end_range )
            comp_guess = range_nums[int( len( range_nums ) / 2 )]
            tries += 1


        elif user_answer.lower() == "correct":
            print( 'Comp guessed the number in {} tries.'.format( tries ) )
            break
