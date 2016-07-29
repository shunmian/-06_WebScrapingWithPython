from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement


driver = webdriver.PhantomJS(executable_path='/Applications/phantomjs-2.1.1-macosx 2/bin/phantomJS')
driver.get("http://pythonscraping.com/pages/itsatrap.html")

links = driver.find_elements_by_tag_name("a")

for link in links:
    if not link.is_displayed():
        print("A trap link: %s" % link.get_attribute("href"))

inputs = driver.find_elements_by_tag_name("input")
for input in inputs:
    if not input.is_displayed():
        print("A trap input: %s" % input.get_attribute("name"))

# output
# A trap link: http://pythonscraping.com/dontgohere
# A trap input: phone
# A trap input: email
