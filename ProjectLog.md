# Project Log

## Week 1

Date | Duration | Summary
------------ | ------------- | -------------
30/09/2017 | 4 Hours | Downloaded and installed Zotero as a tool to keep track of references & bibliography. Beginning research on what tools I can use in my project. What deep learning framework shall I use and why?
01/10/2017 | 4 Hours | Started reading background research on Machine Learning techniques. Also gathered knowledge on what makes a good data-set for machine learning applications. Started reading up on Convolutional Neural Networks and Generative Adversial Networks.
02/10/2017 | 4 Hours | Made an account on Arxiv Sanity Preserver. Started getting familiar with Arxiv Sanity Preserver in order to search/read academic papers in my project’s field. Also started looking for any appropriate data sets (pictures of knots). Found some useful datasets on Image-Net. Read “colah’s blog” and some of Andrej Karpathy’s blog.
03/10/2017 | 2 Hours | Read some of Michael Nielsen’s Deep Learning Book and Deep Learning by Ian Goodfellow, Yoshua Bengio and Aaron Courville.
04/10/2017 | 2 Hours | Decided on using Keras as my deep learning framework. After further research, I am now fairly certain that CNNs will be useful in classifying knots, while GANs will be useful in displaying the knot topology. Read some papers by Dr Mike Pound (Known for Computerphile).


## Week 2

Date | Duration | Summary
------------ | ------------- | -------------
05/10/2017 | 1 Hour | Read the opening chapter of the ‘Ashley Book of Knots’. 
06/10/2017 | 2 Hours | Downloaded Tensorflow and the Keras API.
07/10/2017 | 2 Hours | Started figuring out the scope of this project, what variables to change, and limitations of the project.
08/10/2017 | 1 Hour | Created my first Neural Network using Tensorflow and the Keras API, and trained it on the MNIST data set.
09/10/2017 | 2 Hours | Researching Keras and Tensorflow.
10/10/2017 | 2 Hours | Found a very interesting article on the Keras Blog by Francois Chollet on data augmentation: https://blog.keras.io/building-powerful-image-classification-models-using-very-little-data.html. Giving me a platform to expand any data set I create in the future.
11/10/2017 | 1 Hour | Researching how to make machine learning data sets.


## Week 3

Date | Duration | Summary
------------ | ------------- | -------------
12/10/2017 | 2 Hours | Started considering what variables should be considered invariant to the convolutional neural network for classifying knots. Image rotation, image brightness and horizontal/vertical flip should definitely be invariants to the knot classification. This is because knots should be identified whatever the rotation, orientation or brightness of a photograph.
13/10/2017 | 1 Hour | Completed a tutorial on training a basic neural network on the Cifar-10 dataset. (commit: 3ed9858)
14/10/2017 | 1 Hour | Completed a tutorial on training a convolutional neural network on the Cifar-10 dataset. (commit: 3ed9858)
15/10/2017 | 2 Hours | Researched the various terms of machine learning, such as classification and  clustering using Michael Nielsen’s Deep Learning book as a reference.
16/10/2017 & 17/10/2017 | 1 Hour | Started working on the data augmentation tutorial by Francois Chollet found at https://blog.keras.io/building-powerful-image-classification-models-using-very-little-data.html. Generally just figuring out how to successfully build, use and augment a dataset suitable for machine learning applications using Keras.
18/10/2017 | 1 Hour | Made a private GitHub repository for this project.


## Week 4

Date | Duration | Summary
------------ | ------------- | -------------
19/10/2017 | 3 Hours | Researched and selected five knots to gather data on. These five knots are, The Fisherman’s Knot, The Reef Knot, The Mountaineer’s Coil, The Noose and The Alpine Butterfly Knot. My initial dataset will involve these five knots. 
20/10/2017 | 2 Hours | Completed Francois Chollet’s data augmentation tutorial on the Keras Blog https://blog.keras.io/building-powerful-image-classification-models-using-very-little-data.html. Uploaded my code to this repository. (commit: fe8498b)
23/10/2017 | 1 Hour | Started initial planning on the structure of my dissertation.
24/10/2017 | 1 Hour | Reflecting on my dataset variables, and decided to add image contrast, as this could provide useful comparisons in the knot classifier’s performance.
25/10/2017 | 1 Hour | Decided on an initial dissertation structure. (commit: 3c02019)


## Week 5

Date | Duration | Summary
------------ | ------------- | -------------
26/10/2017 | 1 Hour | Updated my dissertation structure (commit: 43e8dac).
27/10/2017 | 2 Hours | Outlined an official plan for my first dataset of knots (commit: edea2f2). This initial dataset will contain images of five knots. These five knots are, The Overhand Knot, The Fisherman’s Knot, The Reef Knot, The Alpine Butterfly Knot and The Bowline Knot. This has changed from the five knots laid out last week, as I feel it is more important to make an initial dataset that covers five fundamentally important knots of ancient origin, and focus on specific knot variations later on in the classification process.
28/10/2017 | 2 Hours | Gathered data for the Fisherman’s Knot.
29/10/2017 | 3 Hours | Conducted thorough background research and discovered many useful journal articles, notably ‘Very Deep Convolutional Networks for Large-Scale Image Recognition’ authored by Simonyan, Karen and Zisserman, Andrew. This article should prove very useful for the knot classifier CNN model.
29/10/2017 | 2 Hours | Gathered data for the Reef Knot.
30/10/2017 | 2 Hours | Gathered data for the Alpine Butterfly Knot.
30/10/2017 | 1 Hour | Downloaded the dissertation template and added my personal details and dissertation structure to it.
31/10/2017 | 1 Hour | Gathered data for the Overhand Knot.
31/10/2017 | 2 Hours | Gathered data for the Bowline Knot, hence completing the data collection for my initial dataset.
01/11/2017 | 1 Hour | Updated my dissertation structure to include Acknowledgements and Contents Sections. Also added an Objectives subsection to the Introduction section.


## Week 6

Date | Duration | Summary
------------ | ------------- | -------------
02/11/2017 | 1 Hour | Gathered data for the Overhand Knot, this time with a non-reflective background.
03/11/2017 | 1 Hour | Gathered data for the Alpine Butterfly Knot, this time with a non-reflective background.
06/11/2017 | 1 Hour | Considered 5 new knots to add to my initial dataset. These knots are, the Figure-8 Loop, the Clove-Hitch Knot, the Savoy Knot, the Flemish Bend Knot and the Slip Knot.
07/11/2017 | 2 Hours | Wrote a bash script for resizing images within a dataset.
08/11/2017 | 2 Hours | Wrote a python script, called 'ResizeDataset.py', for resizing images within a dataset. This python script replaces the previous bash script as it is more portable between different OS environments. It is important automate the process of data compression for everyone who wants to use my software.


## Week 7

Date | Duration | Summary
------------ | ------------- | -------------
09/11/2017 | 2 Hours | Fully tested my python script for resizing images within a dataset. Subsequently committed the script to my repository (commit: 8af2663).
09/11/2017 | 1 Hour | Resized my initial dataset using my python script 'ResizeDataset.py' and committed this resized dataset to my repository (commit: 21e2f38).
10/11/2017 | 2 Hours | Started writing a python script, using Keras and Tensorflow, that can train a neural network to classify five different knots using my initial dataset uploaded to this repository previously with commit 21e2f38. This script was written with inspiration from all the previous Keras tutorials I completed.
11/11/2017 | 2 Hours | Thoroughly reviewing all meeting minutes collected from meetings with my supervisor John. Uploaded these minutes to this repository.
13/11/2017 | 5 Hours | Continuing with my classification script. Started training my CNN with my dataset, but an accuracy of 25% was consistently yielded. After many hours of debugging, the issue was not found.
14/11/2017 | 3 Hours | Finally solved the issue in my classification script. First, I had to change all classification modes from 'binary' to 'categorical', this allows for multi-class classification, which is essential as I want to classify five different knots. Second, I had to change the last activation layer from 'sigmoid' to 'softmax' and change its output shape from '(None, 1)' to '(None, 5)'. Again, this all allows for multi-class classification, specifically five-class classification. After these changes, the CNN started to show great increases in accuracy, thus it was beginning to learn. The CNN was now yielding an accuracy of up to 95%. Committed this classification script to this repository (commit: c0b6406).
14/11/2017 | 2 Hours | Conducted experimentation on my CNN for knot classification, and wrote a document to explain the results of the experiments and the knot classifier itself. Subsequently, I committed the document to this repository (commit: 02d41bf).


## Week 8

Date | Duration | Summary
------------ | ------------- | -------------
16/11/2017 | 1 Hour | Gathered data for the Fisherman's Knot on a non-reflective background, for my second dataset.
17/11/2017 | 1 Hour | Gathered data for the Reef Knot on a non-reflective background.
18/11/2017 | 1 Hour | Gathered data for the Overhand Knot on a non-reflective background.
19/11/2017 | 1 Hour | Gathered data for the Alpine Butterfly Knot on a non-reflective background.
20/11/2017 | 1 Hour | Gathered data for the Bowline Knot on a non-reflective background, hence completing my second dataset.
21/11/2017 | 2 Hours | Gathered/Downloaded images of the five knots in order to create a validation dataset that is completely separate from the dataset I am creating.
21/11/2017 | 1 Hour | Ran my classification script, this time training the CNN on my complete initial dataset, and validating on the 'wild' dataset I created the previous day. After 50 epochs, the classification CNN achieved an accuracy of 90%.
21/11/2017 | 1 Hour | Experimented with the optimizer function in my model.compile method within my classification script. Initially, I changed the optimizer function from rmsprop to adam, although rmsprop seemed to outperform adam consistently. I will have to spend more time fully understanding optimizer functions next week. 
22/11/2017 | 2 Hours | Making adjustments to my classification script by changing my Keras model. I increased the batch_size from 4 to 8, this showed an increase in accuracy from approximately 90% to approximately 95%. Next, I experimented with normalisation layers and Gaussian noise layers. Gaussian noise appeared to slightly improve accuracy, although normalisation layers did the opposite. I will also have to spend time next week exploring these concepts further.


## Week 9

Date | Duration | Summary
------------ | ------------- | -------------
23/11/2017 | 1 Hour | Trained my CNN model on my wild validation set and validated the network on my training set, effectively flipping the datasets. This provides more insight to the behaviour of my CNN. I managed to obtain a 90% accuracy with this.
27/11/2017 | 2 Hours | Gathered more data to add to my wild dataset from ImageNet and Google Images.
28/11/2017 | 2 Hours | Gathered data for my dataset. These images consisted of knots and various backgrounds along with knots tied in dental floss. The objective of this is to find the limitations of my knot classifier.
29/11/2017 | 2 Hours | Experimenting with the addition of dropout layers to my CNN model.


## Week 10

Date | Duration | Summary
------------ | ------------- | -------------
30/11/2017 | 2 Hours | Collecting more photos from the internet to add to my 'wild' dataset.
01/12/2017 | 3 Hours | Started collecting data for my own 'wild' dataset. This dataset contains my images of knots that are not in a controlled environment. Furthermore, there is a variety of material used to tie the knots.
04/12/2017 | 3 Hours | Finished collecting data for my 'wild' dataset.
05/12/2017 | 2 Hours | Started collecting data for my own dataset covering the extra five knots I selected earlier. These knots are, the Figure-8 Loop, the Clove-Hitch Knot, the Savoy Knot (Figure-8 Knot), the Flemish Bend Knot and the Slip Knot. Specifically, I gathered data for the Figure-8 Loop. 
06/12/2017 | 6 Hours | Started getting familiar with Blender (and the Blender Python API for scripting), which I plan to use in order to create a huge volume of data with which my neural networks can train on.


## Week 11

Date | Duration | Summary
------------ | ------------- | -------------
07/12/2017 | 1 Hour | Continued collecting more data for the 'wild' dataset of images from the internet.
08/12/2017 | 2 Hours | Gathered data for the Clove-Hitch Knot.
11/12/2017 | 4 Hours | Gathered data for the Figure-8 Knot, the Flemish Bend Knot and the Slip Knot.
12/12/2017 | 5 Hours | Further experimentation with scripting in Blender, specifically creating the 3D models of the knots and writing scripts to capture photos from different angles. This script still needs further improvement however.


## Christmas Break

Date | Duration | Summary
------------ | ------------- | -------------
14/12/2017 | 4 Hours | Conducted research on t-SNE (Geoffrey Hinton and Laurens van der Maaten) and visualisation of deep learning data. Started experimenting with visualisation techniques on my own knot classifier.
15/12/2017 | 2 Hours | Wrote my end-of-semester-1 status report. 
18/12/2017 | 2 Hours | Began gathering data for the extra five knots, this time with a non-reflective background. I gathered data for the Figure-8 Knot first.
19/12/2017 | 2 Hours | Gathered data for the Figure-8 Loop.
20/12/2017 | 7 Hours | Figured out how to control and take photos with the camera in Blender via a python script.
04/01/2018 | 2 Hours | Gathered data for the Clove Hitch.
05/01/2018 | 2 Hours | Gathered data for the Slip Knot.
06/01/2018 | 2 Hours | Gathered data for the Flemish Bend and completed data collection for the non-reflective controlled dataset.


## Week 12

Date | Duration | Summary
------------ | ------------- | ------------- 
14/01/2018 | 4 Hours | Trying to model knots such as the Figure-8 loop in Blender.
16/01/2018 | 8 Hours | Trying to model knots such as the Overhand Knot and the Flemish Bend in Blender, however it is a very long a tedious process.
17/01/2018 | 1 Hour | Committed my datasets created over the Christmas Break.


## Week 13

Date | Duration | Summary
------------ | ------------- | -------------
18/01/2018 | 4 Hours | Researching the Keras Functional API that will allow me to create multi-input/multi-output models, instead of just sequential models. 
19/01/2018 | 5 Hours | Trying to implement TSNE visualisation to my python scripts, although this will require more time and understanding. 
20/01/2018 | 4 Hours | Expanding my classifier to classify 10 knots. Initial results show a 90% training accuracy.
21/01/2018 | 6 Hours | Exploring implementations of GANS in Keras. I plan to make a GAN that can synthesise MNIST images this week.
22/01/2018 | 5 Hours | Yet more TSNE research.
23/01/2018 | 4 Hours | Developed my first GAN that can synthesise images based on the MNIST dataset!
23/01/2018 | 1 Hour | Developed and commited new code to plot the training history of my models.
23/01/2018 | 6 Hours | Began developing an iOS app, where I can use my Keras classification models in real-time. This makes sense, because users are most likely to use a mobile device to undertake such a task (usually outdoors with limited access to a desktop computer). So far, I have developed an application that can capture images from the camera to be sent as an input to a CoreML model.
23/01/2018 | 2 Hours | Wrote a python script that can convert Keras models saved as HDF5 files into CoreML models that can be used in iOS apps.
24/01/2018 | 6 Hours | Finished an initial version of the iOS Knot Classifier app. I managed to successfully convert a Keras HDF5 model into a CoreML model, and pass real-time camera footage from an iPhone as an input to my model. A label on the interface updates with the classification identifier (label) and a percentage representing the model's certainty of the classification.


## Week 14

Date | Duration | Summary
------------ | ------------- | -------------
25/01/2018 | 3 Hours | Noticed that my models tended to significantly overfit to the training data, meaning a high training accuracy is achieved, but a low validation accuracy is also a result. Began to reorganise my training and validation datasets to combat this. 
26/01/2018 | 3 Hours | Updated my Keras to CoreML model conversion script to now also rescale images before being sent to my convolutional neural network. I then committed this script to the repository. 
27/01/2018 | 4 Hours | Conducted research on TensorBoard, and how I could possibly use TensorBoard to visualise my models in the future. Figured out how to do this via Keras callbacks, but I still need to figure out how to include embeddings which would allow me to visualise a model's learned representation via t-SNE. 
29/01/2018 | 4 Hours | Conducted some experimentation with my training my models on some newly rearranged datasets, and managed to plot graphs that show the models do not overfit when trained on all data. Before, the models began to overfit when trained and validated on different lighting conditions within the images. However, the new dataset trains on images with all lighting conditions and the model's training and validation accuracy is approximately equal. 
30/01/2018 | 6 Hours | Figured out a way to successfully implement t-SNE visualisation for a model's learned representation. The code to achieve this is located within the 'knotClassifier.py' script. 
31/01/2018 | 3 Hours | Implemented a quick CNN that can classify the tension a knot is tied at. This is a possible stepping stone to creating a GAN that can generate images of knots at different tensions in the future, but I must still try and implement one single CNN that can achieve all of this. 


## Week 15

Date | Duration | Summary
------------ | ------------- | -------------
01/02/2018 | | 
02/02/2018 | | 
03/02/2018 | |
04/02/2018 | | 
05/02/2018 | | 
06/02/2018 | | 
07/02/2018 | |
