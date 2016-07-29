import os
import csv
from bs4 import BeautifulSoup

from urllib.request import urlopen

def getCSVPath(directory,filename):
    if not os.path.exists(directory):
        os.makedirs(directory)
    return os.getcwd()+"/"+directory+"/" + filename

htmlFileHandler = urlopen("https://en.wikipedia.org/wiki/Comparison_of_text_editors")
bsObj = BeautifulSoup(htmlFileHandler.read(),"html.parser")
tableTag = bsObj.findAll("table",{"class":"wikitable"})[0]
rowTags = tableTag.findAll("tr")

path = getCSVPath("CSV","test.csv")
try:
    csvFile = open(path,'w+')
    writer=csv.writer(csvFile)

    for rowTag in rowTags:
        csvRow=[]
        for cell in rowTag.findAll(('td','th')): #输出所有的td或者th Tag
            csvRow.append(cell.string)
        writer.writerow(csvRow)
finally:
    csvFile.close()


