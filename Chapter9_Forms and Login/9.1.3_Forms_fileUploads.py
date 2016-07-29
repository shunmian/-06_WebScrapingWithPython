import requests

files = {'uploadFile': open('logo.jpg', 'rb')}
r = requests.post("http://pythonscraping.com/pages/processing2.php",files=files)
print(r.text)

#Output:
# The file logo.jpg has been uploaded. <a href="/pages/uploads/logo.jpg">Link</a>