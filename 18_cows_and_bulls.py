'''
----------------------------------------
TASK 17 from http://www.practicepython.org/
----------------------------------------
Create a program that will play the “cows and bulls” game with the user. The game works like this:

Randomly generate a 4-digit number. Ask the user to guess a 4-digit number. For every digit that the user guessed correctly in the correct place, they have a “cow”. For every digit the user guessed correctly in the wrong place is a “bull.” Every time the user makes a guess, tell them how many “cows” and “bulls” they have. Once the user guesses the correct number, the game is over. Keep track of the number of guesses the user makes throughout teh game and tell the user at the end.

Say the number generated by the computer is 1038. An example interaction could look like this:

  Welcome to the Cows and Bulls Game!
  Enter a number:
  >>> 1234
  2 cows, 0 bulls
  >>> 1256
  1 cow, 1 bull
  ...
Until the user guesses the number.

'''

# SOLUTION
# created by Kostya
# on 19 Feb 2017
# Time spent: 12 min

import random

def play_game():

    number = str( random.randint( 1000, 9999 ) )
    tries = 0
    print( number )

    while True:

        user_guess = input( "Enter a number: \n" )
        cows = 0
        bulls = 0

        for i in range( 4 ):
            if user_guess[i] == number[i]:
                cows += 1
            else:
                bulls += 1

        print( "{} cows, {} bulls".format( cows, bulls ) )

        if cows == 4:
            print ( "You win in {} tries".format( tries ) )
            break



        tries += 1


if __name__ == '__main__':

    print( "Welcome to the Cows and Bulls Game! \n" )

    play_game()
