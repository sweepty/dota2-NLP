import csv
import pandas as pd
# from nltk.tokenize import word_tokenize
from nltk.tokenize.regexp import RegexpTokenizer 
import nltk
# import numpy as np
from nltk.stem import PorterStemmer

stemmer = PorterStemmer()
tokenizer = RegexpTokenizer("[\w']+") 
df = pd.read_csv('./dota2_data/dota3_chat2.csv')

docs = df['key']

negative_vocab = [ 
    'afk','ass',
    'bloodi', 'bollock', 'bullshit', 'burger', 'bitch',
    'cock', 'cocksucker', 'cracker', 'crap', 'cunt', 'chink', 'cancer',
    'damn', 'dick',
    'fuck', 'dimwit', 'dork', 'douch', 'dumb',
    'eff',
    'fanni', 'freak', 
    'gay', 'goddamn', 'gook', 
    'hell', 'holi', 'honki', 'hate', 
    'idot',
    'jackass', 'jap', 'jerk', 'jesu', 'junk',
    'lame', 'lose',
    'maggot', 'mot', 'motherfuck', 'mofo', 'mf', 'muff', 'monkey', 'mom', 'mother',
    'noob', 'nerd',
    'piss', 'pussi', 'poontang', 'psycho',
    'queer',
    'report', 'rape', 'retard', 'ruski',
    'shit', 'stfu', 'smh', 'stupid', 'shut', 'suck','screw', 'sap', 'scram', 'scum', 'slag', 'slut', 'sod',
    'troll', 'trash', 'twat', 'terrorist', 'tard',
    'wtf'
]

# Predict
def predictSentiment(line):
    neg = 0

    ts = []
    print(line)
    sentence = line['key']
    to = tokenizer.tokenize(sentence)
    if len(to) > 0:
        for j in to:
            ts.append(stemmer.stem(j.lower()))

    for words in ts:
        if words in negative_vocab:
            neg = neg + 1

    with open('./dota2_data/dota3_chat2.csv','r') as csvinput:
        with open('./output.csv', 'w') as csvoutput:
            writer = csv.writer(csvoutput)

            for row in csv.reader(csvinput):
                if row[0] == "match_id":
                    writer.writerow(row+["cuss"])
                else:
                    if neg > 0:
                        writer.writerow(row+[1])
                    else:
                        writer.writerow(row+[0])

with open('./dota2_data/dota3_chat2.csv','r') as csvinput:
    with open('./cuss_chat.csv', 'w') as csvoutput:
        writer = csv.writer(csvoutput)
        count =0
        for row in csv.reader(csvinput):
            if row[0] == "match_id":
                writer.writerow(row+["count"])
            else:
                count += 1
                neg = 0
                ts = []
                print(count)
                print(row)
                sentence = row[4]
                to = tokenizer.tokenize(sentence)
                if len(to) > 0:
                    for j in to:
                        ts.append(stemmer.stem(j.lower()))

                for words in ts:
                    if words in negative_vocab:
                        neg = neg + 1
                writer.writerow(row+[neg])
