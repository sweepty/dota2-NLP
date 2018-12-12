import csv
import pandas as pd
from sklearn import tree
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
import numpy as np
from nltk.tokenize.regexp import RegexpTokenizer 
import nltk, re
from nltk.stem import PorterStemmer

df = pd.read_csv('./chat.csv')

X_train, X_test, y_train, y_test = train_test_split(df['key'].values.astype('U'), df['count'].values.astype('U'), test_size=0.2)

stemmer = PorterStemmer()

tokenizer = RegexpTokenizer("[\w']+") 
ts = []
def tokenize(s): 
    to = tokenizer.tokenize(s)
    if len(to) > 0:
        for j in to:
            ts.append(stemmer.stem(j.lower()))
    return ts

vect = CountVectorizer(tokenizer=tokenize)
tf_train = vect.fit_transform(X_train)
tf_test = vect.transform(X_test)

p = tf_train[y_train==1].sum(0) + 1
q = tf_train[y_train==0].sum(0) + 1
r = np.log((p/p.sum()) / (q/q.sum()))
b = np.log(len(p) / len(q))

model = LogisticRegression(C=0.2, dual=True)
model.fit(tf_train, y_train)
preds = model.predict(tf_test)
accuracy = (preds == y_test).mean()

print(accuracy)