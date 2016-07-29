from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

def ngrams(input,n):
    #保证所有相邻字母之间只有1个空格
    input = re.sub('\n+', ' ', input)   #多个换行符'\n'  变1空格
    input = re.sub(' +', ' ', input)    #多个空格        变1空格
    input = re.sub('\xa0+', ' ', input) #多个硬空格\xa0   变1空格

    input = input.split(' ')
    output = []
    for i in range(len(input)-1+n):
        output.append(input[i:i+n])
    return output



htmlFile = urlopen("http://en.wikipedia.org/wiki/Python_(programming_language)")
bsObj = BeautifulSoup(htmlFile.read(),"html.parser")
content = bsObj.find("div",{"id":"mw-content-text"}).get_text()

ngrams = ngrams(content,2)

for ngram in ngrams:
    print(ngram)

print(len(ngrams))


#Output
# ['This', 'article']
# ['article', 'is']
# ...
# ['Python', '3.5)[5]']
# ['Lisp,[16]', 'Modula‑3,[11]']
# ...
# 总结成
# ['Pythoneers.[43][44]', 'Syntax'], ['7', '/'], ['/', '3'], ['3', '=='], ['==', '2']


# Output
# ['This', 'article']
# ['article', 'is']
# ...
# ['Foundation', 'License\n\n\nFilename']
# ['License\n\n\nFilename', 'extensions\n.py,']