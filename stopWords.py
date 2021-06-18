"""
    Words like "a" and "the" appear so frequently that they 
    don't require tagging as thoroughly as nouns, verbs and modifiers. 
    We call these stop words, and they can be filtered from the text to be processed. 
    spaCy holds a built-in list of some 305 English stop words.
"""
import spacy
nlp = spacy.load('en_core_web_sm')
print("num of stop words: ", len(nlp.Defaults.stop_words))
# to check for stop words
print("myself is stopword?: ", nlp.vocab['myself'].is_stop)
print("mystry is stopword?: ",nlp.vocab['mystery'].is_stop)
# Add the word to the set of stop words. Use lowercase!
nlp.Defaults.stop_words.add('btw')
# Set the stop_word tag on the lexeme
nlp.vocab['btw'].is_stop = True
print("btw is stopword?: ", nlp.vocab['btw'].is_stop)
print("num of stop words: ", len(nlp.Defaults.stop_words))
# Remove the word from the set of stop words
nlp.Defaults.stop_words.remove('beyond')
# Remove the stop_word tag from the lexeme
nlp.vocab['beyond'].is_stop = False
print("beyond is stopword?: ", nlp.vocab['beyond'].is_stop)
print("num of stop words: ", len(nlp.Defaults.stop_words))
# all stopwords
print()
print(nlp.Defaults.stop_words)