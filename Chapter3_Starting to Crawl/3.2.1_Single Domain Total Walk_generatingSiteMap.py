from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import re

pages = set()

def getInternalLinks(inputUrl):
    inputUrl
    htmlHandler = urlopen(inputUrl)
    bsObject = BeautifulSoup(htmlHandler.read(), "html.parser")

    try:
        for link in bsObject.findAll("a",href=re.compile("(https:\/\/www\.flinhong\.com)[^#]*$")):
            url = link.attrs['href']
            if url is not None:
                if url not in pages:
                    print(url)
                    pages.add(url)
                    getInternalLinks(url)
    except HTTPError as e:
        print(e)

getInternalLinks("https://www.flinhong.com/")

print("finished")
print("totla number of internal pages: ", len(pages))

# Output: 4个页面
# index.html
# research.html
# facilities.html
# vacancies.html
# finished
# totla number of internal pages:  4
