# Building an algorithm that replaces some words in a given text with the aim of learning the reader a new language
import operator

from googletrans import Translator
from nltk import sent_tokenize, word_tokenize
from langdetect import detect as languageDetector
import csv
import spacy


class Dora:

    def __init__(self, difficulty, new_lang, text_source):
        self.DICT = Translator()
        self.difficulty = difficulty
        self.new_lang = new_lang
        self.frequent_words = {}
        self.swiper = Swiper()

        if self.source_is_supported(text_source):
            self.base_text = self.text_extractor(text_source)
            self.base_text = self.swiper.sweep(self.base_text)
            self.interchanged_text = "Not yet set"
            self.base_lang = languageDetector(self.base_text)
            self.load_frequent_words()
            self.algorithm_one()
        else:
            print("Error should be thrown, instance creation should be cancelled")

    def source_is_supported(self, text_source):
        if text_source[-4:] == ".txt":
            return True
        else:
            return False

    @staticmethod
    def text_extractor(text_source):
        if text_source[-4:] == ".txt":
            return open(text_source).read()

        # Preferably it cancels the whole creation of a class
        else:
            print("We currently don't support any other file formats than a .txt")
            return False

    def algorithm_one(self):

        occurrence_limit = 5

        nlp = spacy.load(self.base_lang)
        doc = nlp(self.base_text)

        words_we_care_about = {}

        word_types_we_care_about = ["NOUN", "VERB"]

        for word_type in word_types_we_care_about:
            words_we_care_about[word_type] = list()

        # accumulate by word type
        for token in doc:
            print(token, token.pos_)
            if token.pos_ in word_types_we_care_about:
                words_we_care_about[token.pos_].append(token)

        only_text_from_tokens_for_freq = []
        for token in words_we_care_about["NOUN"]:
            only_text_from_tokens_for_freq.append(token.text)


        # count
        noun_freq = {i: only_text_from_tokens_for_freq.count(i) for i in set(only_text_from_tokens_for_freq)}

        sorted_noun_freq = sorted(noun_freq.items(), key=operator.itemgetter(1), reverse=True)

        most_frequent_nouns = [k for k, v in sorted_noun_freq if v > occurrence_limit]

        # TODO
        # for noun in most_frequent_nouns:
        #     loop through doc
        #     if occurrence > limit and occurrence_on_page > 1:
        #         current_pos_in_book = translate(previous_word)


    def load_frequent_words(self):
        with open("../resources/frequent_words/words_" + self.base_lang + ".csv") as csvfile:
            self.frequent_words[self.base_lang] = [row[0] for row in csv.reader(csvfile)]
        with open("../resources/frequent_words/words_" + self.new_lang + ".csv") as csvfile:
            self.frequent_words[self.new_lang] = [row[0] for row in csv.reader(csvfile)]


#TODO Place Swiper in a separate python file and import
class Swiper:
    """
    Swiper, go sweeping!
    Swiper, go sweeping!!
    Swiper, go sweeping!!!

    And finally, swiper DOES sweep, and he sweeps the given string from its dirty characters
    """

    def __init__(self):
        self.tit_for_tat = [
            ["`", "'"]
        ]

    def sweep(self, dirty_text):
        if type(dirty_text) == str:
            clean_text = dirty_text

            for replacements in self.tit_for_tat:
                clean_text = clean_text.replace(replacements[0], replacements[1])
            return clean_text
        else:
            print("Can only handle a pure string for now")
            print("Please hand me a string)")


if __name__ == "__main__":
    epic_lang_learner = Dora(difficulty=1, new_lang='nl', text_source="../resources/input_text_files/alice_chap1.txt")





