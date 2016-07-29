from urllib.request import urlopen
from random import randint
import re

#get the total occurence of a word
def subsequentialWordsTotalOccurence(subsequentialWordsDictionary):
    sum = 0
    for word, occurence in subsequentialWordsDictionary.items():
        sum += occurence
    return sum

#get the random next word of the word
def retrieveSubsequentialWordRandomly(subsequentialWordsDictionary):
    randomIndex = randint(1,subsequentialWordsTotalOccurence(subsequentialWordsDictionary))

    for word, occurence in subsequentialWordsDictionary.items():
        randomIndex -=occurence
        if (randomIndex <=0):
            return word

#build a dictionary of dictionary, as the input of Markov Models
def buildWordsDict(text):

    punctuation = [',',':','.','?','!']

    for symbol in punctuation:
        text = text.replace(symbol," "+symbol+" ")

    text = re.sub("\n+"," ",text)
    text = re.sub(" +"," ",text)
    # text = text.lower()
    words = text.split(" ")
    words = [word for word in words if word != ""]

    mainWordDict = dict()

    for i in range(len(words)-1):
        word = words[i]
        subsequentialWord = words[i+1]
        if word not in mainWordDict:
            mainWordDict[word] = dict()
        subsequentialWordsDict = mainWordDict[word]
        if subsequentialWord not in subsequentialWordsDict:
            subsequentialWordsDict[subsequentialWord] = 1
        else:
            subsequentialWordsDict[subsequentialWord] +=1

    return mainWordDict

#get words dictionary
textFile = urlopen("http://pythonscraping.com/files/inaugurationSpeech.txt")
content = str(textFile.read(), 'utf-8')
wordDict = buildWordsDict(content)

wordsLength = 100
makeupSentence = ""
startWord = "I"


for i in range(wordsLength):
    makeupSentence += startWord + " "
    startWord = retrieveSubsequentialWordRandomly(wordDict[startWord])

print(makeupSentence)

# Output
# I believe with the genuine spirit , those collected in accordance with the several Cantons , are not only by any of their direction , and of each other consequences will than their agents , not be considered most intimate union that the great error in periods like the sages who promised that secured to continue for which has called upon none more particularly of power of conduct in the great principles which it to it has there is danger to produce the necessary employment of all those of the same causes must ever produce the proud democrat of such