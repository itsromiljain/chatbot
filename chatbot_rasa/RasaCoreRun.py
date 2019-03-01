import rasa_core
from rasa_core.agent import Agent
from rasa_core.run import serve_application
from rasa_core.utils import EndpointConfig
from rasa_core.interpreter import RasaNLUInterpreter
import gensim
from gensim.models.fasttext import FastText
import pandas as pd
from jira import JIRA

import json

def call_rest():
    class JIRACLASS(object):

        def __init__(self):
            self.jira = JIRA({'server':'https://manojteluguntla.atlassian.net'},basic_auth=('manoj.teluguntla@lntinfotech.com','Western852$@')) 

        def getProjects(self,data):
            return self.jira.project(data);

        def getIssue(self,id):
            return self.jira.issue(id)

        def createIssue(self,data):
             return self.jira.create_issue(data)

        def deleteIssue(self,id):
            self.jira.delete_issue(id)

    jiravar = JIRACLASS()
    print("Enter the Project Key, or enter 0 if you wish to hit the default project")
    key_1=input()
    if str(key_1)=="0":
        key_1='TG'
    print("Enter the Description, or enter 0 if you wish to hit the default Description")
    des_1=input()
    if str(des_1)=="0":
        des_1='Look into this one'
    print("Enter the Issue Type, or enter 0 if you wish to hit the default Issue Type")
    issu_1=input()
    if issu_1=="0":
        issu_1='Bug'
    
    issue_dict = {
        'project': {'key': key_1},
        'summary': 'New issue from jira-python',
        'description': des_1,
        'issuetype': {'name': issu_1},
    }
#     print(jiravar.getProjects("TG"))
    #print(jiravar.getIssue("CHAT-1"))
    d=jiravar.createIssue(issue_dict)
    #print(d)
    #z=str(d)
    #print(d.id)
    j=d.raw
    dr=json.dumps(j) 
    data=json.loads(dr)
    kal=str("ID: "+data["id"])+'\n'+"Key: "+str(data["key"])+'\n'+"API link: "+str(data["self"])+'\n'+"Description: "+str(data["fields"]["issuetype"]["description"])
#     print(data["id"])
#     print(data["key"])
#     print(data["self"])
#     print(data["fields"]["issuetype"]["description"])
    
    return str(kal)


col=['col1','col2','col3','col4','col5']
data= pd.read_csv("rdany.csv",encoding = "ISO-8859-1", header=None, names=col)
data.drop(['col1','col3','col4','col5'],axis=1,inplace=True)
k=[]
for sent in data['col2']:
    k.append(sent)
import re
dat=[]
for sen in data['col2']:
    wordList = str(sen).split()
    dat.append(wordList)

model = FastText.load("fasttext2.model")
model.build_vocab(dat, update=True)
model.train(dat, total_examples=len(dat), epochs=100)

data_words=['hello','hi','what','hey','near']

interpreter = RasaNLUInterpreter('models/current/default/nlu')
action_endpoint = EndpointConfig(url = "http://localhost:5055/webhook")
agent = Agent.load('models/dialogue', interpreter=interpreter)

print("Your bot is ready to talk! Type your messages here or send 'stop'")

def proc(text):
    st=""
    for word in range(len(text)):
        corr=model.wv.most_similar(text[word], topn=5)
        temp=0
        for i in range(len(corr)):
            for j in range(len(data_words)):
                if corr[i][0]==data_words[j]:
                    text[word]=corr[i][0]
                    temp=1
                    break
            if temp==1:
                break
        if word!=len(text)-1:
            st=st+text[word]+" "
        else:
            st=st+text[word]
    return st


while True:
    a = input()
    k=a.split()
    a=proc(k)
    if a == 'stop':
        break
    responses = agent.handle_message(a)
    for response in responses:
        if response["text"]=="api":
            kal=call_rest()
            print("Here are the details of your ticket"+"\n"+kal)
        else:
            print(response["text"])
        
        
        
