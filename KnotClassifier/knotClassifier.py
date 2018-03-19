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

# PARSE ARGUMENTS

import argparse

parser = argparse.ArgumentParser(description='Train a convolutional neural network to classify knots.')
group = parser.add_mutually_exclusive_group()
group.add_argument('-a', '--augmentation', action='store_true', help='Use data augmentation')
group.add_argument('-s', '--small', action='store_true', help='Use small model architecture')
group.add_argument('-l', '--large', action='store_true', help='Use large model architecture')


# -----------------------------------------------------------

# IMPORT STATEMENTS

from keras.preprocessing.image import ImageDataGenerator
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D
from keras.layers import Activation, Dropout, Flatten, Dense, BatchNormalization
from keras.layers.noise import GaussianNoise
from keras.utils import np_utils
from keras import backend as K

import numpy as np

import matplotlib.pyplot as plt

from sklearn.decomposition import PCA
from sklearn.manifold import TSNE

from sklearn.metrics import confusion_matrix
import itertools

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
epochs = 100
batch_size = 32

if K.image_data_format() == 'channels_first':
    input_shape = (3, img_width, img_height)
else:
    input_shape = (img_width, img_height, 3)

# -----------------------------------------------------------

# CNN MODELS

# SMALL CNN MODEL
if args.small:
    
    print 'You are using the small CNN model architecture'
    
    model = Sequential()
    
    model.add(Conv2D(32, (3, 3), input_shape=input_shape))
    model.add(Activation('relu'))
    model.add(Conv2D(32, (3, 3)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    
    model.add(Conv2D(32, (3, 3)))
    model.add(Activation('relu'))
    model.add(Conv2D(32, (3, 3)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    
    #model.add(Dropout(0.5))
    
    model.add(Conv2D(64, (3, 3)))
    model.add(Activation('relu'))
    model.add(Conv2D(64, (3, 3)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    
    model.add(Conv2D(64, (3, 3)))
    model.add(Activation('relu'))
    model.add(Conv2D(64, (3, 3)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Dropout(0.5))
    
    model.add(Flatten())
    model.add(Dense(32))
    model.add(Activation('relu'))
    model.add(Dropout(0.5))
    model.add(Dense(10))
    model.add(Activation('softmax'))
    
    model.compile(loss='categorical_crossentropy',
                  optimizer='adam',
                  metrics=['accuracy'])
    
    print model.summary()

# LARGE CNN MODEL
elif args.large:
    
    print 'You are using the large CNN model architecture'
    
    model = Sequential()
    
    model.add(Conv2D(32, (3, 3), input_shape=input_shape))
    model.add(Activation('relu'))
    model.add(Conv2D(32, (3, 3)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    
    model.add(Conv2D(64, (3, 3)))
    model.add(Activation('relu'))
    model.add(Conv2D(64, (3, 3)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    
    model.add(Dropout(0.5))
    
#    model.add(Conv2D(128, (3, 3)))
#    model.add(Activation('relu'))
#    model.add(Conv2D(128, (3, 3)))
#    model.add(Activation('relu'))
#    model.add(MaxPooling2D(pool_size=(2, 2)))
    
    model.add(Flatten())
    model.add(Dense(128))
    model.add(Activation('relu'))
    model.add(Dense(64))
    model.add(Activation('relu'))
    model.add(Dropout(0.5))
    model.add(Dense(10))
    model.add(Activation('softmax'))
    
    model.compile(loss='categorical_crossentropy',
                  optimizer='adam',
                  metrics=['accuracy'])
    
    print model.summary()

# MEDIUM CNN MODEL
else:
    
    print 'You are using the medium CNN model architecture'
    
    model = Sequential()
    
    model.add(Conv2D(32, (3, 3), input_shape=input_shape))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    
    model.add(Conv2D(32, (3, 3)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    
    #model.add(Dropout(0.5))
    
    model.add(Conv2D(64, (3, 3)))
    model.add(Activation('relu'))
    #model.add(BatchNormalization())
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Dropout(0.5))
    
    model.add(Flatten())
    model.add(Dense(64))
    model.add(Activation('relu'))
    model.add(Dropout(0.5))
    model.add(Dense(10))
    model.add(Activation('softmax'))
    
    model.compile(loss='categorical_crossentropy',
                  optimizer='adam',
                  metrics=['accuracy'])
    
    print model.summary()

# -----------------------------------------------------------

# DATA AUGMENTATION

if args.augmentation:
    
    print 'You are using data augmentation'
    
    # Training Augmentation Configuration
    # Rotates an image for every degree
    # Rescales images
    # Modifies shear intensity
    # Modifies zoom
    # Shifts width
    # Shifts height
    # Flips images horizontally
    # Flips images vertically
    train_datagen = ImageDataGenerator(
        rotation_range=360,
        rescale=1. / 255,
        shear_range=0.2,
        zoom_range=0.3,
        width_shift_range=0.2,
        height_shift_range=0.2,
        horizontal_flip=True,
        vertical_flip=True
    )
    
    # Testing Augmentation Configuration
    # Only Rescales images
    # Very important for the validation data to have no augmentation
    # Enables validation on real data, and not augmented data
    test_datagen = ImageDataGenerator(
        rescale=1. / 255
    )

# NO DATA AUGMENTATION

else:
    
    print 'You are not using data augmentation'
    
    # Training Augmentation Configuration
    # Only rescales images
    # No augmentation
    train_datagen = ImageDataGenerator(
        rescale=1. /255
    )
    
    # Testing Augmentation Configuration
    # Only rescales images
    # No augmentation
    test_datagen = ImageDataGenerator(
        rescale=1. /255
    )

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
    validation_steps=nb_validation_samples // batch_size,
    shuffle=True)

# SAVE MODEL (INCLUDING WEIGHTS)
model.save('first_try.h5')

# -----------------------------------------------------------

# TSNE VISUALISATION

predictions = model.predict_generator(validation_generator,
                                          steps=nb_validation_samples)

# First, reduce to 10 dimensions with PCA
pca = PCA(n_components=10)
pca_results = pca.fit_transform(predictions)
print('Variance PCA: {}'.format(np.sum(pca.explained_variance_ratio_)))

# Next, run t-SNE on the PCA results to obtain a 2D plot
tsne = TSNE(n_components=2, perplexity=30, learning_rate=250, verbose = 1)
tsne_results = tsne.fit_transform(pca_results[:5000])

# Convert to binary class matrix
categoricalClasses = np_utils.to_categorical(validation_generator.classes[:5000], num_classes = 10)
# Create a figure where each class has a unique colour
colour_map = np.argmax(categoricalClasses, axis=1)
tsneFigure = plt.figure(figsize=(10,10))
for colour in range(10):
    indices = np.where(colour_map==colour)
    indices = indices[0]
    plt.scatter(tsne_results[indices,0],
                tsne_results[indices,1],
                label=colour)
plt.legend()
plt.title('t-SNE Visualisation')
tsneFigure.savefig('tsneVisualisation.jpg')
plt.close()

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

# -----------------------------------------------------------

# PLOT CONFUSION MATRIX

matrix_predictions = model.predict_generator(validation_generator)
matrix_predictions = np.argmax(matrix_predictions, axis=-1)
print validation_generator.classes
print matrix_predictions

confusionMatrix = confusion_matrix(validation_generator.classes, matrix_predictions)
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
final_confusion_matrix = plt.figure(figsize=(20, 10))
plot_confusion_matrix(confusionMatrix, classes=class_names,
                      title='Confusion Matrix')
final_confusion_matrix.savefig('confusionMatrix.jpg')

# Plot Normalised Confusion Matrix
final_normalised_confusion_matrix = plt.figure(figsize=(20, 10))
plot_confusion_matrix(confusionMatrix, classes=class_names, normalize=True,
                      title='Normalised Confusion Matrix')
final_normalised_confusion_matrix.savefig('normalisedConfusionMatrix.jpg')

plt.close()
