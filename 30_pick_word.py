'''
----------------------------------------
TASK 30 from http://www.practicepython.org/
----------------------------------------
This exercise is Part 1 of 3 of the Hangman exercise series.

Here are a few things to keep in mind:

In this exercise, the task is to write a function that picks a random word from a list of words from the SOWPODS dictionary.
http://norvig.com/ngrams/sowpods.txt
Download this file and save it in the same directory as your Python code.
This file is Peter Norvig’s compilation of the dictionary of words used in professional Scrabble tournaments.
Each line in the file contains a single word.

Hint: use the Python random library for picking a random word.

'''

#
# SOLUTION
# created by Kostya
# on 1 Mar 2017
# Time spent: 5 min
#

import random

if __name__ == '__main__':


    def pick_word( file_name ):

        with open( file_name, 'r' ) as f_dic:
            line = random.choice( f_dic.readlines() )

            return line



    file_name = "sowpods.txt"
    print( pick_word( file_name ) )
