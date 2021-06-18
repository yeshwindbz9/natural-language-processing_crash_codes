"""
    Sentiment analysis studies the subjective information in an expression, 
    that is, the opinions, appraisals, emotions, or 
    attitudes towards a topic, person or entity. 
    Expressions can be classified as positive, negative, or neutral. 
    For example: “I really like the new design of your website!” → Positive
"""
# vector arithmetic
# Import spaCy and load the language library. Remember to use a larger model!
import spacy
nlp = spacy.load("en_core_web_md")
# Choose the words you wish to compare, and obtain their vectors
king = nlp.vocab["king"].vector
man = nlp.vocab['man'].vector
woman = nlp.vocab['woman'].vector
# Import spatial and define a cosine_similarity function
from scipy import spatial
cosine_similarity = lambda x, y: 1 - spatial.distance.cosine(x, y)
# Write an expression for vector arithmetic
# For example: new_vector = word1 - word2 + word3
new_vector = king - man + woman
# List the top ten closest vectors in the vocabulary to the result of the expression above
computed_similarities = []

for word in nlp.vocab:
    # Ignore words without vectors and mixed-case words:
    if word.has_vector:
        if word.is_alpha:
            similarity = cosine_similarity(new_vector, word.vector)
            computed_similarities.append((word, similarity))
# sorting with highest to lowest similarity
computed_similarities = sorted(computed_similarities, key=lambda item: -item[1])
print([w[0].text for w in computed_similarities[:10]])
# a function that takes in 3 strings, performs a-b+c arithmetic, and returns a top-ten result
def vector_math(a,b,c):
    # define a cosine_similarity function
    cosine_similarity = lambda x, y: 1 - spatial.distance.cosine(x, y)
    a_vector = nlp.vocab[f"{a}"].vector
    b_vector = nlp.vocab[f"{b}"].vector
    c_vector = nlp.vocab[f"{c}"].vector
    # expression for vector arithmetic
    new_vector = a_vector - b_vector + c_vector
    # List the top ten closest vectors in the vocabulary to the result of the expression above
    computed_similarities = []

    for word in nlp.vocab:
        # Ignore words without vectors and mixed-case words:
        if word.has_vector:
            if word.is_alpha:
                similarity = cosine_similarity(new_vector, word.vector)
                computed_similarities.append((word, similarity))
    # sorting with highest to lowest similarity
    computed_similarities = sorted(computed_similarities, key=lambda item: -item[1])
    print([w[0].text for w in computed_similarities[:10]])
# Test the function on known words:
vector_math('king','man','woman')
print("-------------------------------------------")
# VADER Sentiment Analysis on a review
# import nltk and download the vader lexicon
import nltk
nltk.download("vader_lexicon")
# Import SentimentIntensityAnalyzer and create an sid object
from nltk.sentiment.vader import SentimentIntensityAnalyzer
sid = SentimentIntensityAnalyzer()
# Write a review as one continuous string (multiple sentences are ok)
review = """This was my first switch to an ios device after using an android untill now. And I am not disappointed. The build quality, the responsive touch, the display, the camera, the battery life are just exceptional.
Been using for about 10 days now, and consistently giving around 7h of screen on time.
The camera is just way too good. Espeecially the night mode impressed me a lot.
Only issue when switching from Android to iPhone I encountered was to be not able to restore my whatsapp chats. There are no official/free ways for doing this.
The phone is simple amazing."""
# Obtain the sid scores for your review
print(sid.polarity_scores(review))
print("-------------------------------------------")
# a function that takes in a review and returns a score of "Positive", "Negative" or "Neutral"
def review_rating(string):
    sid = SentimentIntensityAnalyzer()
    reviewScore = sid.polarity_scores(review)["compound"]
    if reviewScore > 0:
        return "Positive"
    elif reviewScore < 0:
        return "Negetive"
    else:
        return "Neutral"
# Test the function on your review above:
print("predicting sentiment for the review\n")
print(review)
print()
print(review_rating(review))