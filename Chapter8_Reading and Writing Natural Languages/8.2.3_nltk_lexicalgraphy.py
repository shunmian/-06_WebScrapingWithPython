from nltk import word_tokenize,Text,pos_tag
from nltk.book import *

text = word_tokenize("The dust was thick so he had to dust")
print(pos_tag(text))

# output
# [('The', 'DT'), ('dust', 'NN'), ('was', 'VBD'), ('thick', 'RB'), ('so', 'RB'), ('he', 'PRP'), ('had', 'VBD'), ('to', 'TO'), ('dust', 'VB')]