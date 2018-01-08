# Building an algorithm that replaces some words in a given text with the aim of learning the reader a new language

from PyDictionary import PyDictionary
from langdetect import detect as languageDetector
import csv

dictionary = PyDictionary()


class Dora:
    # set up Dora with a difficulty level to initialize certain algorithms?

    def __init__(self, diff, new_lang, text_source):
        self.DICT = PyDictionary()
        self.difficulty = diff
        self.new_lang = new_lang
        self.frequent_words = {}

        if self.text_extractor(text_source):
            self.base_text = self.text_extractor(text_source)
            self.interchanged_text = "Not yet set"

            # LanguageDetector requires a string
            self.base_lang = languageDetector("Dit is gewoon even een test")
            self.load_frequent_words()

        else:
            print("Error should be thrown, instance creation should be cancelled")




    def text_extractor(self, text_source):
        # Currently merely checks if it's a .txt. This should have an advanced method that checks for every possible
        # file, especially .epub files and extract the right string / list from it

        if text_source[-4:] == ".txt":
            with open(text_source, newline='') as inputfile:
                # Not entirely sure yet how we should have the data structured.
                # Guess it should be per book, per chapter, per page, per sentence, per word
                # Guess we also need it in different formats for different function. So maybe we need to define a new
                # class that holds BookText.asString and BookText.asEpub and BookText...... and whatever we need
                # {book:
                #   chapter_one:
                #        page_one:
                #           sentence_one:
                #               word_one:
                #           sentence_two:
                #               word_one:
                #               word_two:
                #        page_two:
                #           ...
                #   chapter_two:
                #       ...
                # }
                #
                # With some numerical identifier, so that we can also easily save which words we've replaced and which
                # ID they have.
                #
                return list(csv.reader(inputfile))

        # This
        else:
            print("We currently don't support any other file formats than a .txt")
            return False

    def algorithm_one(self):



        self.interchanged_text = "Now set"

        # sets the interchanged text, hurray
        # should also save all statistics. How many words replaced? Count of all replaced words

    def load_frequent_words(self):
        with open("frequent_words/words_" + self.base_lang + ".csv") as csvfile:
            self.frequent_words[self.base_lang] = [row[0] for row in csv.reader(csvfile)]
        with open("frequent_words/words_" + self.new_lang + ".csv") as csvfile:
            self.frequent_words[self.new_lang] = [row[0] for row in csv.reader(csvfile)]







epic_lang_learner = Dora(diff=1, new_lang='en', text_source="test_text/test_nl_1.txt")
print(epic_lang_learner.base_lang)
print(epic_lang_learner.base_text)
print(epic_lang_learner.frequent_words)




