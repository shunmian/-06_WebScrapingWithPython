from urllib.request import urlopen
from bs4 import BeautifulSoup
import pymysql


connection = pymysql.connect(host='127.0.0.1', unix_socket='/tmp/mysql.sock',
                        user='root', passwd='640401', db='mysql', charset='utf8')
cursor = connection.cursor()
cursor.execute("USE wikipedia")

class SolutionFound(RuntimeError):
    def __init__(self,message):
        self.message = message

def getLinks(fromgPageID):
    cursor.execute("SELECT toPageID from links where fromPageID = %s",(fromgPageID))
    if cursor.rowcount == 0:
        return None
    else:
        # the results row only contains toPageID, thus the first item is selected
        return [x[0] for x in cursor.fetchall()]

def constructDict(curentPageID):
    links = getLinks(curentPageID)
    if links:
        # zip key list and value list(item is dictionary) into a dictionary
        return dict(zip(links,[{}]*len(links)))
    return {}

#The link tree may either be empty or contain multiple links

def searchDepth(targetPageID, currentPageID, linkTree, depth):

    if depth == 0:
        #Stop recursing and return, regardless
        return linkTree

    if not linkTree:
        linkTree = constructDict(currentPageID)
        if not linkTree:
            #No links found. Cannot continue at this code
            return {}

    if targetPageID in linkTree.keys():
        print("TARGET " + str(targetPageID) + " Found!")
        raise SolutionFound("Page: " + str(currentPageID))

    for branchKey, branchValue in linkTree.items():
        try:
            #Recurse here to continue building the tree
            linkTree[branchKey] = searchDepth(targetPageID,branchKey,branchValue,depth-1)
        except SolutionFound as e:
            print(e.message)
            raise SolutionFound("PAGE: " + str(currentPageID))
    return linkTree


try:
    searchDepth(18885,1,{},4)
    print("No Solution FOund")
except SolutionFound as e:
    print(e.message)

#Output
# TARGET 18885 Found!   //Terry_Jones
# Page: 18830           //Douglas_Adams
# PAGE: 3               //San_Diego_Comic-Con_International
# PAGE: 1               //Kevin Bacon
# 即Kevin Bacon -> San_Diego_Comic-Con_International -> Douglas Adams -> Terry Jones