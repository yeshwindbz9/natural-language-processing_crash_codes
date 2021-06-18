"""
 Natural language processing is an area of CS & AI
 that focuses on the interactions between 
 computers and human language particularly in
 analyzing and processing the natural language
 text data is unstructed and needs to be processed 
 NLP uses a variety of techniques to create structure out of text data

"""
#spacyBasics
# Set-ExecutionPolicy RemoteSigned
# nlp() func from spacy takes raw text and performs 
# a series of ops like tagging, parsing and describe the text data
# eg tokenization, pos, stemming and lemmatization
import spacy
# use `conda install -c conda-forge spacy` to install
nlp = spacy.load('en_core_web_sm')
# use `python -m spacy download en` to install model
# create a doc object
doc = nlp(u"The only problem with a pencil, is that they do not stay sharp long enough.")
# printing each token
for token in doc:
    print(token.text, token.pos_, token.dep_)
print()
print(nlp.pipeline)
print(nlp.pipe_names)
print()
# tokenization
doc = nlp(u"The only problem with a pencil, is that they do not stay sharp long enough.")
print(doc)
print("first token: ", doc[0], "type of token: ", type(doc))
# pos
print("pos of first token: ", doc[0].pos_)
# dependencies
print("dependency of first token: ", doc[0].dep_)
# to see the full name of a tag use spacy.explain(tag)
print("propn: ", spacy.explain('PROPN'))
# additional token attributes
"""
    .text->The original word text
    .lemma_->The base form of the word
    .pos_->The simple part-of-speech tag
    .tag_->The detailed part-of-speech tag
    .shape_->The word shape – capitalization, punctuation, digits
    .is_alpha->Is the token an alpha character?
    .is_stop->Is the token part of a stop list, i.e. the most common words of the language?

"""
# lemma
print("text: ", doc[3], "lemma: ", doc[3])
# pos and detailed
print("pos: ", doc[4].pos_)
print(doc[4].tag_ + ' / ' + spacy.explain(doc[4].tag_))
# Word Shapes:
print(doc[0].text+': '+doc[0].shape_)
print(doc[5].text+' : '+doc[5].shape_)
# Boolean Values:
print("alpha: ", doc[0].is_alpha)
print("stop words: ", doc[0].is_stop)
print()
# spans
# span is a slice of Doc object in the form Doc[start:stop].
doc = nlp(u'Although commmonly attributed to John Lennon from his song "Beautiful Boy", \
the phrase "Life is what happens to us while we are making other plans" was written by \
cartoonist Allen Saunders and published in Reader\'s Digest in 1957, when Lennon was 17.')
life_quote = doc[16:30]
print(life_quote)
print(type(life_quote))
print()
# sentences
doc = nlp(u'This is the first sentence. This is another sentence. This is the last sentence.')
for sent in doc.sents:
    print(sent)
    
print(doc[6].is_sent_start)