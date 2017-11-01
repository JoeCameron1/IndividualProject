# Week 5 Status Report

This week, my primary goal involved creating an initial dataset from which I can start training the convolutional neural network. 
I managed to achieve this over the past week. 
I have collected 288 images of 5 different knots, specifically, the Fisherman’s Knot, the Reef Knot, the Alpine Butterfly Knot, the Overhand Knot and the Bowline Knot. 
This list of five knots has changed from last week. 
I feel that in this initial stage, it is necessary to start classifying basic knots of ancient origin, rather than attempting to classify complicated variations of knots. 
For example, last week I mentioned that I should gather data on the mountaineer’s coil knot, however on closer inspection, I realised that the mountaineer’s coil (and many other knots) was merely composed of many overhand knots and loops. 
Hence, it makes more sense to gather data on the overhand knot first. 
For each knot, I took a photo for every 90 degrees of 3d rotation, as this cannot be achieved by data augmentation. 
Following from this theme, I took data of every knot under different lighting conditions (diffuse lighting, source lighting from above and source lighting from the side) and different tensions (very loose, loose and set). 
My plan for this initial dataset is within the ‘Datasets’ folder on my GitHub repository. 
Next week, I shall start augmenting this dataset within Keras to ultimately train a network model within Keras.

Over the past week, I also managed to download the dissertation template and start adding my structure/content to it. 
While doing this, I also realised that I should add an acknowledgements section along with a contents section into my dissertation structure.

One of my most productive accomplishments this week involved background research. 
I conducted some thorough research on neural networks, image classification and generative adversarial networks, and found many useful papers to start constructing a background chapter. 
Most notably, I found the ‘Very Deep Convolutional Networks for Large-Scale Image Recognition’ journal article by Karen Simonyan and Andrew Zisserman. 
This article will prove very useful for my knot classifier, as it lays out the VGG-16 network model, which has shown incredible accuracy for large-scale image recognition problems. 
In total, this week, I have added 15 papers to my Zotero database that hold some relevance to this project.
