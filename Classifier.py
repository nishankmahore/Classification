import os
import json
import glob
import sys
import nltk.classify
from textblob.classifiers import NaiveBayesClassifier

with open('trained_data.json', 'r') as training:
    c = NaiveBayesClassifier(training, format="json")

result = open('result_sample.txt', 'w')

path = 'input/*.txt'
files=glob.glob(path)
for file in files:
    f=open(file, 'r')
    for line in f:
        if line.startswith("#"):
            pass
        else:
            result.write(c.classify(line.decode().encode('utf-8')) + "	" + line )
    f.close()

result.close()



