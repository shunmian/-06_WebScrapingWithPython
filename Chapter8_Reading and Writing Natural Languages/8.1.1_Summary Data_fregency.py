from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import string
from collections import OrderedDict

def cleanInput(input):
    #保证所有相邻字母之间只有1个空格
    input = input.lower()
    input = re.sub('\n+', ' ', input)   #多个换行符'\n'  变1空格
    input = re.sub('\[[0-9]*\|,]','',input)
    input = re.sub(' +', ' ', input)    #多个空格        变1空格
    input = re.sub('\xa0+', ' ', input) #多个硬空格\xa0   变1空格

    input = input.split(' ')
    cleanInput = []
    for item in input:
        item = item.strip(string.punctuation)
        if(len(item) > 1) or (item.lower() == 'a') or item.lower() == 'i':
            cleanInput.append(item)
    return cleanInput

def excludeDigits(list):
    flag = True
    for s in list:
        if any(i.isdigit() for i in s):
            flag = False
    return flag

def excludeHref(list):
    flag = True
    for s in list:
        if "http" in s or "www" in s:
            flag = False
    return flag

def isCommon(ngram):
    commonWords = ["the", "be", "and", "of", "a", "in", "to", "have", "it",
            "i", "that", "for", "you", "he", "with", "on", "do", "say", "this",
            "they", "is", "an", "at", "but","we", "his", "from", "that", "not",
            "by", "she", "or", "as", "what", "go", "their","can", "who", "get",
            "if", "would", "her", "all", "my", "make", "about", "know", "will",
            "as", "up", "one", "time", "has", "been", "there", "year", "so",
            "think", "when", "which", "them", "some", "me", "people", "take", "out", "into",                 "just", "see", "him", "your", "come", "could", "now",
            "than", "like", "other", "how", "then", "its", "our", "two", "more",
            "these", "want", "way", "look", "first", "also", "new", "because",
            "day", "more", "use", "no", "man", "find", "here", "thing", "give",
            "many", "well"]
    for word in ngram:
        if word in commonWords:
            return True
    return False

def ngrams(input,n):
    input = cleanInput(input)
    output = dict()
    for i in range(len(input)-1+n):
        itemList = input[i:i+n]
        if not isCommon(itemList):
            item = ' '.join(input[i:i+n])
            if excludeDigits(item) and excludeHref(item):
                if item in output:
                    output[item] += 1
                else:
                    output[item] = 1
    return output



txtFile = urlopen("http://pythonscraping.com/files/inaugurationSpeech.txt")
content = str(txtFile.read(), 'utf-8')

ngrams = ngrams(content,2)
sortedNGrams = OrderedDict(sorted(ngrams.items(), key=lambda item: item[1], reverse=True))

for k,v in sortedNGrams.items():
    print(k,v)

#Output
# united states 10
# general government 4
# executive department 4
# government should 3
# same causes 3
# chief magistrate 3
# mr jefferson 3
# called upon 3