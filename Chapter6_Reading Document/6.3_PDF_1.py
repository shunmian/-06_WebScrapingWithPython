from urllib.request import urlopen
from pdfminer.pdfinterp import PDFResourceManager, process_pdf
from pdfminer.layout import LAParams
from pdfminer.converter import TextConverter
from io import StringIO


def readPDF(pdfFile):
    resourceManager = PDFResourceManager()
    retstr = StringIO()
    laparams = LAParams()
    device = TextConverter(resourceManager,retstr,laparams=laparams)

    process_pdf(resourceManager,device,pdfFile)
    device.close()

    content = retstr.getvalue()
    retstr.close()
    return content

pdfFile = urlopen("http://pythonscraping.com/pages/warandpeace/chapter1.pdf")
# you can change the pdfFile from local path
# pdfFile = open("chapter1.pdf",'rb')
outputString = readPDF(pdfFile)
print(outputString)
pdfFile.close()

# Output:
# CHAPTER I
#
# "Well, Prince, so Genoa and Lucca are now just family estates of
# theBuonapartes. But I warn you, if you don't tell me that this

