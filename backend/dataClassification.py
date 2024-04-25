#connect to database
#
#preprocess text using nltk
#check for tech/nontech and set nontech jobs to invalid (within a threshold)
#nuke invalid
# a. keyword search titles for the list of keywords that would determine you know what
# b. run the model on everything else, insert proper labels
#disconnect from the database

from writedata import SQLWriter

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
#nltk.download('all', force=True)

def kWordSearch(title):
    keywords = {'backend': ["software engineer", "software developer",
                             "java developer", "c++ developer", 
                             "javascript developer", "back-end developer",
                             "backend developer"],
                'cloud': ["cloud", "azure"],
                'devops': ["devops"], 
                'fullstack': ["full stack", "fullstack"],
                'security': ["security", "cyber"], 
                'ui_ux': ["frontend", "ui", "ux"]}
    
    for i in keywords: #the keyword categories
        for j in range(len(keywords[i])): #
    #me being dumb:
    '''for i in keywords:
        for j in range(len(keywords[i])):
            print(keywords[i][j])'''
    

DATABASE = "backend/jobs.db"

kWordSearch("dog")