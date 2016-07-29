from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import re


# def getNames(url):
#     try:
#         htmlHandler = urlopen(url)
#     except HTTPError as e:
#         print(e)
#         return None
#
#     try:
#         bsObj = BeautifulSoup(htmlHandler.read(), "html.parser")
#         names = bsObj.findAll("img", {"src": re.compile("\.\.\/img\/gifts\/img.*\.jpg")})
#     except AttributeError as e:
#         return None
#     return names
#
# names = getNames("http://www.pythonscraping.com/pages/warandpeace.html")
#
# if names == None:
#     print("title couldn't be found")
# else:
#
#     for img in names:
#      print(img["src"])


# find() and findAll()
# get_text()
# 4 objects in BeautifulSoup: BeautifulSoup object, Tag object, NavigableString object, Commment object
# Navigatiing tree
#    children and descendants
#    siblings
#    parents
# regular expression
# accessing attributes
# lambda Expression

# 2. 搜索文档树-------------------------------------------------------------------------
'''
htmlHandler = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
bsObj = BeautifulSoup(htmlHandler.read(), "html.parser")

print("name:", bsObj.name)                             #name: [document]
print("attrs:", bsObj.attrs)                           #attrs: {}
print("string:", bsObj.string)                         #string: None
print("type:", type(bsObj))                            #type: <class 'bs4.BeautifulSoup'>



people = bsObj.find("span",{"class":"green"})
print(people)                                          #<span class="green">Anna Pavlovna Scherer</span>
print("name:", people.name,type(people.name))          #name: span <class 'str'>
print("attrs:", people.attrs,type(people.attrs))       #attrs: {'class': ['green']} <class 'dict'>
print("string:", people.string,type(people.string))    #string: Anna Pavlovna Scherer <class 'bs4.element.NavigableString'>
print("type:", type(people))                           #type: <class 'bs4.element.Tag'>
'''
'''
#3. 遍历文档树-------------------------------------------------------------------------

htmlHandler = urlopen("http://www.pythonscraping.com/pages/page3.html")
bsObj = BeautifulSoup(htmlHandler.read(), "html.parser")

print(bsObj.find("img",{"src":"../img/gifts/img1.jpg"}).parent.previous_sibling.get_text())

# for child in bsObj.find("table",{"id":"giftList"}).tr.next_siblings:
#     print(child)
'''

'''
# 4. Regular Expression-------------------------------------------------------------------------

htmlHandler = urlopen("http://www.pythonscraping.com/pages/page3.html")
bsObj = BeautifulSoup(htmlHandler.read(), "html.parser")

print(bsObj.findAll("img", src=re.compile("\.\./img/gifts/img.*\.jpg")))
'''

'''
# 5. Attribute access-------------------------------------------------------------------------
images= bsObj.findAll("img", src=re.compile("\.\./img/gifts/img.*\.jpg"))
image = images[0]
print(image.attrs['src'])
'''

# 5. Lambda Expression-------------------------------------------------------------------------
htmlHandler = urlopen("http://www.pythonscraping.com/pages/page3.html")
bsObj = BeautifulSoup(htmlHandler.read(), "html.parser")

tagWith2Attrs = bsObj.findAll(lambda tag: len(tag.attrs)==2)
for tag in tagWith2Attrs:
    print(tag.attrs)