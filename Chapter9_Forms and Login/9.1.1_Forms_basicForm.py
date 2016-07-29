import requests

params = {'firstname': 'Ryan', 'lastname':'Mitchell'}
#注意,post的一个参数是真正执行post的网页,这里是form html里的<form>的action的值
r = requests.post("http://pythonscraping.com/pages/files/processing.php", data=params)
print(r.text)

#Output:
# Hello there, Ryan Mitchell!