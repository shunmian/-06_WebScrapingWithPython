from PIL import Image
import pytesseract
import subprocess

image = Image.open("3.1_CAPTCHA.png")
image.show()

subprocess.call(["tesseract","3.1_CAPTCHA.png","output"])
outputFile = open("output.txt",'r')
print(outputFile.read())
outputFile.close()
# string = pytesseract.image_to_string(image)
# print(string)

#output:
#