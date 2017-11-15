# Week 7 Status Report

Early this week, I managed to thoroughly test my python script ‘resizeDataset.py’ and commit it to my repository along with my initial dataset that had been resized by the script.

Throughout the rest of the week, I focused on making the knot classifier, using Keras & Tensorflow, where I could train a neural network model on my resized dataset and evaluate the results. 
Initially, my convolutional neural network was consistently 25% accurate at knot classification. 
However, this was because I based my classification script on Keras tutorials I had completed so far. 
For my specific classification problem, it became apparent that I must tailor a script to suit my own needs. 
First, I created my own data augmentation generator using the ImageDataGenerator Keras class. 
Next, I created a network model to perform 5-class classification, where each class represents a type of knot I wish to classify. 
Eventually, I managed to successfully train a convolutional neural network to classify knots with an accuracy of 80% over 20 epochs and 90% over 50 epochs. 
For classification training over 50 epochs, the classifier was initially only 20% accurate on the first epoch, but showed significant increases in accuracy over every subsequent epoch, eventually reaching approximately 90% on the 50th epoch, thus showing explicit learning. 
Obviously, the training and validation datasets used for this classifier have influenced the high accuracy, and the datasets must be improved and expanded for future classifiers, but these promising results have positively confirmed that I seem to be following the right trajectory, concerning my datasets, data augmentation and Keras model.

On an administrative note, I have also decided to now add minutes from weekly supervision meetings to the repository for easy access.
