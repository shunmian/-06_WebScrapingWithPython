from urllib.request import urlopen

textFileHandler = urlopen("http://www.pythonscraping.com/pages/warandpeace/chapter1.txt")
textContent = textFileHandler.read()
print(textContent)

# Output:
# b'CHAPTER I\n\n"Well, Prince, so Genoa and Lucca


