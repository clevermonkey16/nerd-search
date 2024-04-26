#connect to database
#
#preprocess text using nltk
#check for tech/nontech and set nontech jobs to invalid (within a threshold)
#nuke invalid
# a. keyword search titles for the list of keywords that would determine you know what
# b. run the model on everything else, insert proper labels
#disconnect from the database

# Steven and Noah's procedure:
# 1. Connect to the database

# Iterate over rows of database

# for each row
# get job description, job title
# if category is na, run black box classifier on info
# if classifier returns false, make row bit invaild
# else run black box classifier to get category, update category 

# nuke table of invalid jobs

# close database connection

# NOTE: Keyword search goes at the top of the blackbox classifier

from writedata import SQLWriter

import pickle

import pandas as pd
import numpy as np
import nltk
import json
import string
from array import array
import re
import sklearn
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
#nltk.download('all', force=True)


from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem.porter import PorterStemmer
from nltk.stem import WordNetLemmatizer

from sklearn.feature_extraction.text import TfidfVectorizer

# remove keyfault stopwords

def remove_stopwords(text):
    stop_words = set(stopwords.words("english"))
    word_tokens = word_tokenize(text)
    filtered_text = [word for word in word_tokens if word not in stop_words]
    return filtered_text

class data_classify:
    #this is stupidly slow
    def __init__(self):
            self.keywords = {'backend': ["software engineer", "software developer",
                                    "java developer", "c++ developer", 
                                    "javascript developer", "back-end developer",
                                    "backend developer", "backend", "back-end", "back end"],
                             'cloud': ["cloud", "azure"],
                             'data': ["data analyst", "data engineer", "data scientist"],
                             'databases': ["database", "data architect", "aws", "db"],
                             'hardware': ["embedded", "mechanical", "electrical", 
                                         "hardware", "photonics", "radio", "circuits"], 
                             'fullstack': ["full stack", "fullstack", "full-stack"],
                             'it_devops': ["devops", "i.t.", "it", "information technology"],
                             'mobile': ["android", "ios", "mobile"],
                             'networks': ["network", "data communication"],
                             'pm': ["project manager", "project coordinator", "pm"],
                             'qa': ["test architect", "test engineer", "qa", "quality assurance", "quality", "tester", "test"],
                             'security': ["security", "cyber"],
                             'systems': ["systems engineer", "system engineer"],
                             'ui_ux': ["frontend", "ui", "ux"]}
            
            self.techModel = pickle.load(open("models/tech.sav",'rb'))
            #self.classModel = pickle.load(open("backend/models/class.sav", 'rb'))

            self.lemmatizer = WordNetLemmatizer()
            self.stemmer = PorterStemmer()

            self.tfidf_vectorizer = TfidfVectorizer()

            print("welcome to blackbox 1.0")
    
    # Removes special characters
    def remove_special_characters(self, text):
        pattern = r'[^a-zA-Z\s]'
        cleaned_text = re.sub(pattern, '', text)
        return cleaned_text

    def remove_punctuation(self, text):
        translator = str.maketrans('', '', string.punctuation)
        return text.translate(translator)
    
    def remove_stopwords(self,text):
        stop_words = set(stopwords.words("english"))
        word_tokens = word_tokenize(text)
        filtered_text = [word for word in word_tokens if word not in stop_words]
        return filtered_text

    def stem_words(self,text):
        word_tokens = word_tokenize(text)
        stems = [self.stemmer.stem(word) for word in word_tokens]
        return stems
    
    def lemma_words(self,text):
        word_tokens = word_tokenize(text)
        lemmatized_words = [self.lemmatizer.lemmatize(word) for word in text]
        return lemmatized_words

    def preProcess(self, phrase):
        processPhrase = phrase #change this later on

        processPhrase = processPhrase.lower()
        processPhrase = self.remove_special_characters(processPhrase)
        processPhrase = self.remove_punctuation(processPhrase)
        processPhrase = self.remove_stopwords(processPhrase) 
        #processPhrase = self.stem_words(processPhrase)
        #processPhrase = self.lemma_words(processPhrase) 

        #return processPhrase
        phraseVectorized = self.tfidf_vectorizer.fit_transform(processPhrase).toarray()
        phraseVectorized = phraseVectorized.reshape(1,-1)
        #phrase_df = pd.DataFrame(phraseVectorized)

        return phraseVectorized
     
    def kWordSearch(self, title):
        for i in self.keywords: #the keyword categories
            for j in range(len(self.keywords[i])-1): #goes through the array belonging to the categories
                if(title.find(self.keywords[i][j]) != -1): #is found inside the phrase
                    return i
                
        return "no_kClass" #"no keyword class"

    def isTech(self, phrase):
        prediction = self.techModel.predict(self.preProcess(phrase))
        #prediction = self.techModel.predict(phrase)
        return prediction

    def classify(self, phrase):
        pass
    #DATABASE = "backend/jobs.db"

if __name__ == "__main__":
    testClass = data_classify()
    #print(testClass.isTech("help me to name it"))
    print(testClass.preProcess("help me to name it, either way it will change"))
    pred = testClass.isTech("help me to name it, either way it will change")
    print(pred)

#we should probably double-triple classify based on kwordsearch
#classModel = "backend/class.sav"



#cloudTest = "Applicaton architecture, cloud, open source, scripting, code, enterprise software, design, technical standards"
#print(kWordSearch(cloudTest, keywords))