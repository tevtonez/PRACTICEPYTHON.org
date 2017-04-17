'''
----------------------------------------
TASK 33 from http://www.practicepython.org/
----------------------------------------

This exercise is Part 4 of 4 of the birthday data exercise series.

In this exercise, use the bokeh Python library to plot a histogram of which months the scientists
have birthdays in! Because it would take a long time for you to input the months of various scientists,
you can use my scientist birthday JSON file. Just parse out the months and draw your histogram.
'''

#
# SOLUTION
# created by Kostya
# on 17 Apr 2017
# Time spent: 20 min
#

import os
import json
import collections

from bokeh.plotting import figure, show, output_file




def read_file( file ):
    '''Takes a JSON file and prints the names form it. Also returns a dictionary with keys/values'''

    # check if file isn't empty
    if os.stat( file ).st_size == 0:
        print( 'File is empty.' )
        quit()

    else:
        # loading from JSON file to a dictionary
        with open( file, 'r' ) as bd_file:
            load_from_json = json.load( bd_file )

            return load_from_json


def print_names( load_from_json ):
    '''Takes a dictionary and prints its keys'''
    # printing the names from bd file
    print( '\nWe know the birthdays of:' )
    for name in load_from_json.keys():
        print( '-', name )


def get_bd( load_from_json, name ):
    '''Takes a dictionary with keys/values pairs and a string, then prints bd date for that string key'''

    bd_date = load_from_json[name]
    print( "{}'s birthday is {}".format( name, bd_date ) )

def month_bds( load_from_json ):

    # making a list of months
    months_list = []
    for value in load_from_json.values():
        months_list.append( value.split( ' ' )[0] )

    # counting month in the list
    month_counter = collections.Counter( months_list )

    for key, value in month_counter.items():
        print( key, ':', value )

def month_bds_for_plot( load_from_json, plot_file_name ):

    # making lists for the months and occurrences
    bd_months_list = []
    x_months = []
    months_list = ['January', 'February', 'March', 'April', 'May', 'July', 'June', 'August', 'September', 'October', 'November', 'December']
    y_occur = []

    for value in load_from_json.values():
        bd_months_list.append( value.split( ' ' )[0] )

    # counting month in the list
    month_counter = collections.Counter( bd_months_list )

    for key, value in month_counter.items():
        x_months.append( key )
        y_occur.append( value )

    # saving plot file
    output_file( plot_file_name + ".html" )

    # building plot
    plot = figure( x_range = months_list )
    plot.vbar( x = x_months, top = y_occur, width = 0.5 )

    show ( plot )




#===============================================================================
# EXECUTION
#===============================================================================
if __name__ == '__main__':

    print( "Welcome to the birthday dictionary!" )


    file = 'task_34_birthdays.json'
    print_names( read_file( file ) )

    while True:
        user_input = input( "\nType name to look up for a birthday\n\nType 'add' do add new item to  the birthday dictionary;\nType 'month' to see how many people have a birthday in each month.;\nType 'plot' to plot data in HTML file.\n;\nType 'exit' to quit.\n" )

        if user_input == "add":
            # ask user for name and date
            user_name = input( 'Enter name: ' )
            user_bd = input( "Enter birthday date: " )

            dictionary = read_file( file )

            # add new data to a dictionary
            dictionary[user_name] = user_bd

            # saving to a JSON file
            with open( file, 'w' ) as jf:
                json.dump( dictionary, jf )

            # print updated list of names
            print_names( read_file( file ) )

        elif user_input == 'month':
            month_bds( read_file( file ) )

        elif user_input == 'plot':
            plot_file_name = input( "Enter file name to save plot (without extension): " )

            month_bds_for_plot( read_file( file ), plot_file_name )

        elif user_input == 'exit':
            quit()

        else:
            get_bd( read_file( file ), user_input )



