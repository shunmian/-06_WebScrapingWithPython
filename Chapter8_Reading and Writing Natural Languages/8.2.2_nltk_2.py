from nltk import word_tokenize,FreqDist,bigrams,ngrams
from nltk import Text
from nltk.book import text6  #直接可用book下的attribute,如果用improt nltk,book,你得book.attribute


#1. text object
tokens = word_tokenize("Here is some not very interesting text")
text = Text(tokens)
print(len(text6)/len(text))

# Output
# 2423.8

#2. freuqncy distribution
fdist = FreqDist(text6)
print(fdist.most_common(10))
print(fdist["Grail"])

# Output
# [(':', 1197), ('.', 816), ('!', 801), (',', 731), ("'", 421), ('[', 319), (']', 312), ('the', 299), ('I', 255), ('ARTHUR', 225)]
# 34

#3. n-grams
bigrams = bigrams(text6)
bigramsDist =FreqDist(bigrams)
print(bigramsDist[("Sir","Robin")])

# Output
# 18

fourgrams = ngrams(text6,4)
fourgamsDist =FreqDist(fourgrams)
print(fourgamsDist[("father","smelt","of","elderberries")])

# Output
# 1

#4. iteration for text object, frequency distribution, ngrams

fourgrams = ngrams(text6,4)
for fourgram in fourgrams:
    if fourgram[0] == "father":
        print(fourgram)

# Output
# ('father', 'smelt', 'of', 'elderberries')
# ('father', 'owns', 'the', 'biggest')
# ('father', ',', 'who', 'wishes')
# ('father', ',', 'that', "'")
# ('father', '--', 'GUEST', '#')
# ('father', '--', 'GUEST', '#')
# ('father', ',', 'who', ',')
