


from textblob import TextBlob
import pandas as pd
dataset = pd.read_csv('E:/Pywork/Pydata/Obama.txt')
dataset = dataset.to_string(index = False) 
type(dataset)
b1 =TextBlob(dataset)
print(b1.sentiment)
import re
dataset = re.sub("[^A-Za-z0-9]+"," ",dataset) # Here I am taking those A-Z ,a-z and 0-9 characters only 
print(dataset)

import nltk

    
from nltk.tokenize import word_tokenize
Tokens = word_tokenize(dataset)
print (Tokens) # These tokens are words

#No. of tokens in the dataset
len(Tokens)

#Freq of occurence of distinct elements
from nltk.probability import FreqDist
fdist = FreqDist()

for word in Tokens:
    fdist[word.lower()]+=1 # Here I am coverting upper letter word to lower lette and calculate the frequency
fdist
fdist.plot(20)


from nltk.stem import PorterStemmer
pst=PorterStemmer()
token=[]
for word in Tokens:
    token=token+[pst.stem(word)]
    
print(token)

import nltk.corpus

stopwords = nltk.corpus.stopwords.words('english')
stopwords[0:10] # printing only 10 stopwords 

#Getting rid of stopwords
for FinalWord in token:
    if FinalWord not in stopwords:
        print(FinalWord)

b2 =TextBlob(FinalWord)
print(b2.sentiment)