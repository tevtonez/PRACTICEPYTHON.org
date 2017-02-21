'''
----------------------------------------
TASK 21 from http://www.practicepython.org/
----------------------------------------
Given a task22-1.txt file that has a list of a bunch of names, count how many of each name there are in the file,
and print out the results to the screen.

Extra:

Instead of using the .txt file from above (or instead of, if you want the challenge), take task22-2.txt file,
and count how many of each “category” of each image there are. This text file is actually a list of files
corresponding to the SUN database scene recognition database, and lists the file directory hierarchy for
the images. Once you take a look at the first line or two of the file, it will be clear which part represents
the scene category. To do this, you’re going to have to remember a bit about string parsing in Python 3.
I talked a little bit about it in this post (http://www.practicepython.org/exercise/2014/03/12/06-string-lists.html).
'''

#
# SOLUTION
# created by Kostya
# on 21 Feb 2017
# Time spent: 14 min without extra
# additional xx min for extra task
#



def read_file_content( file_name ):

    # read the file into content var
    with open( file_name, 'r', encoding = 'utf-8' ) as file:
        content = file.readlines()

    # create dictionary
    names = {}

    # read from content and fill in the dictionary, counting names
    for line in content:

        # strip new lines chars
        line = line.strip()

        # fill in the dictionary with names and numbers
        if line in names.keys():
            names[line] += 1
        else:
            names[line] = 1

    return names



if __name__ == '__main__':

#===============================================================================
# task22-1.txt file
#===============================================================================


    file_name = "task22-1.txt"

    for name, quantity in read_file_content( file_name ).items():
        print ( "{} - {}".format( name, quantity ) )


