import socks
import socket
from urllib.request import urlopen
from selenium import webdriver

#method 1
socks.set_default_proxy(socks.SOCKS5,"localhost",9150)
socket.socket = socks.socksocket
print(urlopen("http://icanhazip.com").read())

#method 2 combine with selenium
service_args = ['--proxy=localhost:9150', '--proxy-type=socks5', ]
driver = webdriver.PhantomJS(executable_path='/Applications/phantomjs-2.1.1-macosx 2/bin/phantomJS',service_args=service_args)
driver.get("http://icanhazip.com")
print(driver.page_source)

driver.close()