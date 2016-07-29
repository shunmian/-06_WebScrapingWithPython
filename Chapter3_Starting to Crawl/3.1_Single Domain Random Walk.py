from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import re
import datetime
import random

'''
1st datetime is the datetime.py module,
2nd datetime is the datetime class, conventionlly it should be capitalized as class name.
However, the early time doesn't follow this convention.
the now() is the class method, which return an datetime instance.

random is the random.py module

random.seed(time) = random.Random().seed(time),
which create one instance of Random number generator, seeded from current time
'''

random.seed(datetime.datetime.now())


def getArticalTags(inputUrl):

    url = "https://en.wikipedia.org" + inputUrl
    htmlHandler = urlopen(url)
    bsObject = BeautifulSoup(htmlHandler.read(), "html.parser")

    return bsObject.find("div",{"id":"bodyContent"}).findAll("a",href=re.compile("^(\/wiki)((.(?!:))*)$"))

articleTagList = getArticalTags("/wiki/Kevin_Bacon")

while(len(articleTagList) > 0):
    i = random.randint(0,len(articleTagList)-1)
    articleUrl = articleTagList[i].attrs["href"]
    print(articleUrl)
    articleTagList=getArticalTags(articleUrl)


# /wiki/Murder_in_the_First_(film)
# /wiki/Henri_Young
# /wiki/Henry_Young_(disambiguation)
# /wiki/Henry_Young_(major)
# /wiki/Union_Army
# /wiki/Department_of_the_Monongahela
# /wiki/Belmont_County,_Ohio

