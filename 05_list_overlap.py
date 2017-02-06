'''
----------------------------------------
TASK 5 from http://www.practicepython.org/
----------------------------------------
Take two lists, say for example these two:

  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
  b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

and write a program that returns a list that contains only the elements that are common between the lists
(without duplicates). Make sure your program works on two lists of different sizes.

Extras:

1. Randomly generate two lists to test this
2. Write this in one line of Python (don’t worry if you can’t figure this out at this point - we’ll get to it soon)


'''

#
# SOLUTION
# created by Kostya
# on 4 Jan 2017
# Time spent: 9 min
#



if __name__ == '__main__':

    import random

    def list_generator( range_list = 30, list_len = 12 ):
        return random.sample( range( range_list ), list_len )



    a = list_generator()
    b = list_generator()


    def list_comparator( list1, list2 ):
        if len( list1 ) >= len( list2 ):
            short_list = list2
            long_list = list1
        else:
            short_list = list1
            long_list = list2

        result_list = [item for item in short_list if item in long_list]

        print( "list1: {}\nlist2: {}\noverlapping numbers: {}".format( short_list, long_list, result_list ) )

    list_comparator( a, b )
