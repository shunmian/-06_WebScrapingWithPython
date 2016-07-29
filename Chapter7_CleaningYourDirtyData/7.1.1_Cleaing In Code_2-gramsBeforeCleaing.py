from urllib.request import urlopen
from bs4 import BeautifulSoup

def ngrams(input,n):
    input = input.split(' ')                   #input is list of string, separated by ' '
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

# Output
# ['This', 'article']
# ['article', 'is']
# ...
# ['Foundation', 'License\n\n\nFilename']
# ['License\n\n\nFilename', 'extensions\n.py,']