'''
----------------------------------------
TASK 21 from http://www.practicepython.org/
----------------------------------------
Take the code from the How To Decode A Website #17 exercise and instead of printing the results to a screen,
write the results to a txt file. In your code, just make up a name for the file you are saving to.

Extras:

1. Ask the user to specify the name of the output file that will be saved.

'''

#
# SOLUTION
# created by Kostya
# on 20 Feb 2017
# Time spent: 15 min
#



import urllib, html.parser
from bs4 import BeautifulSoup


if __name__ == '__main__':

    file_name = input( "Enter desired file name: " )
    file_name += ".txt"


    url = "http://www.nytimes.com/"

    with urllib.request.urlopen( url ) as response:
        html_doc = response.read()

    soup = BeautifulSoup( html_doc, 'html.parser' )

    with open( file_name, 'w', encoding = 'utf-8', newline = "\n" ) as file:
        try:
            for title in soup.select( 'h2.story-heading' ):
                file.write( title.get_text().strip() + "\n" )
            print( "File '{}' written successfully!".format( file_name ) )
        except:
            print( "Failed writing into a file '{}'.".format( file_name ) )
