'''
----------------------------------------
TASK 16 from http://www.practicepython.org/
----------------------------------------
Write a password generator in Python. Be creative with how you generate passwords - strong passwords
have a mix of lowercase letters, uppercase letters, numbers, and symbols. The passwords should be random,
generating a new password every time the user asks for a new password. Include your run-time code in a
main method.

Extra:

1. Ask the user how strong they want their password to be. For weak passwords, pick a word or two from a list.

'''

# SOLUTION
# created by Kostya
# on 10 Feb 2017
# Time spent: 44 min

import random
import string

if __name__ == '__main__':


    def gen_pass( strength ):
        '''Takes number as an argument and generates password with desired length'''
        chars_list = string.ascii_letters + string.digits + string.punctuation
        print ( "".join( random.choice( chars_list ) for i in range( int( strength ) ) ) )


    #===========================================================================
    # EXECUTION
    #===========================================================================
    pass_strength = input( "\nEnter desired length of the password: " )
    while True:
        if pass_strength:
            break

    gen_pass( pass_strength )
