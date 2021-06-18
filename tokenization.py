"""

    Tokenization is the process of breaking up the original text
    into component pieces called tokens.
    eg: 'We're moving to L.A.!'->[We, 're, moving, to, L.A., !]
    They are the basic building blocks of doc
    elements in tokens: prefix, infix, suffix & exception
    example of tokens: $, -, km, U.S.

"""
import spacy
nlp = spacy.load('en_core_web_sm')
sent = nlp(u"We're moving to L.A.!")
print(sent)
print()
# to count the num of tokens check len
print(len(sent), len(sent.vocab))
sentLst = [token.text for token in sent]
print(sentLst)
print()
# named entities
sent = nlp(u"An Apple a day keeps the doctor away!")
sentLst = [
    (entity, entity.label_, str(spacy.explain(entity.label_))) 
    for entity in sent.ents
    ]
print(sentLst)
print()
# noun chunks
sent = nlp(u"Mary had a little lamb!")
sentLst = [chunk for chunk in sent.noun_chunks]
print(sentLst)
print()
# visualization
from spacy import displacy
doc = nlp(u"Apple is going to build a park for $10 million")
# for visualizing dependencies
displacy.render(doc, style="dep", options={"distance": 50})
# for visualizing entities
displacy.serve(doc, style="ent")