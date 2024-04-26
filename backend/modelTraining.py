import pandas as pd
import numpy as np
import nltk
import json
import string
import re
import sklearn
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem.porter import PorterStemmer
from nltk.stem import WordNetLemmatizer

from sklearn.feature_extraction.text import TfidfVectorizer

from sklearn import svm

import pickle

def remove_special_characters(text):
    pattern = r'[^a-zA-Z\s]'
    cleaned_text = re.sub(pattern, '', text)

    return cleaned_text

def remove_punctuation(text):
    translator = str.maketrans('', '', string.punctuation)
    return text.translate(translator)

# remove whitespace
def remove_whitespace(text):
    return " ".join(text.split())


# remove keyfault stopwords

def remove_stopwords(text):
    stop_words = set(stopwords.words("english"))
    word_tokens = word_tokenize(text)
    filtered_text = [word for word in word_tokens if word not in stop_words]
    return filtered_text

# Stemming

stemmer = PorterStemmer()

def stem_words(text):
    word_tokens = word_tokenize(text)
    stems = [stemmer.stem(word) for word in word_tokens]
    return stems

# Lemmatization
lemmatizer = WordNetLemmatizer

def lemma_words(text):
    word_tokens = word_tokenize(text)
    lemmatized_words = [lemmatizer.lemmatize(word) for word in text]
    return lemmatized_words

#if __name__ == '__main__':
def trainModel():
    tech_data = pd.read_csv("models/jobs.csv - trainingv2BDBUFF.csv") #change this file for tech/notech training
    notech_data = pd.read_csv("models/jobs.csv - why.csv") #change this file for classification

    tech_training = pd.DataFrame(tech_data[['jobtitle', 'jobdescription', 'tag']])
    notech_training = pd.DataFrame(notech_data[['jobtitle', 'jobdescription','tech']])

    tech_training = tech_training.dropna()
    tech_training = tech_training.reindex()

    notech_training = notech_training.dropna()
    notech_training = notech_training.reindex()

    # Data Preprocessing
    tech_training = tech_training.applymap(lambda x: x.lower() if isinstance(x, str) else x)
    notech_training = notech_training.applymap(lambda x: x.lower() if isinstance(x, str) else x)

    notech_training

    old_word = r'\bit\b'


    # This is to avoid the stopwords function from removing It since it reads it as "it"
    tech_training['tag'] = tech_training['tag'].str.replace(old_word, 'information_technology', regex=True)
    notech_training['tech'] = notech_training['tech'].str.replace("no", 'no_tech', regex=True)

    # Removes special characters
    

    tech_training = tech_training.applymap(lambda x: remove_special_characters(x) if isinstance(x, str) else x)
    tech_training = tech_training.applymap(lambda x: remove_punctuation (x) if isinstance(x, str) else x)
    tech_training = tech_training.applymap(lambda x: remove_whitespace(x) if isinstance(x, str) else x)
    tech_training = tech_training.applymap(lambda x: remove_stopwords(x) if isinstance(x, str) else x)
    tech_training = tech_training.applymap(lambda x: stem_words(x) if isinstance(x, str) else x)
    #tech_training = tech_training.applymap(lambda x: lemma_words(x) if isinstance(x, str) else x)

    notech_training = notech_training.applymap(lambda x: remove_special_characters(x) if isinstance(x, str) else x)
    notech_training = notech_training.applymap(lambda x: remove_punctuation (x) if isinstance(x, str) else x)
    notech_training = notech_training.applymap(lambda x: remove_whitespace(x) if isinstance(x, str) else x)
    notech_training = notech_training.applymap(lambda x: remove_stopwords(x) if isinstance(x, str) else x)
    notech_training = notech_training.applymap(lambda x: stem_words(x) if isinstance(x, str) else x)
    #notech_training = notech_training.applymap(lambda x: lemma_words(x) if isinstance(x, str) else x)

    # Combining both job title and job description
    tech_training['combined'] = tech_training['jobtitle'] + tech_training['jobdescription']

    notech_training['combined'] = notech_training['jobtitle'] + notech_training['jobdescription']

    #print(tech_training[tech_training['tag'] == "architect"])
    print(tech_training['tag'])

    #tech_training = tech_training[tech_training["tag"] != "non_tech"]

    #notech = tech_training[tech_training["tag"] != "non_tech"]

    #print(str(notech['tag'] == "architect"))


    X = tech_training['combined'].apply(lambda x:x[0])
    y = tech_training['tag'].apply(lambda x:x[0])

    mlb = sklearn.preprocessing.MultiLabelBinarizer()
    lb = sklearn.preprocessing.LabelBinarizer()

    Xn = notech_training['combined'].apply(lambda x:x[0])
    yn = notech_training['tech'].apply(lambda x:x[0])
    #y.drop(y != "nontech")
    #print(y)

    # Initialize
    tfidf_vectorizer = TfidfVectorizer()
    tfidf_vectorizer_noTech = TfidfVectorizer()

    # Fit transform the vectorizer

    X_train_Tfidf_df = tfidf_vectorizer.fit_transform(X).toarray()
    Xn_train_Tfidf_df = tfidf_vectorizer_noTech.fit_transform(Xn).toarray()

    X_train_Tfidf_df = pd.DataFrame(X_train_Tfidf_df)
    Xn_train_Tfidf_df = pd.DataFrame(Xn_train_Tfidf_df)

    s = svm.SVC(C=1.0,kernel = 'rbf',degree = 3,coef0 = 0, probability = True)
    sn = svm.SVC(C=1.0,kernel = 'rbf',degree = 3,coef0 = 0, probability = True)

    s.fit(X_train_Tfidf_df, y)
    sn.fit(Xn_train_Tfidf_df, yn)

    #s_pred = s.predict(X_test_Tfidf_df)
    #s_predProb = s.predict_proba(X_test_Tfidf_df)

    #sn_pred = sn.predict(Xn_test_Tfidf_df)

    pickle.dump(s, open("models/class.sav", 'wb'))
    pickle.dump(sn, open("models/tech.sav", 'wb'))
    pickle.dump(tfidf_vectorizer, open("models/vectorizer.sav", 'wb'))
    pickle.dump(tfidf_vectorizer_noTech, open("models/vectorizer_noTech.sav", 'wb'))

    return tfidf_vectorizer, tfidf_vectorizer_noTech, s, sn

if __name__ == "__main__":
    trainModel()



