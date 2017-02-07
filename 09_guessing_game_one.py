'''
----------------------------------------
TASK 9 from http://www.practicepython.org/
----------------------------------------
Generate a random number between 1 and 9 (including 1 and 9). Ask the user
to guess the number, then tell them whether they guessed too low, too high,
or exactly right. (Hint: remember to use the user input lessons from the
very first exercise)

Extras:
1. Keep the game going until the user types "exit"
2. Keep track of how many guesses the user has taken, and when the game ends,
print this out.

'''

# SOLUTION
# created by Kostya
# on 7 Feb 2017
# Time spent: 11 min

from random import randint

def random_number():
    number = randint( 1, 9 )
    return number


def check_number( num ):
    userinput = input( "Guess the number from 1 to 9: " )



    if userinput == "exit":
        print( "Exiting game...\n" )
        return False

    elif int( userinput ) == num:
        print( "You won!" )
        return False

    elif int( userinput ) > num:
        print( "too high" )
        return True

    elif int( userinput ) < num :
        print( "too low" )
        return True




if __name__ == '__main__':

    num = random_number()
    count_num = 0

    while True:
        count_num += 1
        if not check_number( num ):
            break
    print( "You've tried to guess number {} times".format( count_num ) )


