from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import re
import datetime
import random


pages = set()
random.seed(datetime.datetime.now())

#Retrieves a list of all Internal link found  on a page
def getInternalLinks(bsObj,includeUrl):
    internalLinks = []
    #Finds all links that begin with a "/",.
    #| alternation in Regex has lowest priority,
    #the engine will match everything to the left of the bar, or the right of the bar
    #也就是以/开头,或者以includeUrl开头
    for link in bsObj.findAll("a", href=re.compile("^(/|.*" + includeUrl + ")")):
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


def followExternalOnly(startingSite):
    externalLink = getRandomExternalLink(startingSite)
    print("Random external link is: "+externalLink)
    followExternalOnly(externalLink)

followExternalOnly("http://www.hku.hk")

#Output:
# Random external link is: http://fb.com/hkusa.dseteam
# Random external link is: https://www.facebook.com/hkusa.dseteam/?fref=nf
# Random external link is: http://l.facebook.com/l.php?u=http%3A%2F%2Fcablenews.i-cable.com%2Fwebapps%2Fsuddenfeed.php&h=UAQGaDwNJAQH7di2k2m3G19odhGe1MEunTAthBzkXaMsUAQ&enc=AZNOiAMBe59qZ0jRPRiqmNencoTWzwuMkWs-480Z9NNJ78urS-e7XaFgUcqdaKAfUJZDefYazVfXLpmeCIb4ou8CITstxOA29I8jzl6KVBi5FRfh3RcQe1cUoNfZX1VLpvxcZyAje0KDlCZJ1fJGiLtW9jDS4LmwrE9_aE4gZy9n1TplJ4IJdAj_lxqXZ5hOmPAsDHzxt-B6Smo8HNBOuRgR&s=1
# Random external link is: https://developers.facebook.com/?ref=pf
# Random external link is: https://www.facebook.com/seth.rosenberg
# Random external link is: https://id-id.facebook.com/seth.rosenberg
# ...
