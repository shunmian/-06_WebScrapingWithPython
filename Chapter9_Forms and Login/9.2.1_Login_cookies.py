import requests

params = {'username': 'Johnson','password':'password'}
r = requests.post("http://pythonscraping.com/pages/cookies/welcome.php",params)
print("Cookie is set to:")
print(r.cookies.get_dict())
print('-------------')
print("Going to profile page...")

r = requests.get("http://pythonscraping.com/pages/cookies/profile.php", cookies=r.cookies)
print(r.text)

#Output:
# Cookie is set to:
# {'loggedin': '1', 'username': 'Johnson'}
# -------------
# Going to profile page...
# Hey Johnson! Looks like you're still logged into the site!