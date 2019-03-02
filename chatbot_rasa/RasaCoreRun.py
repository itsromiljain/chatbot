import sys
sys.path.append('/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages')
from rasa_core.agent import Agent
from rasa_core.interpreter import RasaNLUInterpreter
import gensim
from gensim.models.fasttext import FastText
import pandas as pd
from jira import JIRA

import json


def call_rest(key_1,des_1,issu_1):
    class JIRACLASS(object):

        def __init__(self):
            self.jira = JIRA({'server':'https://rajsimhag.atlassian.net'},basic_auth=('gautham.rajsimha@gmail.com','gautham999')) 

        def getProjects(self,data):
            return self.jira.project(data);

        def getIssue(self,id):
            return self.jira.issue(id)

        def createIssue(self,data):
             return self.jira.create_issue(data)

        def deleteIssue(self,id):
            self.jira.delete_issue(id)

    jiravar = JIRACLASS()
#     print("Enter the Project Key, or enter 0 if you wish to hit the default project")
    if key_1=="0":
        key_1='CHAT'
#     print("Enter the Description, or enter 0 if you wish to hit the default Description")
    if des_1=="1":
        des_1='Look into this one'
#     print("Enter the Issue Type, or enter 0 if you wish to hit the default Issue Type")
    if issu_1=="2":
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


model = FastText.load("fasttext2.model")
data_words=['hello','hi','what','hey','near']

interpreter = RasaNLUInterpreter('models/current/nlu')
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

trigger=0
tr=0
gif=0
key_1="0"
key_2="1"
key_3="2"
while True:
    a = input()
    if str(a)!="0" or str(a)!="1" or str(a)!="2":
        aa=a
        k=a.split()
        a=proc(k)
#     if a == "no":
#         kal=call_rest(key_1,key_2,key_3)
#         print(kal)
#         break
#         a="nono"
    if a == 'stop':
        break
    if str(a)=='0':
        a='no1'
    if str(a)=='00':
        a='no2'
    if str(a)=='2':
        a='no3'
    if str(aa)=='11':
        print("Type your description")
        aa=input()
        a='no2'
    if str(a)=='IPAD':
        key_1='IPAD'
    if str(a)=='PHO':
        key_1='PHO'
    if str(a)=='MACB':
        key_1='MACB'
    if key_1=='IPAD':
        y1=99
    responses = agent.handle_message(a)
    for response in responses:
        if response["text"]=="create":
            print("type the project name or type 0 to hit the default project")
            trigger=1
            break
#         elif response["text"]=="project":
#             key_1=str(aa)
#             print("type 11 to type the description or type 00 to hit the default description")
#         elif response["text"]=="desc":
#             key_2=str(aa)
#             print("type the issue or type 2 to hit the default issue")
#         elif response["text"]=="api":
#             key_3=str(aa)
#             kal=call_rest(key_1,key_2,key_3)
#             print(kal)
#             print("type ticket to create a new issue and stop to exit")
#         elif response["text"]=='exx':
#             print("type ticket to create a new issue and stop to exit")
#         elif response["text"]=='phone1':
#             key_1="PHO"
#             print("Which phone is yours?")
#         elif response["text"]=='phone2':
#             key_2=a
#             print("What is your issue?")
#         elif response["text"]=='last':
#             key_3="Bug"
#             kal=call_rest(key_1,key_2,key_3)
#             print(kal)
#             print("A ticket with the above description has been created, please enter press stop to exit or type repair to raise a new issue")
        elif response["text"]=='san':
            sa=a
            lis=sa.split()
            for wd in lis:
#                 print(lis)
                if wd=='phone' or wd=='iphone':
                    key_1='PHO'
                    print("Which model is your iPhone")
#                     print("nonononono ")
                    break
                elif wd=='macbook' or wd=='mac' or wd=='imac':
                    key_1='MACB'
                    print("Which macbook are you using")
                    break
                elif wd=='ipad' or wd=='pad':
                    key_1='IPAD'
                    print("What's the model of your iPad")
                    break
        elif response["text"]=='tank':
            sa=a
            lis=sa.split()
            for wd in lis:
                if wd=='help':
                    print("Yes, tell me about it")
                    gif=2
                    break
            if gif==0:
                gif=1
                print("I'm glad I could help. Have a nice day. Bye.")
                break
        elif response["text"]=='Long press the power button to restart and check':
            sa=a
            lis=sa.split()
            for wd in lis:
                if wd=='screen' or wd=='stuck':
                    print("Long press the power button to restart and check")
                    tr=1
                elif wd=='pair':
                    print("Long press the power button to restart and check")
                    tr=2
                key_2=a
                key_3="Bug"
        elif response["text"]=='ninja':
            if a=='def1':
                key_2="Don't know what's the issue"
                key_3="Bug"
            else:
                key_2=a
                sa=a
                lis=sa.split()
                for wd in lis:
                    if wd=='new':
                        key_3='Task'
                        break
                    else:
                        key_3='Bug'
#             print(key_1)
            kka=call_rest(key_1,key_2,key_3)
            if tr==1:
                print("There must be some damage to the screen")
            elif tr==2:
                print("There must be some problem with the bluetooth")
            else:
                print("We will let you know when your item is available")
            print("A ticket has been raised with the below details as we are unable to find a solution. Our service team mighth help you out on this.")
            print(kka)
            print("Is that it or do you need help on anything else?")
        elif response["text"]=='salp':
            print("We have raised your ticket with default values")
            kl=call_rest(key_1,key_2,key_3)
            print(kl)
        else:
            print(response["text"])
    if gif==1:
        break