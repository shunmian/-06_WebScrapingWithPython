
from twitter import *

ACCESS_TOKEN = "3062948827-ecvv0bF84IifTgUsnhdtqdH9TBc4rr4JDAmwWqz"
ACCESS_SECRET = "Imrqc6nxI5SZpSpGoVSUoGa3LzrLtXLxlegsry2qcrdIV"
CONSUMER_KEY = "aEXFq0NbW7Jf9mhs9Xft7CEQb"
CONSUMER_SECRET = "hUWXGatZzUHfcvGJnp2K8C0OBGyqk97aV7oulkRmzNmlnS9ze5"


t = Twitter(auth=OAuth(ACCESS_TOKEN,ACCESS_SECRET,CONSUMER_KEY,CONSUMER_SECRET))
'''
任务1:搜索tweets
pythonTweets = t.search.tweets(q = "#python")
print(pythonTweets)
'''

'''
任务2:发布Twitter
statusUpdate = t.statuses.update(status="Hello, world!!!")
print(statusUpdate)
'''

'''
任务3:搜索特定用户的tweets
pythonStatuses = t.statuses.user_timeline(screen_name="montypython",count=5)
print(pythonStatuses)
'''


