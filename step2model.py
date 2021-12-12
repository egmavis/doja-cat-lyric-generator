"""
Using Markov Text Generation 
word-level Lyric Generator
"""

import pandas as pd
from statistics import mode
from collections import defaultdict
import re
import random
import nltk


def build_dict(sentence, corpus, n):
    # sentence_in_progress = sentence
    index = n - 1

    # print(index)
    ngram = sentence[-index:]
    # ngram = sentence_in_progress[-index:]

    # print(ngram)

    dictionary = defaultdict(lambda: 0)
    for i in range(len(corpus)):
        current_window = corpus[i : i + index]
        if current_window == ngram:

            # print(current_window)

            next_word = corpus[i + index]
            # sentence_in_progress.append(next_word)
            dictionary[next_word] += 1
            # ngram = sentence_in_progress[-index:]

            pass
        pass

    # print(dictionary)

    return dictionary


def stupid_backoff(sentence, corpus, n, data, deterministic):

    for i in range(n, 0, -1):
        if data == {} and i > 1:
            data = build_dict(sentence, corpus, i)
            pass
        elif data == {} and i == 1:
            if deterministic:
                data[mode(corpus)] = 1
                pass
            else:
                data[random.choice(corpus)] = 1
                pass
            pass
        pass
    return data


def finish_sentence(sentence, corpus, n, deterministic=False):
    # punctuation = [".", "!", "?"]
    while len(sentence) < 100:  # and sentence[-1] not in punctuation:
        data = build_dict(sentence, corpus, n)
        if data == {}:
            data = stupid_backoff(sentence, corpus, n, data, deterministic)
            pass
        if deterministic:
            next_word = max(data, key=lambda x: data[x])
            sentence.append(next_word)
            pass
        else:
            next_word = random.choice(list(data.keys()))
            sentence.append(next_word)
            pass
    sentence.append(".")
    return " ".join(sentence)


def main():
    sentence = ["u", "go", "to", "town", "go", "down"]
    n = 20
    songs = pd.read_csv("~/703/doja-cat-lyric-generator/doj_songs.csv")

    # Tokenize Data

    # merge all characters into one string
    clean = ""
    for line in songs["lyrics"]:
        clean = clean + " ".join(re.findall(r"[a-z']+", line))

    corpus = nltk.word_tokenize(clean)
    # print(corpus)

    flag = True

    print(finish_sentence(sentence, corpus, n, flag))


if __name__ == "__main__":
    main()
