from PIL import Image
import pytesseract

def cleanFile(filePath,newFilePath):

    image = Image.open(filePath)

    #Set a threshold value for the image, and save
    image = image.point(lambda x:0 if x<143 else 255)
    image.save(newFilePath)
    return image

image = cleanFile('text2.png','text3_cleaned.png')
string = pytesseract.image_to_string(image)
print(string)


# output
# This IS some text‘ wntten In Anal, that will be readby
# Tesseract Here are some symbols: !@#$%"&'()



