"""
Code for Scraping AZLyrics for Doja Cat Songs
"""

# import libraries
import urllib.request as urllib2
from bs4 import BeautifulSoup
import pandas as pd
import re
from unidecode import unidecode

#################################
# Create Datafame to store Lyrics
#################################

# specify the url
webpage = "https://www.azlyrics.com/d/dojacat.html"
file = "songs.csv"
songs = pd.read_csv(file)

# query the website and return the html
page = requests.get(webpage)

# parse the html using beautiful soup
soup = BeautifulSoup(page.content, "html.parser")
