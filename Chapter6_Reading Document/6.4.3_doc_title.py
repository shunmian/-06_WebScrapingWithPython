from urllib.request import urlopen
from zipfile import ZipFile
from io import BytesIO
from bs4 import BeautifulSoup

wordFileHandler = urlopen("http://pythonscraping.com/pages/AWordDocument.docx")
wordFileString = wordFileHandler.read()             #read String from wordFielHandler
worldFielByte = BytesIO(wordFileString)             #turn String into Bytes
docuement = ZipFile(worldFielByte)                  #unzip it, because all the .docx are zipped to save space
xml_content = docuement.read('word/document.xml')   #read the unzipped file into string,存储为word/document.xml文件。

bsObj = BeautifulSoup(xml_content,'html.parser')    #BeautifulSoup也可以用来解析XML

textTags= bsObj.findAll("w:t")
for textTag in textTags:
    try:
        titleTag = textTag.parent.previousSibling.find("w:pstyle",{"w:val": "Title"})
        if titleTag is not None:
            print("<h1>",textTag.text,"</h1>")
    except AttributeError:
        pass


# Output:
# <h1> A Word Document on a Website </h1>