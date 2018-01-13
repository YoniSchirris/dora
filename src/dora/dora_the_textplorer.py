# Building an algorithm that replaces some words in a given text with the aim of learning the reader a new language

from googletrans import Translator
from nltk import sent_tokenize, word_tokenize
from langdetect import detect as languageDetector
import csv


class Dora:
    def __init__(self, diff, new_lang, text_source):
        self.DICT = Translator()
        self.difficulty = diff
        self.new_lang = new_lang
        self.frequent_words = {}

        if self.source_is_supported(text_source):
            self.base_text = self.text_extractor(text_source)
            self.interchanged_text = "Not yet set"
            self.base_lang = languageDetector("Dit moet een deel van de gegeven tekst zijn. Hoe te bepalen wat? Alles?")
            self.load_frequent_words()
            self.algorithm_one()
        else:
            print("Error should be thrown, instance creation should be cancelled")

    def source_is_supported(self, text_source):
        if text_source[-4:] == ".txt":
            return True
        else:
            return False

    def text_extractor(self, text_source):
        if text_source[-4:] == ".txt":
            with open(text_source, newline='') as inputfile:
                text_list = list()
                for row in csv.reader(inputfile):
                    try:
                        text_list.append(row[0].split(" "))
                    except IndexError:
                        # This happens if there's a line between paragraphs
                        text_list.append(row)
                return text_list

        # Preferably it cancels the whole creation of a class
        else:
            print("We currently don't support any other file formats than a .txt")
            return False

    def algorithm_one(self):
        self.interchanged_text = self.base_text
        for s_idx, sentence in enumerate(self.base_text):
            for w_idx, word in enumerate(sentence):
                if (s_idx + w_idx) % 5 == 0:
                    self.interchanged_text[s_idx][w_idx] = self.DICT.translate(word).text
                    print("IN %r" % sentence)
                    print("%r is replaced by %r" % (word, self.DICT.translate(word, self.new_lang).text))
                    print()

    def load_frequent_words(self):
        with open("frequent_words/words_" + self.base_lang + ".csv") as csvfile:
            self.frequent_words[self.base_lang] = [row[0] for row in csv.reader(csvfile)]
        with open("frequent_words/words_" + self.new_lang + ".csv") as csvfile:
            self.frequent_words[self.new_lang] = [row[0] for row in csv.reader(csvfile)]


if __name__ == "__main__":
    epic_lang_learner = Dora(diff=1, new_lang='en', text_source="test_text/test_nl_1.txt")
    print(epic_lang_learner.base_lang)
    print(epic_lang_learner.base_text)
    print(epic_lang_learner.frequent_words)
    print(epic_lang_learner.interchanged_text)



