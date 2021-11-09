import nltk
from nltk.corpus import stopwords
from collections import Counter
import math


class PreProcess:
    def __init__(self, data="this is default string", dt="text"):
        self.dt = dt
        self.data = data

    def remove_stopwords_text(self, text=None):
        """
        Removes stopwords from text. Given that data is of text type within instance
        or passed parameter.
        """
        if text is None:
            if(self.dt == "text"):
                text = self.data
            else:
                print("No text to remove stopwords")
        text = text.lower()
        sword = stopwords.words('english')
        text = [word for word in text.split(" ") if word not in sword]
        return " ".join(text)

    def get_word_frequency(self, text=None):
        """
        Returns a dictionary of word frequency.
        """
        if text is None:
            if(self.dt == "text"):
                text = self.data
            else:
                print("No text to get word frequency")
        text = text.lower()
        text = text.replace(".", " ")
        text = text.split(" ")
        text = [word for word in text if word != ""]

        freq = Counter(text)
        return freq

    def tfIdf_score(self, sentence, corpus_freq):
        """
        Returns a tf-idf score for a sentence.
        """
        sentence = sentence.lower()
        sentence = sentence.replace(".", " ")
        sentence = sentence.split(" ")
        sentence = [word for word in sentence if word != ""]

        freq = Counter(sentence)
        score = 0
        total_words = len(sentence)
        for word in freq:
            # Using a modified version... idf is probability word/#word in corpus
            score += freq[word]/total_words * (freq[word] / corpus_freq[word])
        return score
