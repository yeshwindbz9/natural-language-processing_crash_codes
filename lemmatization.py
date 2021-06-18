"""
    Lemmatization looks beyond word reduction, and considers a language's 
    full vocabulary to apply a morphological analysis to words.
    The lemma of 'was' is 'be' and the lemma of 'mice' is 'mouse'. 
"""
import spacy
nlp = spacy.load('en_core_web_sm')
doc = nlp(u"I am a runner running in a race because I love to run since I ran today")

for token in doc:
    print(f"{token.text:{8}}", '\t', token.pos_, '\t', token.lemma, '\t', token.lemma_)

print()

doc = nlp(u"That's Batman's matte black batmobile")

for token in doc:
    print(f"{token.text:{8}}", '\t', token.pos_, '\t', token.lemma, '\t', token.lemma_)
# We should point out that although lemmatization looks at surrounding text to determine 
# a given word's part of speech, it does not categorize phrases.