from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import string
from collections import OrderedDict

def cleanInput(input):
    #保证所有相邻字母之间只有1个空格

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




def ngrams(input,n):
    input = cleanInput(input)
    output = dict()
    for i in range(len(input)-1+n):
        item = ' '.join(input[i:i+n])
        if excludeDigits(item) and excludeHref(item):
            if item in output:
                output[item] += 1
            else:
                output[item] = 1
    return output

htmlFile = urlopen("http://en.wikipedia.org/wiki/Python_(programming_language)")
bsObj = BeautifulSoup(htmlFile.read(),"html.parser")
content = bsObj.find("div",{"id":"mw-content-text"}).get_text()

ngrams = ngrams(content,2)

#ngrams是一个dictionary, 根据其value来排序(sorted,返回一个list),排完之后按顺序插入OrderDict
ngrams = OrderedDict(sorted(ngrams.items(), key=lambda item: item[1], reverse=True))

for k,v in ngrams.items():
    print(k,v)



#Output
# Software Foundation 37
# Python Software 37
# of Python 36
# of the 34
# Foundation Retrieved 32
# ...