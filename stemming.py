# stemming is a method for cataloging related words
# porters stemmer
# the algorithm employs five phases of word reduction, each with its own set of mapping rules.
import nltk
from nltk.stem.porter import PorterStemmer
p_stemmer = PorterStemmer()
words = ["run", "runner", "ran", "runs", "easily", "fairly", "generous", "generously", "generate"]
for word in words:
    print(word+"-->"+p_stemmer.stem(word))
print()

# snowball stemmer
# offers a slight improvement over the original Porter stemmer, both in logic and speed
from nltk.stem.snowball import SnowballStemmer
s_stemmer = SnowballStemmer(language="english")
for word in words:
    print(word+"-->"+s_stemmer.stem(word))