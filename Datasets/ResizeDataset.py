# ResizeDataset.py
# Author = Joseph M. Cameron
# This script resizes images within a dataset.

# Script Usage: python ResizeDataset.py path/to/dataset/folder imageWidth imageHeight
# For example: When this script is in the same directory as a dataset folder named 'Dataset',
# and all images within 'Dataset' should be resized to 100x100 (in pixels), simply enter:
# python ResizeDataset.py ./Dataset 100 100


# IMPORT STATEMENTS
import os
import sys
import shutil
import errno
from PIL import Image


# COPY FUNCTION
# This function creates an exact copy of an existing directory structure.
# Used to create a copy of the original dataset (which will hold resized images).
# This is more desirable than overwriting the original dataset.
def copy(source, destination):
    try:
        shutil.copytree(source, destination)
    except OSError as exception:
        # If non-directory file is given, call shutil.copy instead.
        if exception.errno == errno.ENOTDIR:
            shutil.copy(source, destination)
        else:
            print('Could not copy directory structure. Error: %s' % exception)


# RESIZE FUNCTION
# This function resizes all images within a directory structure.
# Used to resize all png, bmp and jpg images within a dataset to a specific size. 
def resize(dataset, resizeWidth, resizeHeight):
    fileExtensions = ["png", "bmp", "jpg"]
    for path, directories, files in os.walk(dataset):
        for fileName in files:
            file_extension = fileName[-3:].lower()
            # If a file does not have one of the expected extensions, ignore it.
            if file_extension not in fileExtensions:
                continue
            filePath = os.path.join(path, fileName)
            image = Image.open(filePath)
            # Resizing occurs via the Image.ANTIALIAS downsampling filter.
            # Using Image.thumbnail() in order to maintain aspect ratio.
            image.thumbnail((int(resizeWidth), int(resizeHeight)), Image.ANTIALIAS)
            # Overwriting the original image in the 'Resized' directory.
            image.save(filePath)


# MAIN
# Arg[1] = Path to dataset folder
# Arg[2] = Objective Width in pixels
# Arg[3] = Objective Height in pixels
if __name__ == "__main__":
    copy(sys.argv[1], sys.argv[1]+"Resized")
    dataset=sys.argv[1]+"Resized"
    resize(dataset, sys.argv[2], sys.argv[3])
