from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains

driver = webdriver.PhantomJS(executable_path='/Applications/phantomjs-2.1.1-macosx 2/bin/phantomJS')
driver.get("http://pythonscraping.com/pages/files/form.html")


firstname = driver.find_element_by_name("firstname")
lastname = driver.find_element_by_name("lastname")
button = driver.find_element_by_id("submit")


# method1
firstname.send_keys("John")
lastname.send_keys("snow")
button.click()
print(driver.page_source)

# method2
actionChains = ActionChains(driver)
actionChains.click(firstname).send_keys("John").click(lastname).send_keys("snow").send_keys(Keys.RETURN)
actionChains.perform()
print(driver.page_source)