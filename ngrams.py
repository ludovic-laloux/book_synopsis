"""
Identifies bigrams in a dataset of texts.

Bigrams represent consecutive words in a sequence. For example, in the sentence
"I think I can.", the words "think" and "can" follow the word "I".

Bigrams are packaged in a data structure of the following form:
{"i": ["think", "can"], "think": ["I"], "can.": [""]}
"""

def collect_from_dataset(texts):
    """Returns a dictionary of the bigrams in all of the given texts."""
    # Considers all texts as one, which makes some false bigrams across texts.
    all_texts_string = " ".join(texts)
    return collect_from_words(all_texts_string.split())

def collect_from_words(words):
    """Returns a bigram dictionary of word to list of words that follow it."""
    bigrams = {}

    for i in range(len(words)):
        # Use lowercase keys so all forms of the word are equal.
        word = words[i].lower()

        if word not in bigrams:
            bigrams[word] = []

        # Preserve capitalization in the values.
        bigrams[word].append(get_next_word(words, i))

    return bigrams

def get_next_word(words, index):
    """Returns the word in the text that comes after the given index."""
    if index + 1 >= len(words):
        # If it's the last word, signal a stop with the empty string.
        return ""

    return words[index + 1]
