# dataAugmentation.py
# Author = Joseph M. Cameron
# This script saves images that have been augmented through data augmentation

# Script Usage: python dataAugmentation.py
# For example: When this script is in the same directory as a dataset folder named 'dataResized'
# and an empty directory called 'dataAugmentation',
# simply specify a valid path to an example image and enter python dataAugmentation.py

# -----------------------------------------------------------

# IMPORT STATEMENTS

from keras.preprocessing.image import ImageDataGenerator
from keras.preprocessing.image import array_to_img, img_to_array, load_img

# -----------------------------------------------------------

# GLOBAL VARIABLES

directory_path = 'dataResized/train/Alpine Butterfly Knot/DiffuseLight/Set/'
image_path = directory_path + 'IMG_6324.jpg'
output_path = 'dataAugmentation/augmented{}.jpg'

# -----------------------------------------------------------

# DATA AUGMENTATION

generator = ImageDataGenerator(
    rotation_range=360,
    rescale=1. / 255,
    shear_range=0.2,
    zoom_range=0.3,
    width_shift_range=0.2,
    height_shift_range=0.2,
    horizontal_flip=True,
    vertical_flip=True
)

# -----------------------------------------------------------

# LOAD DATASET IMAGE

image = img_to_array(load_img(image_path))
image = image.reshape((1,) + image.shape)

# -----------------------------------------------------------

# SAVE 10 AUGMENTED IMAGES

images = generator.flow(image, batch_size=1)
for i, augmented_images in enumerate(images):
    augmented_image = array_to_img(augmented_images[0], scale=True)
    augmented_image.save(output_path.format(i + 1))
    if i >= 9:
        break


