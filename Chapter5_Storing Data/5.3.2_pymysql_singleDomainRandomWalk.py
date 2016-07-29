import pymysql
from urllib.request import urlopen
from bs4 import BeautifulSoup
import datetime
import random
import re

connection = pymysql.connect(host       ='127.0.0.1',
                             unix_socket='/tmp/mysql.sock',
                             user       ='root',
                             password   ='640401',
                             charset    ='utf8')

cursor = connection.cursor()
cursor.execute("USE scraping")

random.seed(datetime.datetime.now())

def store(title, content):
    '''
    :param title: if title already exist, return, else store
    :param content:
    :return:
    '''

    #use encaosulate string with \"%s\" tackles the NULL tiltle(otherwise error appear), why?
    cursor.execute("SELECT * FROM pages WHERE title=\"%s\"", title)
    if(len(cursor.fetchall()) > 0):
        return;
    else:
        # the title and content should be 'title' and 'content' in the
        cursor.execute("INSERT INTO pages (title,content) VALUES (\"%s\",\"%s\")",(title,content))
        cursor.connection.commit()

def getLinks(articalUrl):
    htmlFileHandler = urlopen("https://en.wikipedia.org" + articalUrl)
    bsObj = BeautifulSoup(htmlFileHandler.read(),"html.parser")
    title = bsObj.find("h1",{"id":"firstHeading"}).string
    content = bsObj.find("div",id="mw-content-text").find('p').get_text()
    print(content[0:100])
    store(title, content[0:100])

    return bsObj.find("div",{"id":"bodyContent"}).findAll("a",href=re.compile("^(/wiki/)((?!:).)*$"))

links = getLinks("/wiki/Kevin_Bacon")
try:
    while(len(links)>0):
        newArticleHref = links[random.randint(0,len(links)-1)].attrs["href"]
        print(newArticleHref)
        getLinks(newArticleHref)

finally:
    cursor.close()
    connection.close()




#Output:
# +-----+------------------------------+------------------------------------------------------------------------------------------------------------------+---------------------+
# | id  | title                        | content                                                                                                          | created             |
# +-----+------------------------------+------------------------------------------------------------------------------------------------------------------+---------------------+
# | 119 | 'Kevin Bacon'                | 'Kevin Norwood Bacon[1] (born July 8, 1958)[2] is an American actor and musician whose films include '           | 2016-07-20 22:18:52 |
# | 120 | 'Kathleen Quinlan'           | 'Kathleen Denise Quinlan (born November 19, 1954) is an American film and television actress. She rec'           | 2016-07-20 22:18:54 |
# | 121 | 'Andrew Lincoln'             | 'Andrew James Clutterbuck (born 14 September 1973),[1] better known by his stage name Andrew Lincoln,'           | 2016-07-20 22:19:00 |
# | 122 | 'Kevin Costner'              | 'Kevin Michael Costner (born January 18, 1955) is an American actor, film director, producer, musicia'           | 2016-07-20 22:19:03 |
# | 123 | 'Jamie Foxx'                 | 'Eric Marlon Bishop (born December 13, 1967),[1] known professionally by his stage name Jamie Foxx, i'           | 2016-07-20 22:19:07 |
# | 124 | 'Ménage à trois'             | 'A ménage à trois (French for "household of three") is a domestic arrangement in which three people h'           | 2016-07-20 22:19:08 |
# | 125 | 'He Said, She Said'          | 'He Said, She Said is a 1991 American romantic comedy directed by Ken Kwapis and Marisa Silver and st'           | 2016-07-20 22:19:09 |
