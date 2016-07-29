from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import re

from selenium.webdriver import  ActionChains


driver = webdriver.Chrome(executable_path="/Users/LAL/PycharmProjects/Python/WebScrapingWithPython/Chapter10_Scraping JavaScript/Selenium Tutorial/chromedriver")

driver.get("http://www.w3schools.com/html/html5_draganddrop.asp")

source = driver.find_element_by_id('div1')
target = driver.find_element_by_id('div2')
action_chains = ActionChains(driver)
action_chains.drag_and_drop(source,target).perform()




