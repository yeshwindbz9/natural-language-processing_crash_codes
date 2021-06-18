# ner is an abbreviation for named entity recognition
# spaCy has an 'ner' pipeline component that identifies 
# token spans fitting a predetermined set of named entities.
# ner locates and classifies named entities in unstructured text
# into predefined categories like time, values, locations, oragizations, etc
# Perform standard imports
import spacy
nlp = spacy.load('en_core_web_sm')
# Write a function to display basic entity info:
def show_ents(doc):
    if doc.ents:
        for ent in doc.ents:
            print(ent.text+' - '+ent.label_+' - '+str(spacy.explain(ent.label_)))
    else:
        print('No named entities found.')

doc = nlp(u'May I go to Washington, DC next May to see the Washington Monument?')
show_ents(doc)
print()
# demostrating other named entity annotations
doc = nlp(u'Can I please borrow 500 dollars from you to buy some Microsoft stock?')
for ent in doc.ents:
    print(ent.text, ent.start, ent.end, ent.start_char, ent.end_char, ent.label_)
print()
# creating our own entity
doc = nlp(u'Tesla to build a U.K. factory for $6 million')
show_ents(doc)
# here, Tesla is not recognized as an entity
from spacy.tokens import Span
# Get the hash value of the ORG entity label
ORG = doc.vocab.strings[u'ORG']
# Create a Span for the new entity
# doc - the name of the Doc object
# 0 - the start index position of the span
# 1 - the stop index position (exclusive)
# label=ORG - the label assigned to our entity
new_ent = Span(doc, 0, 1, label=ORG)
# Add the entity to the existing Doc object
doc.ents = list(doc.ents) + [new_ent]
print(show_ents(doc))
print("-----------------------------")
# what if we want to tag all occurences of Tesla?
# how to use the PhraseMatcher to 
# identify a series of spans in the Doc:
doc = nlp(u'Our company plans to introduce a new vacuum cleaner. '
          u'If successful, the vacuum cleaner will be our first product.')
show_ents(doc)
# Import PhraseMatcher and create a matcher object:
from spacy.matcher import PhraseMatcher
matcher = PhraseMatcher(nlp.vocab)
# Create the desired phrase patterns:
phrase_list = ['vacuum cleaner', 'vacuum-cleaner']
phrase_patterns = [nlp(text) for text in phrase_list]
# Apply the patterns to our matcher object:
matcher.add('newproduct', None, *phrase_patterns)
# Apply the matcher to our Doc object:
matches = matcher(doc)
# See what matches occur:
print(matches)
print()
# Here we create Spans from each match, and create named entities from them:
from spacy.tokens import Span
PROD = doc.vocab.strings[u'PRODUCT']
new_ents = [Span(doc, match[1],match[2],label=PROD) for match in matches]
doc.ents = list(doc.ents) + new_ents
print(show_ents(doc))
print()
# counting entities
doc = nlp(u'Originally priced at $29.50, the sweater was marked down to five dollars.')
show_ents(doc)
# looking for all entities
print(len([ent for ent in doc.ents]))
# looking for entities related to money
len([ent for ent in doc.ents if ent.label_=='MONEY'])
print()
# visualizing named entities
# Import the displaCy library
from spacy import displacy
doc = nlp(u'Over the last quarter Apple sold nearly 20 thousand iPods for a profit of $6 million. '
         u'By contrast, Sony sold only 7 thousand Walkman music players.')
displacy.serve(doc, style='ent')
# to view specific entities
options = {'ents': ['ORG', 'PRODUCT']}
displacy.serve(doc, style='ent', options=options)