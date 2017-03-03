'''
----------------------------------------
TASK 32 from http://www.practicepython.org/
----------------------------------------
This exercise is Part 3 of 3 of the Hangman exercise series.

In this exercise, we will finish building Hangman.
In the game of Hangman, the player only has 6 incorrect guesses (head, body, 2 legs, and 2 arms) before they lose the game.

In Part 1, we loaded a random word list and picked a word from it.
In Part 2, we wrote the logic for guessing the letter and displaying that information to the user.
In this exercise, we have to put it all together and add logic for handling guesses.

Copy your code from Parts 1 and 2 into a new file as a starting point. Now add the following features:

1. Only let the user guess 6 times, and tell the user how many guesses they have left.
2. Keep track of the letters the user guessed. If the user guesses a letter they already guessed, don’t penalize them - let them guess again.
Optional additions:

- When the player wins or loses, let them start a new game.
- Rather than telling the user "You have 4 incorrect guesses left", display some picture art for the Hangman. This is challenging - do the other parts of the exercise first!

Your solution will be a lot cleaner if you make use of functions to help you!

'''

#
# SOLUTION
# created by Kostya
# on 3 Mar 2017
# Time spent: 20 min
#

import  random

def pick_word( file_name ):

    with open( file_name, 'r' ) as f_dic:
        line = random.choice( f_dic.readlines() )

        print ( line )

        return line



def guess_letter( word ):

    # forming answer list
    answer_list = []
    for letter in word.strip():
        answer_list.append( '_' )

    positions = []
    guessed_letters = []
    guesses = len( word.strip() )

    while True:
        user_inupt = input( "Guess your letter: " ).upper()

        # add letter to guessed list
        if user_inupt not in guessed_letters:
            guessed_letters.append( user_inupt )
            guesses -= 1

            if user_inupt in word:

                positions = [pos for pos, char in enumerate( word ) if char == user_inupt]

                for i in positions:
                    answer_list[i] = user_inupt

                answer_str = ''.join( answer_list )

                print( answer_str )

                if '_' not in answer_list:
                    print( "You won!" )
                    break

            else:
                print( "Wrong letter!" )


            if guesses == 0:
                print( "You loose!" )
                print( "The word was:", word )
                break

        else:
            print( "You've tried this letter already!" )

        print( 'you have {} guesses left'.format( guesses ) )




if __name__ == '__main__':


    print( "Welcome to Hangman!\n" )

    file_name = "sowpods.txt"
    guess_letter( pick_word( file_name ) )
