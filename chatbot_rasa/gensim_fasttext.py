import gensim
from gensim.models.fasttext import FastText
import pandas as pd
col=['col1','col2','col3','col4','col5']
data= pd.read_csv("rdany.csv",encoding = "ISO-8859-1", header=None, names=col)
data.drop(['col1','col3','col4','col5'],axis=1,inplace=True)
data.head
print(data['col2'])
k=[]
for sent in data['col2']:
    k.append(sent)
import re
dat=[]
for sen in data['col2']:
    wordList = str(sen).split()
    dat.append(wordList)
print(dat[0:5])
model = FastText(dat, size=100, window=5, min_count=1, workers=4)
print(model.wv.most_similar('which', topn=5))
model.build_vocab(dat, update=True)
model.save("fasttext2.model")
model.train(dat, total_examples=len(dat), epochs=100)
corr=model.wv.most_similar('hellp', topn=5)
print(corr[2][0])
if corr[2][0]=='hello':
    print('kk')
print(model.wv.most_similar('whay', topn=5))
print(model.wv.most_similar('probem', topn=5))
print(model.wv.most_similar('hallo', topn=5))
import collections
for sent in dat:
    vocab = vocab+collections.Counter(sent)
print(vocab)
print(vocab)
vocab = vocab+collections.Counter(dat[1])
print(vocab)
