import requests

session = requests.session()

params = {'username': 'John','password':'password'}
s = session.post("http://pythonscraping.com/pages/cookies/welcome.php",params)
print("Cookie is set to:")
print(s.cookies.get_dict())
print('-------------')
print("Going to profile page...")

s = session.get("http://pythonscraping.com/pages/cookies/profile.php")
print(s.text)

#Output:
# Cookie is set to:
# {'loggedin': '1', 'username': 'John'}
# -------------
# Going to profile page...
# Hey John! Looks like you're still logged into the site!