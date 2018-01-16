# Week 9 Status Report

The first task I set out to do this week was the flipped dataset experiment, where I trained my neural network on the wild dataset I gathered last week and validated the network on my dataset.
Once training and validation had completed, the network achieved an accuracy of approximately 90%, which is a 5% decrease from the accuracy obtained by training and validating with the opposite datasets.
Nevertheless, this is still a promising result, as the network only had 40 images to train on, and was validated on 288 images.
Although, it must be noted that I kept the same values for the number of training and validation samples from before the flip, so that the epoch iterations could be the same.

Next, I focused my attention towards expanding my datasets. 
Initially, I gathered more data for my ‘wild’ dataset of knot images downloaded from ImageNet. 
However, I quickly realised that the 40 images I gathered last week seem to have been recirculated throughout ImageNet, and I had exhausted its resources. 
In light of this realisation, I switched my focus to downloading images from Google, and I have managed to add approximately 30 images to my wild dataset. 
Next week, I will continue to focus on gathering more images for this wild dataset and try contacting knot enthusiasts to see if they would be willing to share their photos. 

I then proceeded to gather some more data for my dataset. 
I gathered images of knots in differing backgrounds and knots in dental floss. 
This is an area I certainly plan to focus more heavily on throughout December.

The final task I completed this week was the experimentation with dropout layers in my CNN model. 
Upon adding dropout layers, I noticed a 5-10% decrease in accuracy, although it is hoped that this will help prevent overfitting when training on larger datasets.

Over the upcoming two weeks, I hope to fully use the time to implement a multi-output CNN, develop my datasets and experiment with visualisation of the network (TSNE).
