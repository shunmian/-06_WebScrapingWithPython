from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import string
from collections import OrderedDict

# items = {
#     ('A','aaa'):1,
#     ('B','bbb'):2,
#     ('c','ccc'):3,
#     ('B','bbb'):4
# }
#
# orderedDic = OrderedDict(sorted(items.items(), key =lambda i:i[1], reverse = True))
# print(orderedDic)
#
# items = (
#     ('A','aaa'),
#     ('B','bbb'),
#     ('c','ccc'),
#     ('B','bbb')
# )
#
# orderedDic = OrderedDict(sorted(items, key =lambda i:i[1], reverse = True))
# print(orderedDic)

items =(
    ('A',1),
    ('B',2),
    ('C',3)
)
print(items)

regular_dict = dict(items)
print(regular_dict)
ordered_dict = OrderedDict(items)
print(ordered_dict.keys())
print(ordered_dict.values())
print(ordered_dict)
#
#
#
#
# #Output
# # ['This', 'article']
# # ['article', 'is']
# # ['is', 'about']
# # ['about', 'the']
# # ['the', 'programming']
# # ['programming', 'language']
# # ['language', 'For']

