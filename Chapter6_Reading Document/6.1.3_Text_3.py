from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://en.wikipedia.org/wiki/Python_(programming_language)")
bsObj = BeautifulSoup(html,"html.parser")
content = bsObj.find("div", {"id":"mw-content-text"}).get_text()
# content = bytes(content, "UTF-8")  #先转回二进制数
# content = content.decode("UTF-8")  #再用UTF-8解码

print(content)




