from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import re

from selenium.webdriver import  ActionChains


driver = webdriver.Chrome(executable_path="/Users/LAL/PycharmProjects/Python/WebScrapingWithPython/Chapter10_Scraping JavaScript/Selenium Tutorial/chromedriver")

driver.get("http://www.hku.hk/")

loginElement = driver.find_element_by_class_name("login-to-hku")
loginElement.click()



def switchToWindow(title):
    handles = driver.window_handles
    for handle in handles:
        driver.switch_to_window(handle)
        if driver.title == title:
            break


title1 = "The University of Hong Kong (HKU)"
title2 = "HKU Portal"

switchToWindow(title2)

#
# driver.switchTo().frame(driver.find_element_by_css_selector("iframe[title='The University of Hong Kong (HKU)']"))
