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
import modelTraining

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

class data_classify:
    #this is stupidly slow
    def __init__(self):
            self.keywords = {'backend': ["backend", "back-end", "back end"],
                             'cloud': ["cloud", "azure"],
                             'data': ["data analyst", "data engineer", "data scientist"],
                             'databases': ["database", "data architect", "aws", "db"],
                             'hardware': ["embedded", "mechanical", "electrical", 
                                         "hardware", "photonics", "radio", "circuits"], 
                             'fullstack': ["full stack", "fullstack", "full-stack"],
                             'it_devops': ["devops", "i.t.", "it", "information technology"],
                             'mobile': ["android", "ios", "mobile"],
                             'networks': ["network", "data communication", "networks"],
                             'pm': ["project manager", "project coordinator", "pm"],
                             'qa': ["qa", "quality", "tester", "test"],
                             'security': ["security", "cyber"],
                             'systems': ["systems engineer", "system engineer"],
                             'ui_ux': ["frontend", "ui", "ux", "front-end"]}
            
            self.techModel = pickle.load(open("models/tech.sav",'rb'))
            self.classModel = pickle.load(open("models/class.sav", 'rb'))
            self.techVectorizer = pickle.load(open("models/vectorizer_noTech.sav",'rb'))
            self.classVectorizer = pickle.load(open("models/vectorizer.sav", 'rb'))

            self.lemmatizer = WordNetLemmatizer()
            self.stemmer = PorterStemmer()

            """
            vectorizer, vectorizer_noTech, classModel, techModel = modelTraining.trainModel()
            self.classVectorizer = vectorizer
            self.techVectorizer = vectorizer_noTech
            self.classModel = classModel
            self.techModel = techModel"""

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
        return " ".join(filtered_text)

    def stem_words(self,text):
        word_tokens = word_tokenize(text)
        stems = [self.stemmer.stem(word) for word in word_tokens]
        return " ".join(stems)
    
    def lemma_words(self,text):
        word_tokens = word_tokenize(text)
        lemmatized_words = [self.lemmatizer.lemmatize(word) for word in text]
        #print(lemmatized_words)
        return " ".join(lemmatized_words)
    
    def remove_whitespace(self,text):
        return " ".join(text.split())

    def preProcess(self, phrase, typ):
        
        processPhrase = phrase #change this later on
        
        #processPhrase = processPhrase.lower()
        processPhrase = self.remove_special_characters(processPhrase)
        processPhrase = self.remove_punctuation(processPhrase)
        processPhrase = self.remove_stopwords(processPhrase) 
        processPhrase = self.remove_whitespace(processPhrase) 
        
        processPhrase = self.stem_words(processPhrase)
        #print(processPhrase)
        #processPhrase = self.lemma_words(processPhrase) 

        #print(type(processPhrase))

        #processPhrase = ' '.join(processPhrase)
        processPhrase = [processPhrase]

        print(processPhrase)

        if typ == "class":
            phraseVectorized = self.classVectorizer.transform(processPhrase).toarray()
            phrase_df = pd.DataFrame(phraseVectorized)
        elif typ == "tech":
            phraseVectorized = self.techVectorizer.transform(processPhrase).toarray()
            phrase_df = pd.DataFrame(phraseVectorized)

        return phrase_df
     
    def kWordSearch(self, title):
        title = title.lower()
        for i in self.keywords: #the keyword categories
            for j in range(len(self.keywords[i])): #goes through the array belonging to the categories
                if((self.keywords[i][j]) in title): #is found inside the phrase
                    return i
                
        return "no_kClass" #"no keyword class"

    def isTech(self, phrase):
        prediction = self.techModel.predict(self.preProcess(phrase,"tech"))
        #prediction = self.techModel.predict(phrase)
        return prediction

    def classify(self, phrase):
        prediction = self.classModel.predict(self.preProcess(phrase,"class"))
        return prediction

if __name__ == "__main__":
    testClass = data_classify()
    #print(testClass.isTech("help me to name it"))
    #print(testClass.preProcess("help me to name it, either way it will change"))
    pred = testClass.classify("""Y ou will…

Participate in and successfully complete structured classroom workshops specific to core CCNA preparation administered by a Meraki instructor
Work through lab assignments via Packet Tracer, NetAcad labs, and Meraki troubleshooting labs to learn the foundations of networking and troubleshooting
Gain an understanding of the networking field by participating and engaging in various courses
Assist with lab testing work as needed for Meraki products
Identify issues suitable for entry in the Meraki Knowledge Base
Effectively communicate with third parties such as partners and customers regarding technical issues and customer service inquiries, both orally and in writing
Collaborate with other Support team members to fix network outages, misconfigurations, and complex networking issues of customers’ devices
Read and analyze packet capture using Wireshark

You are….

Pursuing an associate's degree or are a Junior or senior pursuing a bachelor's degree with a computer science, information technology, networking, systems administration, or a related field from an accredited university. Individuals who have completed a relevant networking BootCamp within the last 6 months will also be considered. Individuals pursuing a master’s degree will not be considered 
Hardworking and interested in exploring the Networking field
Passionate to assist and problem-solve with customers
Able to strategically and critically think about how to look for solutions, willing to be pushed outside your knowledge areas, and eager to learn and find solutions
An efficient communicator and problem-solver
Networking certifications a plus: CCNA, CCNP CWNA, etc. 
Experience supporting or testing LANs, VLANs, WLANs, VPNs, NAT devices, &/or DHCP servers is a plus
Comprehension of networking protocols, including TCP, STP, ARP, Ethernet, OSPF, etc. is a plus
Preferred experiences within helpdesk, technical call center, desktop support, or past networking experiences preferred, but not required. 
Authorized to work in the U.S. without requiring sponsorship now or in the future 

Qualifications

Basic understanding of networking fundamentals, e.g. be able to explain the functions of and differences among the link, network, transport, and application layers
A passion to assist and problem-solve with our customers
Outstanding account management, follow-through, and problem-solving skills
Resourcefulness and attention to detail
Excellent communication skills, both written and verbal
""")
    print(pred)

    techCheck = testClass.isTech("""Y ou will…

Participate in and successfully complete structured classroom workshops specific to core CCNA preparation administered by a Meraki instructor
Work through lab assignments via Packet Tracer, NetAcad labs, and Meraki troubleshooting labs to learn the foundations of networking and troubleshooting
Gain an understanding of the networking field by participating and engaging in various courses
Assist with lab testing work as needed for Meraki products
Identify issues suitable for entry in the Meraki Knowledge Base
Effectively communicate with third parties such as partners and customers regarding technical issues and customer service inquiries, both orally and in writing
Collaborate with other Support team members to fix network outages, misconfigurations, and complex networking issues of customers’ devices
Read and analyze packet capture using Wireshark

You are….

Pursuing an associate's degree or are a Junior or senior pursuing a bachelor's degree with a computer science, information technology, networking, systems administration, or a related field from an accredited university. Individuals who have completed a relevant networking BootCamp within the last 6 months will also be considered. Individuals pursuing a master’s degree will not be considered 
Hardworking and interested in exploring the Networking field
Passionate to assist and problem-solve with customers
Able to strategically and critically think about how to look for solutions, willing to be pushed outside your knowledge areas, and eager to learn and find solutions
An efficient communicator and problem-solver
Networking certifications a plus: CCNA, CCNP CWNA, etc. 
Experience supporting or testing LANs, VLANs, WLANs, VPNs, NAT devices, &/or DHCP servers is a plus
Comprehension of networking protocols, including TCP, STP, ARP, Ethernet, OSPF, etc. is a plus
Preferred experiences within helpdesk, technical call center, desktop support, or past networking experiences preferred, but not required. 
Authorized to work in the U.S. without requiring sponsorship now or in the future 

Qualifications

Basic understanding of networking fundamentals, e.g. be able to explain the functions of and differences among the link, network, transport, and application layers
A passion to assist and problem-solve with our customers
Outstanding account management, follow-through, and problem-solving skills
Resourcefulness and attention to detail
Excellent communication skills, both written and verbal
""")
    print(techCheck)

    wordSearch = testClass.kWordSearch("Network Support Engineering Intern - Fall 2024 (Meraki)")
    print(wordSearch)

#we should probably double-triple classify based on kwordsearch
#classModel = "backend/class.sav"



#cloudTest = "Applicaton architecture, cloud, open source, scripting, code, enterprise software, design, technical standards"
#print(kWordSearch(cloudTest, keywords))