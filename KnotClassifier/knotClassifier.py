# knotClassifier.py
# Author = Joseph M. Cameron
# This script trains a convolutional neural network on a dataset of images
# The final weights are then saved within the same directory as 'first_try.h5'

# Script Usage: python knotClassifier.py
# For example: When this script is in the same directory as a dataset folder named 'dataResized',
# where all training data is in 'datasetResized/train',
# and all validation data is in 'datasetResized/validation', simply enter:
# python knotClassifier.py


# -----------------------------------------------------------

# IMPORT STATEMENTS

from keras.preprocessing.image import ImageDataGenerator
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D
from keras.layers import Activation, Dropout, Flatten, Dense
from keras.layers.noise import GaussianNoise
from keras import backend as K

import matplotlib.pyplot as plt

# -----------------------------------------------------------

# GLOBAL VARIABLES

# Target dimensions for the images
# (150, 150) has been shown to be an optimal image size for training
img_width, img_height = 150, 150

# Global variables that are directory specific
train_data_dir = 'dataResized/train'
validation_data_dir = 'dataResized/validation'
nb_train_samples = 384
nb_validation_samples = 192
epochs = 50
batch_size = 16

if K.image_data_format() == 'channels_first':
    input_shape = (3, img_width, img_height)
else:
    input_shape = (img_width, img_height, 3)

# -----------------------------------------------------------

# CNN MODEL

model = Sequential()
model.add(Conv2D(32, (3, 3), input_shape=input_shape))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Conv2D(32, (3, 3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Conv2D(64, (3, 3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Flatten())
model.add(Dense(64))
model.add(GaussianNoise(0.2))
model.add(Activation('relu'))
model.add(Dropout(0.5))
model.add(Dense(10))
model.add(Activation('softmax'))

model.compile(loss='categorical_crossentropy',
              optimizer='rmsprop',
              metrics=['accuracy'])

print model.summary()

# -----------------------------------------------------------

# DATA AUGMENTATION

# Training Augmentation Configuration
# Rotates an image for every degree
# Rescales images
# Flips images horizontally
train_datagen = ImageDataGenerator(
    rotation_range=1,
    rescale=1. / 255,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True)

# Testing Augmentation Configuration
# Only rescales images for testing purposes
test_datagen = ImageDataGenerator(rescale=1. / 255)

# -----------------------------------------------------------

# TRAINING GENERATOR
train_generator = train_datagen.flow_from_directory(
    train_data_dir,
    target_size=(img_width, img_height),
    batch_size=batch_size,
    class_mode='categorical')

# VALIDATION GENERATOR
validation_generator = test_datagen.flow_from_directory(
    validation_data_dir,
    target_size=(img_width, img_height),
    batch_size=batch_size,
    class_mode='categorical')

# MODEL FITTING
fit = model.fit_generator(
    train_generator,
    steps_per_epoch=nb_train_samples // batch_size,
    epochs=epochs,
    validation_data=validation_generator,
    validation_steps=nb_validation_samples // batch_size)

# SAVE MODEL (INCLUDING WEIGHTS)
model.save('first_try.h5')

# -----------------------------------------------------------

# PLOT TRAINING HISTORY

historyFigure, (left, right) = plt.subplots(ncols=2, figsize=(20,10))

# Plot the training history loss
def plotHistoryLoss(fit):
    left.plot(fit.history['loss'],label="Training Loss")
    left.plot(fit.history['val_loss'],label="Validation Loss")
    left.set_title('Model Loss')
    left.set_xlabel('Epoch')
    left.set_ylabel('Loss')
    left.legend(loc='upper left')

# Plot the training history accuracy
def plotHistoryAccuracy(fit):
    right.plot(fit.history['acc'],label="Training Accuracy")
    right.plot(fit.history['val_acc'],label="Validation Accuracy")
    right.set_title('Model Accuracy')
    right.set_xlabel('Epoch')
    right.set_ylabel('Accuracy')
    right.legend(loc='upper left')

plotHistoryLoss(fit)
plotHistoryAccuracy(fit)
historyFigure.savefig('trainingHistory.jpg')
plt.close()
