"""
Code for Scraping AZLyrics for Doja Cat Songs
"""

# import libraries
import urllib.request as urllib2
from bs4 import BeautifulSoup
import pandas as pd
import os
import re
from unidecode import unidecode

#################################
# Create Datafame to store Lyrics
#################################

os.chdir("/Users/emeliamavis/703/doja-cat-lyric-generator/")

# grab the pre-defined dataframe of song titles
file = f"{os.getcwd()}/doj_songs.csv"
songs_df = pd.read_csv(file)


# specify the url (with fomatting brackets)
webpage = "https://www.azlyrics.com/d/dojacat/{}.html"

for index, row in songs_df.iterrows():

    # grab each song's webpage
    page = urllib2.urlopen(webpage.format(row[1].replace(" ", "")))

    # parse the html using beautiful soup
    soup = BeautifulSoup(page, "html.parser")

    print(page)
