from keras.layers import Input, Dense, Conv2D, MaxPooling2D, UpSampling2D
from keras.models import Model
from keras import backend as K
from keras.preprocessing.image import ImageDataGenerator
from keras.datasets import mnist
from keras.callbacks import TensorBoard
import numpy as np
import matplotlib.pyplot as plt

def tuple_generator(generator):
    for batch in generator:
        yield (batch, batch)

img_width = 148
img_height = 148
train_data_dir = 'dataResized/train'
validation_data_dir = 'dataResized/validation'
epochs = 50
batch_size = 128
nb_train_samples = 1152
nb_validation_samples = 226

input_img = Input(shape=(img_width, img_height, 3))

x = Conv2D(16, (3, 3), activation='relu', padding='same')(input_img)
x = MaxPooling2D((2, 2), padding='same')(x)
x = Conv2D(8, (3, 3), activation='relu', padding='same')(x)
x = MaxPooling2D((2, 2), padding='same')(x)
x = Conv2D(8, (3, 3), activation='relu', padding='same')(x)
encoded = MaxPooling2D((2, 2), padding='same')(x)

x = Conv2D(8, (3, 3), activation='relu', padding='same')(encoded)
x = UpSampling2D((2, 2))(x)
x = Conv2D(8, (3, 3), activation='relu', padding='same')(x)
x = UpSampling2D((2, 2))(x)
x = Conv2D(16, (3, 3), activation='relu')(x)
x = UpSampling2D((2, 2))(x)
decoded = Conv2D(3, (3, 3), activation='sigmoid', padding='same')(x)

autoencoder = Model(input_img, decoded)
autoencoder.compile(optimizer='adadelta', loss='binary_crossentropy')

train_datagen = ImageDataGenerator(rescale=1. / 255)
test_datagen = ImageDataGenerator(rescale=1. / 255)

# TRAINING GENERATOR
train_generator = train_datagen.flow_from_directory(
    train_data_dir,
    target_size=(img_width, img_height),
    batch_size=batch_size,
    class_mode=None)

# VALIDATION GENERATOR
validation_generator = test_datagen.flow_from_directory(
    validation_data_dir,
    target_size=(img_width, img_height),
    batch_size=batch_size,
    class_mode=None)

# MODEL FITTING
fit = autoencoder.fit_generator(
    tuple_generator(train_generator),
    steps_per_epoch=nb_train_samples // batch_size,
    epochs=epochs,
    validation_data=tuple_generator(validation_generator),
    validation_steps=nb_validation_samples // batch_size,
    shuffle=True)

img = next(validation_generator)[:1]
dec = autoencoder.predict(img)
img = img[0]
dec = dec[0]
img = (img*255).astype('uint8')
dec = (dec*255).astype('uint8')

plt.imshow(np.hstack((img, dec)))
plt.title('Original (Validation) and Reconstructed Images')
plt.show()

img = next(train_generator)[:1]
dec = autoencoder.predict(img)
img = img[0]
dec = dec[0]
img = (img*255).astype('uint8')
dec = (dec*255).astype('uint8')

plt.imshow(np.hstack((img, dec)))
plt.title('Original (Train) and Reconstructed Images')
plt.show()

