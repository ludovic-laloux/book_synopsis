import corpus
import ngrams
import text_generation

dataset = corpus.book_summaries
starting_words = ["A", "The", "When"]
word_count = 40

bigrams = ngrams.collect_from_dataset(dataset)

# Seed each book summary with a common starting word.
for word in starting_words:
    new_text = text_generation.write(bigrams, word, word_count)
    print(new_text + "\n")
