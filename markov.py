"""Generate Markov text from text files."""

from random import choice
import sys


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    # your code goes here

    text_file = open(file_path)

    # for text in text_file:
    #     strip_text = text.rstrip()

    text = text_file.read()

    text_file.close()

    return text


def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains("hi there mary hi there juanita")

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

    # your code goes here

    text_list = text_string.split()

    for idx in range(len(text_list) - 2):
        key = (text_list[idx], text_list[idx + 1])

        following_word = text_list[idx + 2]

        # current_value = chains.get(key, []) + [following_word]

        # current_value = chains.get(key, [])
        # current_value.append("hi") -- edits first list in place

        # chains[key] = current_value

        chains[key] = chains.get(key, []) + [following_word] #makes a new list every time

    return chains


def make_text(chains):
    """Return text from chains."""

    words = []
    chain_keys = []
    # your code goes here
    for key in chains.keys():
        if key[0][0] == key[0][0].upper():
            chain_keys.append(key)

    first = choice(list(chain_keys))
    words += list(first)

    # random_value = choice(chains[first])
    # words.append(random_value)

    while True:

        try:
            current_key = chains[(words[-2], words[-1])]
            random_word = choice(current_key)
            words.append(random_word)

        except KeyError:
            break

    return " ".join(words)

filename = sys.argv[1] #runs argv file in terminal

input_path = filename

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)
