# plot_confusion_matrix.py
# Author = Joseph M. Cameron
# This script produces a 10-class confusion matrix when given a saved Keras model
# The resulting confusion matrix is then saved as an image called 'confusion_matrix.jpg' in the same directory

# Script Usage: python plot_confusion_matrix.py
# For example: When this script is in the same directory as the Keras model 'first_try.h5',
# and validation image directory 'dataResized/validation',
# simply enter: python plot_confusion_matrix.py

# Of course, the global variables can be altered to suit any other working directory and dataset.

# -----------------------------------------------------------

# IMPORT STATEMENTS

from keras.models import load_model
from keras.preprocessing.image import ImageDataGenerator
from keras.utils import np_utils

import numpy as np

import matplotlib.pyplot as plt

import itertools

from sklearn.metrics import confusion_matrix

# -----------------------------------------------------------

# LOAD MODEL

model = load_model('first_try.h5')
model.compile(loss='categorical_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])

# -----------------------------------------------------------

# GLOBAL VARIABLES

# Target dimensions for the images
# (150, 150) has been shown to be an optimal image size for training
img_width, img_height = 150, 150

# Global variables that are directory specific
validation_data_dir = 'dataResized/validation'
nb_validation_samples = 274
batch_size = nb_validation_samples

# -----------------------------------------------------------

# RESCALE VALIDATION IMAGES
test_datagen = ImageDataGenerator(
    rescale=1. / 255
)

# VALIDATION GENERATOR
validation_generator = test_datagen.flow_from_directory(
    validation_data_dir,
    target_size=(img_width, img_height),
    batch_size=batch_size,
    class_mode='categorical'
)

# -----------------------------------------------------------

# TRUE CLASSES

true_classes = validation_generator.classes

# -----------------------------------------------------------

# MODEL PREDICTIONS

print "Obtaining model predictions..."
predictions = model.predict_generator(validation_generator)
# Get index of largest probability
predictions = np.argmax(predictions, axis=-1)

# -----------------------------------------------------------

# PLOT CONFUSION MATRIX

confusionMatrix = confusion_matrix(true_classes, predictions)
class_names = ['Alpine Butterfly Knot', 'Bowline Knot', 'Clove Hitch', 'Figure-8 Knot', 'Figure-8 Loop',
               'Fisherman Knot', 'Flemish Bend', 'Overhand Knot', 'Reef Knot', 'Slip Knot']

# plot_confusion_matrix function obtained from sklearn documentation
# Confusion Matrix Examples
# http://scikit-learn.org/stable/modules/generated/sklearn.metrics.confusion_matrix.html
def plot_confusion_matrix(cm, classes,
                          normalize=False,
                          title='Confusion matrix',
                          cmap=plt.cm.Blues):
    """
    This function prints and plots the confusion matrix.
    Normalization can be applied by setting `normalize=True`.
    """
    if normalize:
        cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
        print("Normalized confusion matrix")
    else:
        print('Confusion matrix, without normalization')

    print(cm)

    plt.imshow(cm, interpolation='nearest', cmap=cmap)
    plt.title(title)
    plt.colorbar()
    tick_marks = np.arange(len(classes))
    plt.xticks(tick_marks, classes, rotation=45)
    plt.yticks(tick_marks, classes)

    fmt = '.2f' if normalize else 'd'
    thresh = cm.max() / 2.
    for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
        plt.text(j, i, format(cm[i, j], fmt),
                 horizontalalignment="center",
                 color="white" if cm[i, j] > thresh else "black")

    plt.tight_layout()
    plt.ylabel('True label')
    plt.xlabel('Predicted label')

np.set_printoptions(precision=2)

# Plot Confusion Matrix
final_confusion_matrix = plt.figure(figsize=(10, 10))
plot_confusion_matrix(confusionMatrix, classes=class_names, title='The Knot Classifier Confusion Matrix')
print "Confusion matrix plotted!"
plt.show()

# -----------------------------------------------------------

# SAVE CONFUSION MATRIX

final_confusion_matrix.savefig('confusion_matrix.jpg')

# -----------------------------------------------------------

