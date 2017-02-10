'''
----------------------------------------
TASK 14 from http://www.practicepython.org/
----------------------------------------
Write a program (using functions!) that asks the user for a long string containing multiple
words. Print back to the user the same string, except with the words in backwards order.

For example, say I type the string:

  My name is Michele
Then I would see the string:

  Michele is name My

shown back to me.

'''

# SOLUTION
# created by Kostya
# on 10 Feb 2017
# Time spent: 6 min


if __name__ == '__main__':

    def get_phrase( text = "Enter a phrase you want to reverse: " ):

        entered_text = input( text ).split( " " )
        reversed_text = entered_text[::-1]

        print( ' '.join( reversed_text ) )


    get_phrase()
