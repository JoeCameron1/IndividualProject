# multiclass_roc_analysis.py
# Author = Joseph M. Cameron
# This script produces multiclass ROC curve analysis when given a saved Keras model
# The resulting ROC curves are then saved as an image called 'roc_curve_analysis.jpg' in the same directory

# Script Usage: python multiclass_roc_analysis.py
# For example: When this script is in the same directory as the Keras model 'first_try.h5',
# and validation image directory 'dataResized/validation',
# simply enter: python multiclass_roc_analysis.py

# Of course, the global variables can be altered to suit any other working directory and dataset.

# -----------------------------------------------------------

# IMPORT STATEMENTS

from keras.models import load_model
from keras.preprocessing.image import ImageDataGenerator
from keras.utils import np_utils

import numpy as np

import matplotlib.pyplot as plt

from scipy import interp

from itertools import cycle

from sklearn.metrics import roc_curve, auc

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

# Number of classes
n_classes = 10

# ROC Curve Linewidth
lw = 2

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

true_classes = np_utils.to_categorical(validation_generator.classes, n_classes)

# -----------------------------------------------------------

# MODEL PREDICTIONS

print "Obtaining model predictions..."
predictions = model.predict_generator(validation_generator)

# -----------------------------------------------------------

# PLOT ROC CURVES

# Compute ROC curve and ROC area (AUC) for each class
fpr = dict()
tpr = dict()
roc_auc = dict()
for i in range(n_classes):
    fpr[i], tpr[i], _ = roc_curve(true_classes[:, i], predictions[:, i])
    roc_auc[i] = auc(fpr[i], tpr[i])

# Compute micro-average ROC curve and ROC area (AUC)
fpr["micro"], tpr["micro"], _ = roc_curve(true_classes.ravel(), predictions.ravel())
roc_auc["micro"] = auc(fpr["micro"], tpr["micro"])

# Compute macro-average ROC curve and ROC area (AUC)
# First aggregate all false positive rates
all_fpr = np.unique(np.concatenate([fpr[i] for i in range(n_classes)]))

# Then interpolate all ROC curves at these points
mean_tpr = np.zeros_like(all_fpr)
for i in range(n_classes):
    mean_tpr += interp(all_fpr, fpr[i], tpr[i])

# Finally average it and compute AUC
mean_tpr /= n_classes

fpr["macro"] = all_fpr
tpr["macro"] = mean_tpr
roc_auc["macro"] = auc(fpr["macro"], tpr["macro"])

# Plot the one vs all ROC curves
multiclass_roc_curve = plt.figure(figsize=(15,10))

plt.plot(fpr["micro"], tpr["micro"],
         label='micro-average ROC curve (area = {0:0.2f})'
               ''.format(roc_auc["micro"]),
         color='deeppink', linestyle=':', linewidth=4)

plt.plot(fpr["macro"], tpr["macro"],
         label='macro-average ROC curve (area = {0:0.2f})'
               ''.format(roc_auc["macro"]),
         color='navy', linestyle=':', linewidth=4)

colors = cycle(['aqua', 'darkorange', 'cornflowerblue', 'blue', 'green', 'red', 'peachpuff', 'magenta', 'yellow', 'black'])
for i, color in zip(range(n_classes), colors):
    plt.plot(fpr[i], tpr[i], color=color, lw=lw,
             label='ROC curve of class {0} (area = {1:0.2f})'
             ''.format(i, roc_auc[i]))

plt.plot([0, 1], [0, 1], 'k--', lw=lw)
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('The Knot Classifier Multiclass (One vs All) ROC Analysis')
plt.legend(loc="lower right")
print "ROC curves plotted!"
plt.show()

# -----------------------------------------------------------

# SAVE ROC CURVES

multiclass_roc_curve.savefig('roc_curve_analysis.jpg')

# -----------------------------------------------------------

