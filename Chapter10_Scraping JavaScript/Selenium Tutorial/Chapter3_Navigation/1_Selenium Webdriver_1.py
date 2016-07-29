from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



driver = webdriver.Chrome(executable_path="/Users/LAL/PycharmProjects/Python/WebScrapingWithPython/Chapter10_Scraping JavaScript/Selenium Tutorial/chromedriver")

driver.get("http://www.google.com")

print(driver.title)

inputElement = driver.find_element_by_name("q")

inputElement.send_keys("cheese!")


try:
    WebDriverWait(driver,10).until(EC.title_contains("cheese!"))
    print(driver.title)

finally:
    print("chrome task finished")
#
# driver.back()
