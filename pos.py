# pos is an abbreviation for parts of speech
# pos tages include noun, verb, adjective etc
# and fine grained tags like plural noun, past tense verb and superlative adjective
import spacy
nlp = spacy.load('en_core_web_sm')
doc = nlp(u"The quick brown fox jumped over the lazy dog's back.")

# To view the coarse POS tag use token.pos_
# To view the fine-grained tag use token.tag_
# To view the description of either type of tag use spacy.explain(tag)
print(doc.text)
# Print the associated tags:
for token in doc:
    print(f'{token.text:{10}} {token.pos_:{8}} {token.tag_:{6}} {spacy.explain(token.tag_)}')
# pos_ gives coarse-grained pos
# tag_ gives fine-grained pos
# explain gives description of either type of tag
print("-------------------------------------")
# the same string of characters can have different meanings, 
# even within the same sentence.
# note the fine-grained pos
doc = nlp(u'I read books on NLP.')
print(doc.text)
r = doc[1]
print(f'{r.text:{10}} {r.pos_:{8}} {r.tag_:{6}} {spacy.explain(r.tag_)}')
print()
doc = nlp(u'I read a book on NLP.')
print(doc.text)
r = doc[1]
print(f'{r.text:{10}} {r.pos_:{8}} {r.tag_:{6}} {spacy.explain(r.tag_)}')
print("--------------------------")
# we can count the pos tags in a doc
doc = nlp(u"The quick brown fox jumped over the lazy dog's back.")

# Count the frequencies of different coarse-grained POS tags:
# doc.vocab[80].text give the str repr of the tag
POS_counts = doc.count_by(spacy.attrs.POS)
for k,v in sorted(POS_counts.items()):
    print(f'{k}. {doc.vocab[k].text:{5}}: {v}')
print()
# Count the different fine-grained tags:
# doc.vocab[80].text give the str repr of the tag
TAG_counts = doc.count_by(spacy.attrs.TAG)
for k,v in sorted(TAG_counts.items()):
    print(f'{k}. {doc.vocab[k].text:{4}}: {v}')
print()
# Count the different dependencies:
DEP_counts = doc.count_by(spacy.attrs.DEP)
for k,v in sorted(DEP_counts.items()):
    print(f'{k}. {doc.vocab[k].text:{4}}: {v}')

# Import the displaCy library to visualize pos
from spacy import displacy
# Create a simple Doc object
doc = nlp(u"The quick brown fox jumped over the lazy dog's back.")
# Render the dependency parse
displacy.serve(doc, style='dep', options = {
    'distance': 110, 
    'compact': 'True', 
    'color': 'yellow', 
    'bg': '#09a3d5', 
    'font': 'Times'
    })
for token in doc:
    print(f'{token.text:{10}} {token.pos_:{7}} {token.dep_:{7}} {spacy.explain(token.dep_)}')