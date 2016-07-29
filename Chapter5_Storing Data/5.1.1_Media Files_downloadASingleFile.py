from urllib.request import urlretrieve
from urllib.request import urlopen
from bs4 import BeautifulSoup

htmlHandler = urlopen("http://www.pythonscraping.com")
bsObj = BeautifulSoup(htmlHandler.read(),"html.parser")
imageUrl = bsObj.find("a",{"id": "logo"}).find("img").attrs["src"]

urlretrieve(imageUrl, "logo.jpg")   #a URL, filename in the same directory that the script is running from

