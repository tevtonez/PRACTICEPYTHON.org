'''
----------------------------------------
TASK 17 from http://www.practicepython.org/
----------------------------------------
WUse the BeautifulSoup and requests Python packages to print out a list of all the article titles on the New York Times home page.

'''

# SOLUTION
# created by Kostya
# on 10 Feb 2017
# Time spent: 60 min

import urllib, html.parser
from bs4 import BeautifulSoup

if __name__ == '__main__':


    url = "http://www.nytimes.com/"

    with urllib.request.urlopen( url ) as response:
        html_doc = response.read()

    soup = BeautifulSoup( html_doc, 'html.parser' )
    for title in soup.find_all( 'h2' ):
        print( title.get_text() )


