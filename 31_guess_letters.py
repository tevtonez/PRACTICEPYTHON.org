'''
----------------------------------------
TASK 31 from http://www.practicepython.org/
----------------------------------------
This exercise is Part 2 of 3 of the Hangman exercise series.

Here are a few things to keep in mind:

Let’s say the word the player has to guess is “EVAPORATE”. For this exercise, write the logic that asks a player to
guess a letter and displays letters in the clue word that were guessed correctly. For now, let the player guess an
infinite number of times until they get the entire word. As a bonus, keep track of the letters the player guessed
and display a different message if the player tries to guess that letter again. Remember to stop the game when all
the letters have been guessed correctly! Don’t worry about choosing a word randomly or keeping track of the number
of guesses the player has remaining - we will deal with those in a future exercise.

'''

#
# SOLUTION
# created by Kostya
# on 3 Mar 2017
# Time spent: 20 min
#


def guess_letter( word ):

    # forming answer list
    answer_list = []
    for letter in word:
        answer_list.append( '_' )

    positions = []
    guessed_letters = []

    while True:
        user_inupt = input( "Guess your letter: " ).upper()

        # add letter to guessed list
        if user_inupt not in guessed_letters:
            guessed_letters.append( user_inupt )

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

        else:
            print( "You've tried this letter already!" )




if __name__ == '__main__':


    print( "Welcome to Hangman!\n" )
    guess_letter( "EVAPORATE" )
