"""
In vocabulary and matching identify and label specific 
phrases that match patterns we can define ourselves
"""
# rule-matching tool called Matcher that allows us to build a library of 
# token patterns, then match those patterns against a 
# Doc object to return a list of found matches
import spacy
nlp = spacy.load('en_core_web_sm')
from spacy.matcher import Matcher
matcher = Matcher(nlp.vocab)
# looks for a single token whose lowercase text reads 'solarpower'
pattern1 = [{'LOWER': 'solarpower'}]
# looks for two adjacent tokens that read 'solar' and 'power' in that order
pattern2 = [{'LOWER': 'solar'}, {'LOWER': 'power'}]
# looks for three adjacent tokens, with a middle token that can be any punctuation
pattern3 = [{'LOWER': 'solar'}, {'IS_PUNCT': True}, {'LOWER': 'power'}]
matcher.add('SolarPower', None, pattern1, pattern2, pattern3)

doc = nlp(u'The Solar Power industry continues to grow as demand \
for solarpower increases. Solar-power cars are gaining popularity.')
found_matches = matcher(doc)
print(found_matches)
for match_id, start, end in found_matches:
    string_id = nlp.vocab.strings[match_id]  # get string representation
    span = doc[start:end]                    # get the matched span
    print(match_id, string_id, start, end, span.text)
# Remove the old patterns to avoid duplication:
matcher.remove('SolarPower')
# Redefine the patterns:
pattern1 = [{'LOWER': 'solarpower'}]
pattern2 = [{'LOWER': 'solar'}, {'IS_PUNCT': True, 'OP':'*'}, {'LOWER': 'power'}]
# Add the new set of patterns to the 'SolarPower' matcher:
matcher.add('SolarPower', None, pattern1, pattern2)
found_matches = matcher(doc)
print(found_matches)
# quantifiers can be passed to the 'OP' key
# \!->Negate the pattern, by requiring it to match exactly 0 times
# ?->Make the pattern optional, by allowing it to match 0 or 1 times
# \+->Require the pattern to match 1 or more times
# \*->Allow the pattern to match zero or more times
# Remove the old patterns to avoid duplication:
matcher.remove('SolarPower')
# matching lemmas
pattern1 = [{'LOWER': 'solarpower'}]
pattern2 = [{'LOWER': 'solar'}, {'IS_PUNCT': True, 'OP':'*'}, {'LEMMA': 'powered'}]
# Add the new set of patterns to the 'SolarPower' matcher:
matcher.add('SolarPower', None, pattern1, pattern2)
doc = nlp(u'Solar-powered energy runs solar-powered cars.')
found_matches = matcher(doc)
print(found_matches)
print()
# other tken attributes
# `ORTH`	The exact verbatim text of a token
# `LOWER`	The lowercase form of the token text
# `LENGTH`	The length of the token text
# `IS_ALPHA`, `IS_ASCII`, `IS_DIGIT`	Token text consists of alphanumeric characters, ASCII characters, digits
# `IS_LOWER`, `IS_UPPER`, `IS_TITLE`	Token text is in lowercase, uppercase, titlecase
# `IS_PUNCT`, `IS_SPACE`, `IS_STOP`	Token is punctuation, whitespace, stop word
# `LIKE_NUM`, `LIKE_URL`, `LIKE_EMAIL`	Token text resembles a number, URL, email
# `POS`, `TAG`, `DEP`, `LEMMA`, `SHAPE`	The token's simple and extended part-of-speech tag, dependency label, lemma, shape
# `ENT_TYPE`	The token's entity label

# phrase matcher
# An alternative - and often more efficient - method 
# is to match on terminology lists
from spacy.matcher import PhraseMatcher
matcher = PhraseMatcher(nlp.vocab)
with open('test_files/reaganomics.txt', encoding='cp1252') as f:
    doc = nlp(f.read())

# First, create a list of match phrases:
phrase_list = ['voodoo economics', 'supply-side economics', 'trickle-down economics', 'free-market economics']
# Next, convert each phrase to a Doc object:
phrase_patterns = [nlp(text) for text in phrase_list]
# Pass each Doc object into matcher (note the use of the asterisk!):
matcher.add('VoodooEconomics', None, *phrase_patterns)
# Build a list of matches:
found_matches = matcher(doc)
for match_id, start, end in found_matches:
    string_id = nlp.vocab.strings[match_id]  # get string representation
    span = doc[start:end]                    # get the matched span
    print(match_id, string_id, start, end, span.text)
    print(doc[start-5: end+5])
    print("\n\n")