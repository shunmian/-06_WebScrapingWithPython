from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup


def getTitle(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        print(e)
        return None

    try:
        bsObj = BeautifulSoup(html.read(), "html.parser")
        title = bsObj.html.body.h1
    except AttributeError as e:
        return None
    return title

title = getTitle("http://www.pythonscraping.com/pages/page1.html")
if title == None:
    print("title couldn't be found")
else:
    print(title)

# htmlHandler = urlopen("http://pythonscraping.com/pages/page1.html")   #获取html文件句柄
# bsObj = BeautifulSoup(htmlHandler.read(),"html.parser")               #读取html文件内容,然后实例化BeautifulSoup
# print(bsObj.h1)                                                       #打印 h1 tag, 完整的是bsObj,html.body.h1
# #输出: <h1>An Interesting Title</h1>