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
16/11/2017 | |
17/11/2017 | |
18/11/2017 | |
19/11/2017 | |
20/11/2017 | |
21/11/2017 | |
22/11/2017 | |
