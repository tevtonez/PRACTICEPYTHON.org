'''
----------------------------------------
TASK 19 from http://www.practicepython.org/
----------------------------------------
Using the requests and BeautifulSoup Python libraries, print to the screen the full text of the article on this website: http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture.

The article is long, so it is split up between 4 pages. Your task is to print out the text to the screen so that you can read the full article without having to click any buttons.

This will just print the full text of the article to the screen. It will not make it easy to read, so next exercise we will learn how to write this text to a .txt file.

'''

# SOLUTION
# created by Kostya
# on 19 Feb 2017
# Time spent: 10 min

import urllib, html.parser
from bs4 import BeautifulSoup

if __name__ == '__main__':


    url = "http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture"

    with urllib.request.urlopen( url ) as response:
        html_doc = response.read()

    soup = BeautifulSoup( html_doc, 'html.parser' )
    for text in soup.select( "section.content-section > p" ):
        print( text.get_text() )
