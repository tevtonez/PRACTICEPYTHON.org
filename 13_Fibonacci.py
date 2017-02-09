'''
----------------------------------------
TASK 13 from http://www.practicepython.org/
----------------------------------------
Write a program that asks the user how many Fibonnaci numbers to generate and then
generates them. Take this opportunity to think about how you can use functions.
Make sure to ask the user to enter the number of numbers in the sequence to generate.
(Hint: The Fibonnaci seqence is a sequence of numbers where the next number in the
sequence is the sum of the previous two numbers in the sequence. The sequence looks
like this: 1, 1, 2, 3, 5, 8, 13, …)

'''

#
# SOLUTION
# created by Kostya
# on 9 Feb 2017
# Time spent: 19 min
#


if __name__ == '__main__':

    def number_from_user( text = "Please, provide a desired length of Fibonacci sequence: " ):
        num = int( input( text ) )
        return num

    def fibonacci( length ):
        fib_list = []
        prev_prev_num = 0
        prev_num = 0
        start_num = 1

        for _ in range( length ):
            # starting Fibonacci sequence
            if start_num == 1:
                num_to_add = start_num + prev_prev_num + prev_num
                prev_prev_num = prev_num
                prev_num = start_num
                start_num = 0
            # continue sequence
            else:
                num_to_add = prev_prev_num + prev_num
                prev_prev_num = prev_num
                prev_num = num_to_add

            # add number if it's not zero
            if num_to_add > 0: fib_list.append( num_to_add )

        return fib_list

    print( fibonacci( number_from_user() ) )
