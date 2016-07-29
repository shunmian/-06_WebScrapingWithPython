from urllib.request import urlopen

textFileHandler = urlopen("http://www.pythonscraping.com/pages/warandpeace/chapter1-ru.txt")
textContent = textFileHandler.read()
print(str(textContent,'UTF-8'))

#Output:
# b"\xd0\xa7\xd0\x90\xd0\xa1\xd0\xa2\xd0\xac


