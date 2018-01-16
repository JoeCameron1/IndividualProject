# Week 2 Status Report

This week, one of my main goals was to download Tensorflow and the Keras API in order create my first Neural Network model and train it on the MNIST data set. 
I managed to do this, and the network I made had an error of only 1.8%. 
I’ve also become more comfortable with the Keras API features and syntax.

My other main goal was to define the scope of this project. 
The aim of this project is to firstly, classify popular knots from knot families using Convolutional Neural Networks. 
I propose to try and classify the 5 most popular knots from the 5 most popular knot families at first. 
Once classified, a Generative Adversarial Network should then generate a 3D model representing the topology of the knot in question. 
Another aim of the project is to develop an appropriate data set of labelled knot photos with varying features to train these networks on. 
The varying features of the photos will include the type of knot, the type/state of material used to tie the knot, the brightness of the photo and the background of the photo at the very least. 
With time, I hope to come up with more variables. 
I also came across this very interesting article written by Francois Chollet himself on data augmentation in Keras: https://blog.keras.io/building-powerful-image-classification-models-using-very-little-data.html. 
This has given me a platform to start thinking about expanding any possible data set I create. 
If I manage to achieve this in due time, I would certainly consider packaging the trained models into a mobile application of some sort.
