import spacy

nlp = spacy.load('en')
doc = nlp(u'Hello, world. Here are two sentences. C:/users/documents')

for token in doc:
    print(token.text, token.lemma_, token.pos_, token.tag_, token.dep_,
          token.shape_, token.is_alpha, token.is_stop)