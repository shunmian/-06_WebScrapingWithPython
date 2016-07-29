from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import json
import re
import datetime
import random



def getArticalTags(inputUrl):

    url = "https://en.wikipedia.org" + inputUrl
    htmlHandler = urlopen(url)
    bsObject = BeautifulSoup(htmlHandler.read(), "html.parser")

    return bsObject.find("div",{"id":"bodyContent"}).findAll("a",href=re.compile("^(\/wiki)((.(?!:))*)$"))

def getHistoryIPs(articalUrl):
    # articalUrl="/wiki/Six_Degrees_of_Kevin_Bacon"

    # revision history page pattern
    # https://en.wikipedia.org/w/index.php?title=Kevin_Bacon&action=history
    # https://en.wikipedia.org/w/index.php?title=Six_Degrees_of_Kevin_Bacon&action=history
    title = articalUrl.replace("/wiki/","")
    print("revision history of ",title," -------------------------")
    revisionPageUrl = "https://en.wikipedia.org/w/index.php?title="+title+"&action=history"

    htmlHandler = urlopen(revisionPageUrl)
    bsObject = BeautifulSoup(htmlHandler.read(), "html.parser")
    IPs= set()
    for IPTag in bsObject.find("ul",{"id":"pagehistory"}).findAll("a",{"class":"mw-anonuserlink"}):
        if IPTag.string not in IPs:
            IPs.add(IPTag.string)
    return IPs

def getIPCountry(IP):
    JSONFileHandler = urlopen("http://freegeoip.net/json/" + IP)
    JSONFileString = JSONFileHandler.read().decode('utf-8')
    JSONObject = json.loads(JSONFileString)
    IPCountry = JSONObject.get('country_name')
    return IPCountry



def start(startPage):
    articalTags = getArticalTags(startPage)
    for articalTag in articalTags:
        articalLink = articalTag.attrs["href"]
        for IP in getHistoryIPs(articalLink):
            print(IP, " from: ",getIPCountry(IP))

    while(len(articalTags)>0):
        i = random.randint[0,random.randint(len(articalTags)-1)]
        randomArticalTag = articalTags[i]
        start(randomArticalTag)

start("/wiki/Kevin_Bacon")

#Output:
# revision history of  Kevin_Bacon_(disambiguation)  -------------------------
# revision history of  San_Diego_Comic-Con_International  -------------------------
# 70.67.239.79  from:  Canada
# 220.221.249.249  from:  Japan
# 2602:306:b883:4f0:198d:191a:4f08:5b16  from:  United States
# 2600:8801:9604:3900:7273:cbff:fe5c:336d  from:  United States
# 96.250.2.62  from:  United States
# 134.223.230.151  from:  United States
# 126.229.33.149  from:  Japan
# 1.79.84.210  from:  Japan
# 126.204.160.80  from:  Japan
# 91.122.178.55  from:  Russia
# 176.182.35.113  from:  France
# revision history of  Philadelphia  -------------------------