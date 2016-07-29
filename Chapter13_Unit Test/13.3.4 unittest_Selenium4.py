from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver import ActionChains

driver = webdriver.PhantomJS(executable_path='/Applications/phantomjs-2.1.1-macosx 2/bin/phantomJS')
driver.get('http://pythonscraping.com/')

driver.get_screenshot_as_file('tmp/pythonscraping.png')

#seems not work?