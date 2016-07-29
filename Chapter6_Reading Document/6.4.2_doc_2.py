from urllib.request import urlopen
from zipfile import ZipFile
from io import BytesIO
from bs4 import BeautifulSoup

wordFileHandler = urlopen("http://pythonscraping.com/pages/AWordDocument.docx")
wordFileString = wordFileHandler.read()             #read String from wordFielHandler
worldFielByte = BytesIO(wordFileString)             #turn String into Bytes
docuement = ZipFile(worldFielByte)                  #unzip it, because all the .docx are zipped to save space
xml_content = docuement.read('word/document.xml')   #read the unzipped file into string

bsObj = BeautifulSoup(xml_content,'html.parser')    #BeautifulSoup也可以用来解析XML
texts= bsObj.findAll("w:t")
for text in texts:
    print(text.get_text())

# Output:
# A Word Document on a Website
# This is a Word document, full of content that you want very much. Unfortunately, it’s difficult to access because I’m putting it on my website as a .
# docx
#  file, rather than just publishing it as HTML