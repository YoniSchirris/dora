from nltk import sent_tokenize, word_tokenize
import nltk

nltk.download()



example_text = "This is an example. Mr. Robertson has a mustache."

print(sent_tokenize(example_text))

print(word_tokenize(example_text))



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