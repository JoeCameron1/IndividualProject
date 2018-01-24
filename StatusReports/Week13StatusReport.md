# Week 13 Status Report

This week has been very productive for me.

First, I committed my fourth controlled dataset (non-reflective background for the extra five knots) to the repository. 

Then, I decided to begin researching the Keras Functional API that will allow me to create multi-output Keras models. 
However, I became a little bit confused over how I will create another output (along with my array describing the knot type) describing knot tension. 
I’m undecided between training a separate network that will classify tension and then merge the results together, or creating the multi-output network as we discussed previously.

After looking at the Keras Functional API, I decided to try and implement TSNE visualisation into my classifiers, however, I also got extremely confused over this. 
I tried to use the TSNE function from sklearn, although I was having difficulty with extracting the weight from my Keras model correctly. 
I feel that I may be missing the correct way to do this in Keras at the moment. 
Even though this was slightly disappointing, I thought to add some form of visualisation to my classifiers, so I implemented some code that plots the classification training history with matplotlib. 
This is somewhat useful to quickly analyse each training session.

Next, I decided to fully utilise my new datasets by expanding my classifier to classify 10 knots. 
I updated the dataset and the classification script to do so, and I immediately got promising results, where the training accuracy peaked at 90% after 50 epochs.

After all of this, I turned my attention towards implementing my first GAN in Keras. 
I aimed to develop a GAN that could synthesise MNIST images, and after using the GAN hacks git repo and a few other examples, I managed to get an initial version of a Deep Convolutional GAN working. 
I committed this to my repository under the ‘KerasTutorials' folder.

Finally, I managed to develop an initial version of an iOS app that implements one of my early Keras models to classify knots. 
This is perhaps my biggest progression this week, as I now have the application on my phone with an interface to display the output from the CNN. 
To create this app, I had to write a python script that converts Keras HDF5 files into CoreML models that can be used in iOS apps. 
The app uses real-time footage from an iPhone camera to classify knots on the fly. 
I plan to show this app in the next meeting.
