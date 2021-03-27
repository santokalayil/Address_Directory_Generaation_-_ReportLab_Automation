from PIL import Image
import os

size = (320, 480)


# This function is to convert image to small size
def convert_img(img_name):
    source = os.path.join(os.path.join('photos', 'original'), img_name)
    destination = os.path.join(os.path.join('photos', 'resized'), img_name)
    image = Image.open(source)
    image.thumbnail(size, Image.ANTIALIAS)
    image.save(destination)


# This function converts all images in the directory
def convert_images():
    for img_name in os.listdir(os.path.join('photos', 'original')):
        convert_img(img_name)
    print("Images' conversion completed!")
