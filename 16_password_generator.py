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

from random import *
import string

if __name__ == '__main__':


    def gen_pass( strength ):
        numb_list = range( 10 )
        chars_list = string.ascii_lowercase
        password = []


        if strength == "w":
            # generating weak numeric password

            for i in range( 6 ):
                password.append( str( choice( numb_list ) ) )

            password_res = "".join( password )
            print ( password_res )


        elif strength == "m":
            # generating medium alpha-numeric password
            for i in range( 5 ):
                password.append( str( choice( numb_list ) ) )
                password.append( choice( chars_list ) )

            shuffle( password )
            password_res = "".join( password )
            print ( password_res )


        else:
            # generating strong alpha-numeric case-sensitive password
            for i in range( 7 ):
                password.append( str( choice( numb_list ) ) )
                upper_case = choice( [0, 1] )
                if upper_case:
                    password.append( choice( chars_list.upper() ) )
                else:
                    password.append( choice( chars_list ) )
                password.append( choice( chars_list ) )

            shuffle( password )
            password_res = "".join( password )
            print ( password_res )




    answers = ["s", "w", "m", ""]
    pass_strength = input( "\nHow strong password should be? (Strong [S], Medium [M], Weak [W])\nDefault [S]trong: " )

    while pass_strength.lower() not in answers:
        pass_strength = input( "\nHow strong password should be? (Strong [S], Medium [M], Weak [W])\nDefault [S]trong: " )


    gen_pass( pass_strength )
