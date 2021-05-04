"""Generate Markov text from text files."""

import random
from random import choice


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    # your code goes here
    contents = open(file_path).read()
    return contents


def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains('hi there mary hi there juanita')

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']

        >>> chains[('there','juanita')]
        [None]
    """
    chains = {}
    word_list = text_string.split()
    # loop through text_string:
    for i in range(len(word_list)-2):
        if chains.get((word_list[i], word_list[i+1]), 0) == 0:
            chains[(word_list[i], word_list[i+1])] = []
        chains[(word_list[i], word_list[i+1])].append(word_list[i+2])
    
    #   add word pairs to dictionary keys
    #   add next word(value) to keys
    for items in chains.items():
        print(items)
    # print(chains)
    return chains


def make_text(chains):
    """Return text from chains."""

    words = []

    #1) create a new key by indexing into the previous tuple and choosing a random word for the item list
    #   new_key = (previous_tuple[1], random.choice(item list of previous tuple))
    #   for loop
    for key, value in chains.items():
        words.append(key[0])
        words.append(random.choice(value))
        words.append(key[1])
        if chains.get((words[-2], words[-1]), 0):
            words.append(random.choice(chains.get((words[-2], words[-1]), 0)))

    return ' '.join(words)

input_path = 'green-eggs.txt'

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)
