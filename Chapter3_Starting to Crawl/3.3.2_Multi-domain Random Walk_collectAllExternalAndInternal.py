from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
from urllib.error import HTTPError
import re
import datetime
import random




random.seed(datetime.datetime.now())

#Retrieves a list of all Internal link found  on a page
def getInternalLinks(bsObj,includeUrl):
    internalLinks = []
    #Finds all links that begin with a "/",.
    #| alternation in Regex has lowest priority,
    #the engine will match everything to the left of the bar, or the right of the bar
    #也就是以/开头,或者以includeUrl开头
    for link in bsObj.findAll("a", href=re.compile("^(/|.*" + includeUrl + ")[^#]*$")):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in internalLinks:
                internalLinks.append(link.attrs['href'])
    return internalLinks


# Retrieves a list of all External link found  on a page
def getExternalLinks(bsObj, excludeUrl):
    externalLinks = []
    # Finds all links that start with "http" or "www"
    # (((非excludeUrl)后面跟任何word)0或者1次)结尾的
    for link in bsObj.findAll("a", href=re.compile("^(http|www)((?!" + excludeUrl + ").)*$")):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in externalLinks:
                externalLinks.append(link.attrs['href'])
    return externalLinks

def splitAddress(address):
    if "https://" in address:
        addressParts = address.replace("https://","").split("/")
    else:
        addressParts = address.replace("http://", "").split("/")
    return addressParts

def getRandomExternalLink(startingPage):
    request = Request(startingPage, headers={'User-Agent': 'Mozilla/5.0'})
    html = urlopen(request)
    bsObj = BeautifulSoup(html,"html.parser")
    externalLinks = getExternalLinks(bsObj,splitAddress(startingPage)[0])
    if len(externalLinks) == 0:
        internalLinks = getInternalLinks(bsObj,startingPage)
        if len(internalLinks) == 1:
            return getRandomExternalLink(internalLinks[0])
        else:
            return getRandomExternalLink(internalLinks[random.randint(0,len(internalLinks)-1)])
    elif len(externalLinks) == 1:
        return externalLinks[0]
    else:
        return externalLinks[random.randint(0,len(externalLinks)-1)]

def validateUrl(address):
    validateAddress = address
    if address.startswith("//",0,2):
        validateAddress = "https:" + address
    elif address.startswith("/",0,2):
        validateAddress = "https://www.oreilly.com" + address
    return validateAddress

allExtLinks = set()
allIntLinks = set()

def getAllExternalAndInternalLink(siteUrl):
    try:
        request = Request(siteUrl, headers={'User-Agent': 'Mozilla/5.0'})
        html = urlopen(request)
        bsObj = BeautifulSoup(html,"html.parser")
        internalLinks = getInternalLinks(bsObj,splitAddress(siteUrl)[0])
        externalLinks = getExternalLinks(bsObj,splitAddress(siteUrl)[0])

        for link in externalLinks:
            if link not in allExtLinks:
                allExtLinks.add(link)
                print(link)
        for link in internalLinks:
            if link not in allIntLinks:
                allIntLinks.add(link)
                print("About to get link: " +validateUrl(link))
                getAllExternalAndInternalLink(validateUrl(link))
    except HTTPError as e:
        print(e)

def followExternalOnly(startingSite):
    externalLink = getRandomExternalLink(startingSite)
    print("Random external link is: "+externalLink)
    followExternalOnly(externalLink)

getAllExternalAndInternalLink("https://www.flinhong.com/")
print("https://www.flinhong.com/, external link number: ",len(allExtLinks))
print("https://www.flinhong.com/, internal link number: ",len(allIntLinks))

# print("//oreilly.com")
#
# print(validateUrl("//oreilly.com"))

#Output:
# https://www.flinhong.com/, external link number:  103
# https://www.flinhong.com/ internal link number:  68