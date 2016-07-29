from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import re


driver = webdriver.Chrome(executable_path="/Users/LAL/PycharmProjects/Python/WebScrapingWithPython/Chapter10_Scraping JavaScript/Selenium Tutorial/chromedriver")

driver.get("http://www.htmlcodetutorial.com/forms/_OPTION_SELECTED.html")

element = driver.find_element_by_xpath('//*[@id="node-272"]/div/div[1]/div/div/table[1]/tbody/tr[2]/td[2]/form/select')

select = Select(element)
select.select_by_visible_text("resistor array")
select.submit()
for option in select.options:
    if option.text == "resistor array":
        option.submit()
        break




