# from selenium import webdriver
# import time
# from selenium.webdriver.remote.webelement import WebElement
# from selenium.common.exceptions import StaleElementReferenceException
#
# def waitForLoad(driver):
#     elem = driver.find_element_by_tag_name("html")
#     count = 0
#     while True:
#         count += 1
#         if count > 20:
#             print("Timing out after 10 seconds and returning")
#             return
#         time.sleep(1)
#         try:
#             elem == driver.find_element_by_tag_name("html")
#         except StaleElementReferenceException:
#             print("original html disappear")
#             return
# driver = webdriver.PhantomJS(executable_path='/Applications/phantomjs-2.1.1-macosx 2/bin/phantomjs')
# driver.get("http://pythonscraping.com/pages/javascript/redirectDemo1.html")
# waitForLoad(driver)
# print(driver.page_source)


from selenium import webdriver
import time
from selenium.common.exceptions import StaleElementReferenceException

def waitForLoad(driver):
    elem = driver.find_element_by_tag_name("html")
    print("orignal html:%s" %elem)
    count = 0
    while True:
        count += 1
        if count > 20:
            print("Timing out after 10 seconds and returning")
            return
        time.sleep(1)
        try:
            elem == driver.find_element_by_tag_name("html")
        except StaleElementReferenceException:
            print("original page disappear")
            return

driver = webdriver.PhantomJS(executable_path='/Applications/phantomjs-2.1.1-macosx 2/bin/phantomjs')
driver.get("http://pythonscraping.com/pages/javascript/redirectDemo1.html")
waitForLoad(driver)
print(driver.page_source)