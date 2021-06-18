"""
    Text classification also known as text tagging or text categorization is 
    the process of categorizing text into organized groups. 
    By using Natural Language Processing (NLP), text classifiers can 
    automatically analyze text and then assign a set of pre-defined tags or 
    categories based on its content.
"""
# Perform imports and 
# load the dataset into a pandas DataFrame
import pandas as pd
df = pd.read_csv("test_files/moviereviews.tsv", sep="\t")
print(df.head())
print("--------------------------")
# Check for NaN values:
print(df.isnull().sum())
print("--------------------------")
# Check for whitespace strings
blanks = []
for i, lb, rv in df.itertuples():
    if type(rv) == str:
        if rv.isspace():
            blanks.append(i)
# Remove NaN values
df.dropna(inplace=True)
# quick look at the label column
print(df['label'].value_counts())
# Split the data into train & test sets
from sklearn.model_selection import train_test_split
X = df['review']
y = df['label']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)
# Build a pipeline to vectorize the date, then train and fit a model
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC
text_clf = Pipeline([('tfidf', TfidfVectorizer()), ('clf', LinearSVC())])
text_clf.fit(X_train, y_train)
# Form a prediction set
predictions = text_clf.predict(X_test)
print("--------------------------")
# Report the confusion matrix
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score
print(confusion_matrix(y_test, predictions))
# Print a classification report
print(classification_report(y_test, predictions))
# Print the overall accuracy
print(accuracy_score(y_test, predictions))