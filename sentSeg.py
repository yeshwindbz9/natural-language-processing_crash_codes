# sentence segmentation
# Perform standard imports
import spacy
nlp = spacy.load('en_core_web_sm')
# From Spacy Basics:
doc = nlp(u'This is the first sentence. This is another sentence. This is the last sentence.')
for sent in doc.sents:
    print(sent)
print("-----------------")
# doc.sents is a generator. That is, a Doc is not 
# segmented until doc.sents is called
# building a sentence collection by running doc.sents
doc_sents = [sent for sent in doc.sents]
print(doc_sents)
# sents are Spans
print(type(doc_sents[1]))
print("-----------------")
# checking if a token is a sentence starter
# Parsing the segmentation start tokens happens during the nlp pipeline
doc = nlp(u'This is a sentence. This is a sentence. This is a sentence.')
for token in doc:
    print(token.is_sent_start, ' '+token.text)
print("-----------------")
# adding a semicolon to our existing segmentation rules
# default behaviour
doc = nlp(u'"Management is doing things right; leadership is doing the right things." -Peter Drucker')
for sent in doc.sents:
    print(sent)
# adding a new rule to the pipeline
def set_custom_boundaries(doc):
    for token in doc[:-1]:
        if token.text == ';':
            doc[token.i+1].is_sent_start = True
    return doc
nlp.add_pipe(set_custom_boundaries, before='parser')
print(nlp.pipe_names)
print("-----------------")
# changing the rules
# reloading library
nlp = spacy.load('en_core_web_sm')
mystring = u"This is a sentence. This is another.\n\nThis is a \nthird sentence."
doc = nlp(mystring)
print("deafult repr \n",mystring)
print("\ndoc repr\n")
for sent in doc.sents:
    print(sent)
for sent in doc.sents:
    print([token.text for token in sent])
print("-----------------")
# changing rules
from spacy.pipeline import SentenceSegmenter
def split_on_newlines(doc):
    start = 0
    seen_newline = False
    for word in doc:
        if seen_newline:
            yield doc[start:word.i]
            start = word.i
            seen_newline = False
        elif word.text.startswith('\n'): # handles multiple occurrences
            seen_newline = True
    yield doc[start:]      # handles the last group of tokens
sbd = SentenceSegmenter(nlp.vocab, strategy=split_on_newlines)
nlp.add_pipe(sbd)
# it's important to use the name sbd for the SentenceSegmenter
doc = nlp(mystring)
for sent in doc.sents:
    print([token.text for token in sent])