from collections import Counter
def wordFreq(book, word):
    """
    Count the frequency of a word in a book
    :param book:
    :param word:
    :return:
    """
    freq = Counter(book)
    return freq[word]
