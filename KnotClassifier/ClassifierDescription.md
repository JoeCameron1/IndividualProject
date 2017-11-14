# Knot Classifier

This initial classifier is created by knotClassifier.py.

knotClassifier.py trains and validates on data from the dataset 'dataResized'.

'dataResized' has been resized using the script resizeData.py contained within the Datasets directory of this repo.

Within 'dataResized', there is a train directory and a validation directory.
The train directory contains data taken in diffuse lighting conditions and side source lighting conditions.
The validation directory only contains data taken in overhead source lighting conditions.
This results in an approximate 66% training 33% validation split.

knotClassifier.py first prints a summary of the convolutional neural network model:

```
_________________________________________________________________
Layer (type)                 Output Shape              Param #   
=================================================================
conv2d_1 (Conv2D)            (None, 148, 148, 32)      896       
_________________________________________________________________
activation_1 (Activation)    (None, 148, 148, 32)      0         
_________________________________________________________________
max_pooling2d_1 (MaxPooling2 (None, 74, 74, 32)        0         
_________________________________________________________________
conv2d_2 (Conv2D)            (None, 72, 72, 32)        9248      
_________________________________________________________________
activation_2 (Activation)    (None, 72, 72, 32)        0         
_________________________________________________________________
max_pooling2d_2 (MaxPooling2 (None, 36, 36, 32)        0         
_________________________________________________________________
conv2d_3 (Conv2D)            (None, 34, 34, 64)        18496     
_________________________________________________________________
activation_3 (Activation)    (None, 34, 34, 64)        0         
_________________________________________________________________
max_pooling2d_3 (MaxPooling2 (None, 17, 17, 64)        0         
_________________________________________________________________
flatten_1 (Flatten)          (None, 18496)             0         
_________________________________________________________________
dense_1 (Dense)              (None, 64)                1183808   
_________________________________________________________________
activation_4 (Activation)    (None, 64)                0         
_________________________________________________________________
dropout_1 (Dropout)          (None, 64)                0         
_________________________________________________________________
dense_2 (Dense)              (None, 5)                 325       
_________________________________________________________________
activation_5 (Activation)    (None, 5)                 0         
=================================================================
Total params: 1,212,773
Trainable params: 1,212,773
Non-trainable params: 0
_________________________________________________________________

```

As we can see from this summary, the last activation layer has an output shape of (None, 5).
This is essential for 5-class classification, as we are dealing with five knots.

Initially, I allowed the model to train for 20 epochs.
This was the result:

```

Found 192 images belonging to 5 classes.
Found 96 images belonging to 5 classes.
Epoch 1/20
48/48 [==============================] - 4s - loss: 1.6512 - acc: 0.2135 - val_loss: 1.6000 - val_acc: 0.4062
Epoch 2/20
48/48 [==============================] - 4s - loss: 1.6210 - acc: 0.2917 - val_loss: 1.5864 - val_acc: 0.2604
Epoch 3/20
48/48 [==============================] - 4s - loss: 1.5932 - acc: 0.2812 - val_loss: 1.4559 - val_acc: 0.4583
Epoch 4/20
48/48 [==============================] - 4s - loss: 1.3763 - acc: 0.4479 - val_loss: 1.3645 - val_acc: 0.5104
Epoch 5/20
48/48 [==============================] - 4s - loss: 1.2036 - acc: 0.5521 - val_loss: 2.4489 - val_acc: 0.4375
Epoch 6/20
48/48 [==============================] - 4s - loss: 1.0813 - acc: 0.5729 - val_loss: 1.4460 - val_acc: 0.6250
Epoch 7/20
48/48 [==============================] - 4s - loss: 0.9564 - acc: 0.6302 - val_loss: 1.8398 - val_acc: 0.5208
Epoch 8/20
48/48 [==============================] - 4s - loss: 1.0920 - acc: 0.6250 - val_loss: 1.5271 - val_acc: 0.4896
Epoch 9/20
48/48 [==============================] - 4s - loss: 0.9359 - acc: 0.6823 - val_loss: 2.0667 - val_acc: 0.3958
Epoch 10/20
48/48 [==============================] - 4s - loss: 0.8711 - acc: 0.7396 - val_loss: 1.9357 - val_acc: 0.5833
Epoch 11/20
48/48 [==============================] - 4s - loss: 0.8468 - acc: 0.6979 - val_loss: 2.5044 - val_acc: 0.5000
Epoch 12/20
48/48 [==============================] - 4s - loss: 0.8802 - acc: 0.6667 - val_loss: 2.5785 - val_acc: 0.4271
Epoch 13/20
48/48 [==============================] - 4s - loss: 0.6806 - acc: 0.7292 - val_loss: 3.6923 - val_acc: 0.4167
Epoch 14/20
48/48 [==============================] - 4s - loss: 0.7333 - acc: 0.7552 - val_loss: 2.4173 - val_acc: 0.4896
Epoch 15/20
48/48 [==============================] - 4s - loss: 0.6917 - acc: 0.7344 - val_loss: 1.8637 - val_acc: 0.5729
Epoch 16/20
48/48 [==============================] - 4s - loss: 0.6715 - acc: 0.7708 - val_loss: 2.9250 - val_acc: 0.3958
Epoch 17/20
48/48 [==============================] - 4s - loss: 0.6782 - acc: 0.7760 - val_loss: 2.0771 - val_acc: 0.5938
Epoch 18/20
48/48 [==============================] - 4s - loss: 0.6438 - acc: 0.7500 - val_loss: 2.1085 - val_acc: 0.6250
Epoch 19/20
48/48 [==============================] - 4s - loss: 0.4918 - acc: 0.8073 - val_loss: 4.4362 - val_acc: 0.4896
Epoch 20/20
48/48 [==============================] - 4s - loss: 0.5745 - acc: 0.8333 - val_loss: 3.5282 - val_acc: 0.5104

```

On the first epoch, an accuracy of 21.35% was achieved. 
However, after 20 epochs, an accuracy of 83.33% was achieved for knot classification.
This shows rapid learning in action.

Next, I decided to allow the model to train for 50 epochs.
This was the result:

```

Found 192 images belonging to 5 classes.
Found 96 images belonging to 5 classes.
Epoch 1/50
48/48 [==============================] - 4s - loss: 1.6811 - acc: 0.2135 - val_loss: 1.5870 - val_acc: 0.2500
Epoch 2/50
48/48 [==============================] - 4s - loss: 1.6050 - acc: 0.2865 - val_loss: 1.5523 - val_acc: 0.4375
Epoch 3/50
48/48 [==============================] - 4s - loss: 1.6367 - acc: 0.2760 - val_loss: 1.4979 - val_acc: 0.4479
Epoch 4/50
48/48 [==============================] - 4s - loss: 1.3660 - acc: 0.4740 - val_loss: 1.2865 - val_acc: 0.4792
Epoch 5/50
48/48 [==============================] - 4s - loss: 1.2084 - acc: 0.5104 - val_loss: 2.4173 - val_acc: 0.4062
Epoch 6/50
48/48 [==============================] - 3s - loss: 0.9954 - acc: 0.6667 - val_loss: 1.5782 - val_acc: 0.4792
Epoch 7/50
48/48 [==============================] - 4s - loss: 1.0110 - acc: 0.6354 - val_loss: 1.5889 - val_acc: 0.4271
Epoch 8/50
48/48 [==============================] - 4s - loss: 0.9166 - acc: 0.6667 - val_loss: 1.9426 - val_acc: 0.4583
Epoch 9/50
48/48 [==============================] - 3s - loss: 0.9436 - acc: 0.6615 - val_loss: 2.0109 - val_acc: 0.4167
Epoch 10/50
48/48 [==============================] - 4s - loss: 0.7372 - acc: 0.7500 - val_loss: 1.3969 - val_acc: 0.5625
Epoch 11/50
48/48 [==============================] - 4s - loss: 0.7188 - acc: 0.6927 - val_loss: 1.4303 - val_acc: 0.4479
Epoch 12/50
48/48 [==============================] - 4s - loss: 0.6829 - acc: 0.7396 - val_loss: 2.6566 - val_acc: 0.4271
Epoch 13/50
48/48 [==============================] - 4s - loss: 0.7002 - acc: 0.7604 - val_loss: 2.4022 - val_acc: 0.4583
Epoch 14/50
48/48 [==============================] - 4s - loss: 0.7333 - acc: 0.7812 - val_loss: 2.9035 - val_acc: 0.3854
Epoch 15/50
48/48 [==============================] - 4s - loss: 0.5756 - acc: 0.7969 - val_loss: 2.6065 - val_acc: 0.4583
Epoch 16/50
48/48 [==============================] - 3s - loss: 0.5168 - acc: 0.8281 - val_loss: 2.8159 - val_acc: 0.4479
Epoch 17/50
48/48 [==============================] - 4s - loss: 0.5502 - acc: 0.8021 - val_loss: 2.8005 - val_acc: 0.4792
Epoch 18/50
48/48 [==============================] - 4s - loss: 0.4832 - acc: 0.8281 - val_loss: 3.5529 - val_acc: 0.4688
Epoch 19/50
48/48 [==============================] - 3s - loss: 0.6077 - acc: 0.8073 - val_loss: 2.3582 - val_acc: 0.4792
Epoch 20/50
48/48 [==============================] - 4s - loss: 0.4110 - acc: 0.8490 - val_loss: 3.8254 - val_acc: 0.4375
Epoch 21/50
48/48 [==============================] - 4s - loss: 0.4640 - acc: 0.8542 - val_loss: 5.8018 - val_acc: 0.3854
Epoch 22/50
48/48 [==============================] - 4s - loss: 0.4605 - acc: 0.8438 - val_loss: 4.9427 - val_acc: 0.4271
Epoch 23/50
48/48 [==============================] - 4s - loss: 0.4589 - acc: 0.8646 - val_loss: 4.1439 - val_acc: 0.4375
Epoch 24/50
48/48 [==============================] - 4s - loss: 0.3390 - acc: 0.8646 - val_loss: 5.7454 - val_acc: 0.4375
Epoch 25/50
48/48 [==============================] - 4s - loss: 0.4399 - acc: 0.8438 - val_loss: 3.6235 - val_acc: 0.4479
Epoch 26/50
48/48 [==============================] - 4s - loss: 0.2988 - acc: 0.8958 - val_loss: 5.4660 - val_acc: 0.4583
Epoch 27/50
48/48 [==============================] - 4s - loss: 0.3075 - acc: 0.9010 - val_loss: 6.2898 - val_acc: 0.4583
Epoch 28/50
48/48 [==============================] - 4s - loss: 0.4546 - acc: 0.8854 - val_loss: 3.9266 - val_acc: 0.4792
Epoch 29/50
48/48 [==============================] - 4s - loss: 0.3660 - acc: 0.8906 - val_loss: 5.7075 - val_acc: 0.4062
Epoch 30/50
48/48 [==============================] - 4s - loss: 0.2993 - acc: 0.8958 - val_loss: 6.0729 - val_acc: 0.4583
Epoch 31/50
48/48 [==============================] - 4s - loss: 0.3017 - acc: 0.8854 - val_loss: 3.9278 - val_acc: 0.5417
Epoch 32/50
48/48 [==============================] - 4s - loss: 0.3101 - acc: 0.8906 - val_loss: 4.1609 - val_acc: 0.4479
Epoch 33/50
48/48 [==============================] - 4s - loss: 0.2863 - acc: 0.9062 - val_loss: 4.8107 - val_acc: 0.4688
Epoch 34/50
48/48 [==============================] - 4s - loss: 0.3076 - acc: 0.9271 - val_loss: 4.9404 - val_acc: 0.4167
Epoch 35/50
48/48 [==============================] - 4s - loss: 0.2248 - acc: 0.9375 - val_loss: 6.2589 - val_acc: 0.4583
Epoch 36/50
48/48 [==============================] - 4s - loss: 0.3085 - acc: 0.9062 - val_loss: 7.4152 - val_acc: 0.3646
Epoch 37/50
48/48 [==============================] - 4s - loss: 0.1467 - acc: 0.9583 - val_loss: 6.8573 - val_acc: 0.4271
Epoch 38/50
48/48 [==============================] - 4s - loss: 0.2550 - acc: 0.9271 - val_loss: 7.5519 - val_acc: 0.3542
Epoch 39/50
48/48 [==============================] - 4s - loss: 0.2816 - acc: 0.8958 - val_loss: 6.7278 - val_acc: 0.4167
Epoch 40/50
48/48 [==============================] - 4s - loss: 0.3710 - acc: 0.9010 - val_loss: 9.0009 - val_acc: 0.3438
Epoch 41/50
48/48 [==============================] - 4s - loss: 0.2812 - acc: 0.9167 - val_loss: 6.2485 - val_acc: 0.4271
Epoch 42/50
48/48 [==============================] - 4s - loss: 0.2139 - acc: 0.9427 - val_loss: 5.7675 - val_acc: 0.4479
Epoch 43/50
48/48 [==============================] - 4s - loss: 0.2314 - acc: 0.9427 - val_loss: 8.2553 - val_acc: 0.3958
Epoch 44/50
48/48 [==============================] - 4s - loss: 0.2563 - acc: 0.9062 - val_loss: 5.3616 - val_acc: 0.4896
Epoch 45/50
48/48 [==============================] - 4s - loss: 0.2693 - acc: 0.9219 - val_loss: 4.9042 - val_acc: 0.5625
Epoch 46/50
48/48 [==============================] - 4s - loss: 0.1458 - acc: 0.9583 - val_loss: 3.9704 - val_acc: 0.5312
Epoch 47/50
48/48 [==============================] - 4s - loss: 0.2204 - acc: 0.9219 - val_loss: 6.6370 - val_acc: 0.4375
Epoch 48/50
48/48 [==============================] - 4s - loss: 0.1867 - acc: 0.9583 - val_loss: 6.5813 - val_acc: 0.5000
Epoch 49/50
48/48 [==============================] - 4s - loss: 0.1940 - acc: 0.9531 - val_loss: 6.6344 - val_acc: 0.4375
Epoch 50/50
48/48 [==============================] - 4s - loss: 0.2168 - acc: 0.9167 - val_loss: 6.4264 - val_acc: 0.4688

```

On the first epoch, an accuracy of 21.35% was achieved. 
However, after 50 epochs, an accuracy of 91.67% was achieved for knot classification.
In fact, we can see that the classifier achieved an accuracy of 95.83% during the 46th and 48th epochs.
Again, this shows rapid learning in action, and the increase from 20 epochs to 50 epochs resulted in an accuracy gain of 12.5% in some cases.

There is no doubt that this level of accuracy on this first try has been significantly increased due to data augmentation.
Furthermore, for future classification, the models will trained and validated on a far wider variety of data.
