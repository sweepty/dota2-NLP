from sklearn.feature_extraction.text import CountVectorizer
from nltk.tokenize import word_tokenize
from nltk.tokenize.regexp import RegexpTokenizer 
import nltk
import numpy as np
from nltk.stem import PorterStemmer
import pandas as pd
from nltk.corpus import stopwords 

df = pd.DataFrame()
df = pd.read_csv('./cuss_chat.csv')

stemmer = PorterStemmer()
tokenizer = RegexpTokenizer("[\w']+") 

docs = df['key']
# print(docs[10031])

a_docs  = np.array(docs)

count = CountVectorizer()
ts = []
stop_words = set(stopwords.words('english')) 
# 1120648
print(len(a_docs))
length = len(a_docs)

for i in range(0, length):
    to = word_tokenize(a_docs[i])  
    for j in to:
        if j not in stop_words:
            ts.append(stemmer.stem(j.lower()))
    
bag = count.fit_transform(ts)

en = nltk.Text(ts)

en.vocab().items()

fdist = nltk.FreqDist(en.vocab())

with open('./topword100.csv', 'w') as csvoutput:
    writer = csv.writer(csvoutput)
    writer.writerow("word", "frequency")
    for word, frequency in fdist.most_common(100):
        writer.writerow(word, frequency)
        print(u'{};{}'.format(word, frequency))
