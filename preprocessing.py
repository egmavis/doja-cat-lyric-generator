import pandas as pd
import re
import numpy as np

songs = pd.read_csv("doj_songs.csv")
songs


"""
Tokenize the data
"""

# merge all characters together in one string
text = ""
clean = ""
for line in songs["lyrics"]:
    text = text + str(line).lower()
    clean = clean + " ".join(re.findall(r"[a-z']+", text))

# find all unique characters
tokens = re.findall(r"[a-z'\s]", clean)


"""
Define the alphabet
"""

characters = sorted(list(set(tokens)))
len(characters)
# 28 unique characters

# dictionary for character-to-index mapping
char_to_index = dict((char, index) for index, char in enumerate(characters))

# dictionary for index-to-character mapping
index_to_char = dict((index, char) for index, char in enumerate(characters))


"""
Create training sequences
"""

# chunk the text into sequences
maxlen = 20  # n
step = 1  # length of step at each iteration

# list of sequences
sequences = []

# list of next characters model should predict
next_characters = []

# iterate over cleaned text string and each 20-length sequence into list
for i in range(0, len(clean) - maxlen, step):
    sequences.append(clean[i : (i + maxlen)])
    next_characters.append(clean[i + maxlen])


"""
Label encode training sequences
(one-hot encoding)
"""

# create empty matrices for input and output sets
# input: each n-length sequence in sequences list
# output: next character after each n-length sequence
# i.e.: sentence = "hello there"
#       sequence = "hel"
#       next char = "l"

x = np.zeros((len(sequences), maxlen, len(characters)), dtype=np.bool)  # input
y = np.zeros((len(sequences), len(characters)), dtype=np.bool)  # output

for i, chunk in enumerate(sequences):
    for j, c in enumerate(chunk):
        x[i, j, char_to_index[c]] = 1
    y[i, char_to_index[next_characters[i]]] = 1
