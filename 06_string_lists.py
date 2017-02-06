'''
----------------------------------------
TASK 6 from http://www.practicepython.org/
----------------------------------------
Ask the user for a string and print out whether this string is a palindrome or not.
(A palindrome is a string that reads the same forwards and backwards.)

'''

#
# SOLUTION
# created by Kostya
# on 4 Jan 2017
# Time spent: 2 min
#


if __name__ == '__main__':

    word = input( "Enter a single word, please: " )

    if word == word[::-1]:
        print ( "The word '{}' is a palindrome!".format( word ) )
    else:
        print( "Word '{}' is not a palindrome".format( word ) )

