#!/usr/bin/python3
#Jeannelle Alford
#jkalfor2

#A language ID program using a word bigram model

from dicts import DefaultDict
import re
import math

file = open("LangId.train.English", "r")
data = file.read()
file.close()
data = re.split('[^a-zA-Z\']+',data)
enDictUni = DefaultDict(1)
enDictBi = DefaultDict(DefaultDict(1))
enDictUni[data[0]] += 1
for i in range(1, len(data)):
    enDictUni[data[i]] += 1
    enDictBi[data[i-1]][data[i]] += 1

file = open("LangId.train.French", "r")
data = file.read()
file.close()
data = re.split('[^a-zA-Z\']+', data)
frDictUni = DefaultDict(1)
frDictBi = DefaultDict(DefaultDict(1))
frDictUni[data[0]] += 1
for i in range(1, len(data)):
    frDictUni[data[i]] += 1
    frDictBi[data[i-1]][data[i]] += 1

file = open("LangId.train.Italian", "r")
data = file.read()
file.close()
data = re.split('[^a-zA-Z\']+', data)
itDictUni = DefaultDict(1)
itDictBi = DefaultDict(DefaultDict(1))
itDictUni[data[0]] += 1
for i in range(1, len(data)):
    itDictUni[data[i]] += 1
    itDictBi[data[i-1]][data[i]] += 1

file = open("LangId.test")
data = file.read()
file.close()

data= data.split('\n')

def englishProb(prev, curr):
    if enDictUni[prev]==0:
        return 0
    ans = enDictBi[prev][curr] / enDictUni[prev]
    if ans==0:
        return 0    
    return math.log(ans)

def frenchProb(prev, curr):
    if frDictUni[prev]==0:
        return 0
    ans = frDictBi[prev][curr] / frDictUni[prev]
    if ans==0:
        return 0
    return math.log(ans)

def italianProb(prev, curr):
    if itDictUni[prev]==0:
        return 0
    ans = itDictBi[prev][curr] / itDictUni[prev]
    if ans==0:
        return 0
    return math.log(ans)

outfile = open("wordLangId.out", "w")
sent=1
for sentence in data:
    if sentence=='':
        break
    enProb = 0
    frProb = 0
    itProb = 0
    sentence = re.split('[^a-zA-Z\']+', sentence)
    for i in range(1, len(sentence)):
        enProb += englishProb(sentence[i-1], sentence[i])
        frProb += frenchProb(sentence[i-1], sentence[i])
        itProb += italianProb(sentence[i-1], sentence[i])
    if enProb < frProb and enProb < itProb:
        outfile.write(str(sent)+" English\n")
    elif frProb < enProb and frProb < itProb:
        outfile.write(str(sent)+" French\n")
    else:
        outfile.write(str(sent)+" Italian\n")
    sent += 1
outfile.close()
#
#
#
#
#
#
