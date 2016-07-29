import requests
from requests.auth import HTTPBasicAuth

auth = HTTPBasicAuth('Jo','password')
r = requests.post("http://pythonscraping.com/pages/auth/login.php",auth=auth)
print(r.text)

#Output:
# <p>Hello Jo.</p><p>You entered password as your password.</p>