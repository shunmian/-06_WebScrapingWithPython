import json
from urllib.request import urlopen

def getCountry(ipAddress):
    JSONFileHandler = urlopen("http://freegeoip.net/json/"+ipAddress)   #获取JSONFile句柄
    JSONFileString = JSONFileHandler.read().decode('utf-8')             #用UTF-8读取成String
    responseJSON = json.loads(JSONFileString)                           #json模块loads该String
    return responseJSON.get("country_code")                             #获取其"country_code"对应的内容。

print(getCountry("168.70.77.50"))

#Output:
#HK


jsonString = '{"arrayOfNums":[{"number":0},{"number":1},{"number":2}],"arrayOfFruits":[{"fruit": "apple"}, {"fruit": "banana"},{"fruit": "pear"}]}'
jsonObj = json.loads(jsonString)
print(jsonObj.get("arrayOfNums"))
print(jsonObj.get("arrayOfNums")[1])
print(jsonObj.get("arrayOfNums")[1].get("number") + jsonObj.get("arrayOfNums")[2].get("number"))
print(jsonObj.get("arrayOfFruits")[2].get("fruit"))

# Output:
# [{'number': 0}, {'number': 1}, {'number': 2}]
# {'number': 1}
# 3
# pear

