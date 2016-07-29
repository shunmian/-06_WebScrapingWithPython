from urllib.request import urlopen
import pymysql
from bs4 import BeautifulSoup
import re

connection = pymysql.connect(host       ='127.0.0.1',
                             unix_socket='/tmp/mysql.sock',
                             user       ='root',
                             password   ='640401',
                             charset    ='utf8')

cursor = connection.cursor()
cursor.execute("USE wikipedia")

def insertPageIfNotExists(url):
    '''
    :param url: if url already exist, return its id; else insert first, then return its id
    :return: id
    '''

    #use encaosulate string with \"%s\" tackles the NULL tiltle(otherwise error appear), why?
    cursor.execute("SELECT * FROM pages WHERE url=%s", url)
    if cursor.rowcount == 0:
        # the title and content should be 'title' and 'content' in the
        cursor.execute("INSERT INTO pages (url) VALUES (%s)", url)
        cursor.connection.commit()
        return cursor.lastrowid
    else:
        return cursor.fetchone()[0];


def insertLink(fromPageId,toPageId):
    '''
    :param fromPageId,toPageId: if (fromPageId,toPageId) not exist, insert into links table
    :return:
    '''

    #use encaosulate string with \"%s\" tackles the NULL tiltle(otherwise error appear), why?
    cursor.execute("SELECT * FROM links WHERE fromPageId=%s AND toPageId=%s", (int(fromPageId),int(toPageId)))
    if cursor.rowcount == 0:
        # the title and content should be 'title' and 'content' in the
        cursor.execute("INSERT INTO links (fromPageId,toPageId) VALUES (%s,%s)", (fromPageId,toPageId))
        cursor.connection.commit()
    else:
        return;

pages = set()

def getLinks(pageUrl,recursionLevel):
    global pages
    # 大于4的pageUrl扔掉
    if recursionLevel > 4:
        return
    pageId = insertPageIfNotExists(pageUrl)
    print(pageId,type(pageId))
    htmlFileHandler = urlopen("https://en.wikipedia.org" + pageUrl)
    bsObj = BeautifulSoup(htmlFileHandler.read(),"html.parser")
    linkTags = bsObj.find("div",{"id":"bodyContent"}).findAll("a",href=re.compile("^(/wiki/)((?!:).)*$"))

    for linkTag in linkTags:
        linkHref = linkTag.attrs["href"]
        insertLink(pageId,insertPageIfNotExists(linkHref))
        if linkHref not in pages:
            pages.add(linkHref)
            getLinks(linkHref,recursionLevel+1)

try:
    getLinks("/wiki/Kevin_Bacon",0)
finally:
    cursor.close()
    connection.close()


#Output:

# mysql> SELECT * FROM pages;
# +----+-----------------------------------------+---------------------+
# | id | url                                     | created             |
# +----+-----------------------------------------+---------------------+
# |  1 | /wiki/Kevin_bacon                       | 2016-07-20 23:11:47 |
# |  2 | /wiki/Kevin_Bacon_(disambiguation)      | 2016-07-20 23:12:49 |
# |  3 | /wiki/San_Diego_Comic-Con_International | 2016-07-20 23:24:33 |
# |  4 | /wiki/Comic_Con_(disambiguation)        | 2016-07-20 23:24:47 |
# +----+-----------------------------------------+---------------------+
# 3 rows in set (0.00 sec)
#
# mysql> SELECT * FROM links;
# +-----+------------+----------+---------------------+
# | id  | fromPageId | toPageId | created             |
# +-----+------------+----------+---------------------+
# |   1 |          1 |        2 | 2016-07-20 23:24:24 |
# |   2 |          2 |        1 | 2016-07-20 23:24:25 |
# |   3 |          1 |        3 | 2016-07-20 23:24:33 |
# |   4 |          3 |        4 | 2016-07-20 23:24:47 |
# |   5 |          4 |        3 | 2016-07-20 23:24:48 |
# |   6 |          4 |        5 | 2016-07-20 23:24:48 |
# |   7 |          4 |        6 | 2016-07-20 23:24:48 |
# |   8 |          4 |        7 | 2016-07-20 23:24:48 |
# |   9 |          4 |        8 | 2016-07-20 23:24:48 |
# |  10 |          4 |        9 | 2016-07-20 23:24:48 |
# |  11 |          4 |       10 | 2016-07-20 23:24:48 |
# |  12 |          4 |       11 | 2016-07-20 23:24:48 |
# |  13 |          4 |       12 | 2016-07-20 23:24:48 |
# +-----+------------+----------+---------------------+
