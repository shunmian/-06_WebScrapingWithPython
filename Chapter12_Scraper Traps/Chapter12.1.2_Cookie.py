from selenium import webdriver

driver = webdriver.PhantomJS(executable_path='/Applications/phantomjs-2.1.1-macosx 2/bin/phantomJS')
driver.get("http://pythonscraping.com")
driver.implicitly_wait(1)

print(driver.get_cookies())



# output
# [{'name': '_gat', 'secure': False, 'path': '/', 'value': '1', 'expiry': 1469629021, 'domain': '.pythonscraping.com', 'httponly': False, 'expires': '周三, 27 7月 2016 14:17:01 GMT'}, {'name': '_ga', 'secure': False, 'path': '/', 'value': 'GA1.2.491484311.1469628421', 'expiry': 1532700421, 'domain': '.pythonscraping.com', 'httponly': False, 'expires': '周五, 27 7月 2018 14:07:01 GMT'}, {'name': 'has_js', 'secure': False, 'path': '/', 'value': '1', 'domain': 'pythonscraping.com', 'httponly': False}]
