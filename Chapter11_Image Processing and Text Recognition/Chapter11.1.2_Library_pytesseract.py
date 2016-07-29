from PIL import Image
import pytesseract

#1 Well-Formateed Text
image = Image.open("text1.png")
string = pytesseract.image_to_string(image)
print(string)
# output
# This is some text, written in Arial, that will be read by
# Tesseract. Here are some symbols: !@#$%"&*()

#2 slightly dirty Well-Formateed Text
image = Image.open("text2.png")
string = pytesseract.image_to_string(image)
print(string)
# output
# This is some text, mitten in Anal, 1!" _,
# Tessetact. Here are some symbols: _



