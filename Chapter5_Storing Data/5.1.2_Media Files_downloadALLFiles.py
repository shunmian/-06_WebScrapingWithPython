import os
from urllib.request import urlretrieve
from urllib.request import urlopen
from bs4 import BeautifulSoup

downloadDirectory = "downloaded"
baseUrl = "http://pythonscraping.com"

def getAbsoluteURL(baseUrl,source):
  '''
  :param baseUrl:
  :param source: http://www.pythonscraping.com/misc/jquery.once.js?v=1.2
  :return:       http://pythonscraping.com/misc/jquery.once.js?v=1.2
  '''
    if source.startswith("http://www."):    #去掉www
        url = "http://"+source[11:]
    elif source.startswith("http://"):      #已经去掉www,则不变
        url = source
    elif source.startswith("www."):         #若www.开头,则加http://并去掉www
        url =  "http://"+source[4:]
    else:
        url = baseUrl + "/" + source        #若部分url,则补全
    if baseUrl not in url:                  #去掉外部链接
        return  None
    return  url

def getDownloadPath(baseUrl,absoluteUrl,downloadDirectory):  #dwonloadDirectory是script目录下的文件夹,
  '''
    :param baseUrl:
    :param absoluteUrl: http://pythonscraping.com/misc/jquery.once.js?v=1.2
    :return:            downloaded/misc/jquery.once.js?v=1.2
  '''
    path = absoluteUrl.replace("www.","")
    path = path.replace(baseUrl,"")
    path = downloadDirectory+path
    directory = os.path.dirname(path)

    if not os.path.exists(directory):
        os.makedirs(directory)

    return path

htmlHandler = urlopen("http://www.pythonscraping.com")
bsObj = BeautifulSoup(htmlHandler.read(),"html.parser")
downloadList = bsObj.findAll(src=True)

for download in downloadList:
    fileUrl = getAbsoluteURL(baseUrl,download.attrs["src"])
    if fileUrl is not None:
        print(fileUrl)
        urlretrieve(fileUrl, getDownloadPath(baseUrl,fileUrl,downloadDirectory))

