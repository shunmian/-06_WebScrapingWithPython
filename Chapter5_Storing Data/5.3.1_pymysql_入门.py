import pymysql

#1.1 create connection object
connection = pymysql.connect(host='127.0.0.1', unix_socket='/tmp/mysql.sock',user='root',password='640401',db='mysql')
#1.2 create cursor object
cursor = connection.cursor()
#2.1 xecyte SQL
cursor.execute("USE scraping")
cursor.execute("SELECT * FROM pages WHERE title LIKE 'title%'")
#2.2 获取data
for row in cursor.fetchall():
    print(row)

#3.1 close cursor
cursor.close()
#3.2 close connection
connection.close()


#Output:
# (4, 'title1', 'content1', datetime.datetime(2016, 7, 20, 17, 32, 36))
# (5, 'title2', 'content2', datetime.datetime(2016, 7, 20, 17, 32, 36))
# (6, 'title6', 'content6', datetime.datetime(2016, 7, 20, 17, 55, 35))
# (7, 'title7', 'content7', datetime.datetime(2016, 7, 20, 17, 55, 35))
