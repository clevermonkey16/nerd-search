import json
import statistics
from math import log2
import itertools
import re

minsize = 10 # consider words with frequency > minsize in each set

count1 = 3909
count2 = 22000

file1 = open("ds.json", encoding='utf8', newline='')
file2 = open("jobs.json", encoding='utf8', newline='')
data1 = json.load(file1)
data2 = json.load(file2)

size1 = 0
size2 = 0
for key in data1.keys():
    if data1[key] <= minsize: continue
    size1 += data1[key]
for key in data2.keys():
    if data2[key] <= minsize: continue
    size2 += data2[key]

# data.keys() = list of keys
# data.items() = list of (key, value) pairs

"""
approach:
currently have a frequency table of words
- stats based upon number of times only in documents where it appears
- compare vs regular dataset, find words with negative/positive correlations
- remove those with close to neutral correlation, check only those with positive/negative correlation

"""

stattable = {}
ratio = size2/size1

cswords = []
nwords = [] # nword LMAO
for word in data1.keys():
    if data1[word] <= minsize: continue
    if word in data2 and data2[word] > minsize:
        stattable[word] = data1[word]/data2[word]*ratio
    else:
        cswords.append(word)

for word in data2.keys():
    if data2[word] <= minsize: continue
    if word not in data1:
        nwords.append(word)

# print(len(stattable))
# print(stattable)

words = sorted(stattable.keys(), key=lambda x:stattable[x])

sortedwords = {}
nums = []
for word in words:
    sortedwords[word] = log2(stattable[word])
    nums.append(log2(stattable[word]))

# print(sortedwords)

description = """

Data Engineer Intern

"""

tokens = re.split(r'[,.\" !?><\-=+@#$/%^&*()\s\\:;{}\[\]~`•]', description)
techness = 0
for token in tokens:
    if token in sortedwords:
        print(token, sortedwords[token])
        techness += sortedwords[token]

print(techness)

"""
mean = statistics.mean(nums)
med = statistics.median(nums)
stdev = statistics.stdev(nums)
var = statistics.variance(nums)
print("mean:", mean)
print("med:", med)
print("stdev:", stdev)
print("var:", var)

print(sortedwords['and'], sortedwords['of'], sortedwords['or'])
print(cswords)
# print(nwords)
print(size1, size2)
print(len(sortedwords))

# consider number of standard deviations above mean (note that this is log(ratio))
clean = list(itertools.filterfalse(lambda x:sortedwords[x]<mean+1.5*stdev, sortedwords.keys()))
print(clean)
print(len(clean))
print(sortedwords["python"])
"""
"""
improvements:
- filter out low-frequency words automatically
    - account for low-freq words
- better model (include some NLP in this?)
- maybe use this data and throw it in a neural network?

parameters: 
- minimum frequency
- ratio (num standard deviations)
- word2vec similarity (to what?) (not added yet)

how to identify?
- some statistic for "more likely than not" to be a data science job
idea: multiply (or add since we are using logs) ratios of all the words lmao this is a horrible idea
    - would directly use the table of ratios 
    - then can do statistical analysis on that and pick things more likely than not to be true
    - gives each page a "score"

"""