# import time
# from urllib.request import urlretrieve
# from selenium import  webdriver
#
#
#
# from PIL import Image
# import pytesseract
#
#
# driver = webdriver.Chrome(executable_path="/Applications/chromedriver")
# driver.get("http://www.amazon.com/War-Peace-Leo-Nikolayevich-Tolstoy/dp/1427030200")
# time.sleep(2)
#
# driver.find_element_by_id("sitbLogoImg").click()
#
#
#
#
# def cleanFile(filePath,newFilePath):
#
#     image = Image.open(filePath)
#
#     #Set a threshold value for the image, and save
#     image = image.point(lambda x:0 if x<143 else 255)
#     image.save(newFilePath)
#     return image
#
# image = cleanFile('text2.png','text3_cleaned.png')
# string = pytesseract.image_to_string(image)
# print(string)
#
#
# # output
# # This IS some text‘ wntten In Anal, that will be readby
# # Tesseract Here are some symbols: !@#$%"&'()


import time
from urllib.request import urlretrieve
import subprocess
from selenium import webdriver

#driver = webdriver.PhantomJS(executable_path='/Users/ryan/Documents/pythonscraping/code/headless/phantomjs-1.9.8-macosx/bin/phantomjs')
driver = webdriver.Chrome(executable_path="/Applications/chromedriver")
url = "https://www.amazon.com/War-Peace-Vintage-Classics-Tolstoy/dp/1400079985/ref=sr_1_1?ie=UTF8&qid=1469602093&sr=8-1&keywords=peace+and+war"
driver.get(url)
time.sleep(2)

driver.find_element_by_id("img-canvas").click()
#The easiest way to get exactly one of every page
imageList = set()

#Wait for the page to load
time.sleep(10)
print(driver.find_element_by_id("sitbReaderRightPageTurner").get_attribute("style"))
while "pointer" in driver.find_element_by_id("sitbReaderRightPageTurner").get_attribute("style"):
    #While we can click on the right arrow, move through the pages
    driver.find_element_by_id("sitbReaderRightPageTurner").click()
    time.sleep(2)
    #Get any new pages that have loaded (multiple pages can load at once)
    pages = driver.find_elements_by_xpath("//div[@class='pageImage']/div/img")
    for page in pages:
        image = page.get_attribute("src")
        imageList.add(image)

driver.quit()

#Start processing the images we've collected URLs for with Tesseract
for image in sorted(imageList):
    urlretrieve(image, "page.jpg")
    p = subprocess.Popen(["tesseract", "page.jpg", "page"], stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    p.wait()
    f = open("page.txt", "r")
    print(f.read())

