'''
----------------------------------------
TASK 23 from http://www.practicepython.org/
----------------------------------------
Given two .txt files that have lists of numbers in them, find the numbers that are
overlapping. One .txt file has a list of all prime numbers under 1000, and the other
.txt file has a list of happy numbers up to 1000.

(If you forgot, prime numbers are numbers that can’t be divided by any other number.
And yes, happy numbers are a real thing in mathematics - you can look it up on Wikipedia.
'''

#
# SOLUTION
# created by Kostya
# on 21 Feb 2017
# Time spent: 9 min
#


if __name__ == '__main__':

    file_primes = '23-prime_numbers.txt'
    file_happies = '23-happy_numbers.txt'

    with open( file_primes, "r" ) as primes:
        prime_numbers = []
        for line in primes:
            prime_numbers.append( int( line.strip() ) )

    with open( file_happies, "r" ) as happies:
        happy_numbers = []
        for line in happies:
            happy_numbers.append( int( line.strip() ) )


    print( len( happy_numbers ) )
    print( len( prime_numbers ) )

    owerlap = []
    for i in prime_numbers:
        if i in happy_numbers:
            owerlap.append( i )

    print( owerlap )

