"""Generates text based on word probabilities in a bigram dictionary."""

import random

def write(bigrams, start, num_words):
    """Returns a new text generated from the bigram dictionary."""
    words = [start]

    current_word = start
    while len(words) < num_words:
        current_word = pick_next_word(bigrams, current_word.lower())
        words.append(current_word)

    return " ".join(words)

def pick_next_word(bigrams, word):
    """Returns a word that follows the given word based on the bigrams."""
    if word not in bigrams:
        return pick_random_word(bigrams)

    return random.choice(bigrams[word])

def pick_random_word(bigrams):
    """Returns a random word from the bigrams dictionary."""
    all_words = list(bigrams.keys())
    return random.choice(all_words)
