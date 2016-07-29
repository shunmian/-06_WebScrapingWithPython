from PIL import Image, ImageFilter

kitten = Image.open("kitten.jpg")
#GaussianBlur is added to the orginal image
blurryKitten = kitten.filter(ImageFilter.GaussianBlur)
blurryKitten.save("kittent_blurred.jpg")
blurryKitten.show()




