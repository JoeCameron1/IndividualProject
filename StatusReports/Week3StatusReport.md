# Week 3 Status Report

This week, I have focused heavily on datasets, as I would like to make my own in the coming weeks. 
Specifically, I have focused on Data Augmentation in Keras using the ImageDataGenerator class, and how I would apply this to my dataset for this project. 

I have identified variables that I would like my neural network to consider invariant. 
I would plan to use data augmentation to achieve this. 
Firstly, I would like to rotate all images in my dataset at every degree of rotation. 
For this project, I feel this makes sense because I want to be able to classify knots no matter what angle they are photographed/placed at. 
I want to augment the image brightness, as I would also want to classify knots no matter what the specific brightness of a photo is. 
I would also like to flip every image horizontally and vertically to allow the network to identify knots no matter the orientation in which they have been tied. 
You mentioned rope tension in our last meeting, I certainly want to include this to the list, as knots can be tied at many different tensions in the real world. 
That should not stop the network from correctly classifying. 
I’m hoping that this will help prevent the networks overfit with respect to the dataset.

Furthermore, I decided to spend some more time reading Michael Nielsen’s Deep Learning book, specifically looking at clustering and classification techniques. 
The difference between classification and clustering is certainly interesting in the scope of this project. 
Along with classification, it may be nice to also group similar knots into clusters.

I completed a few more tutorials on Keras, this time with the CIFAR-10 dataset, to further my understanding of Keras and the implementation of convolutional neural networks. 

I also set up a private GitHub repository for the project this week. 
Currently, the code from my MNIST and CIFAR10 tutorials are there, along with a log of my project work and weekly status reports.
