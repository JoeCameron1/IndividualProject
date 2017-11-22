# Week 8 Status Report

The first goal I set out to accomplish this week was the completion of my second dataset. 
I finished collecting data for my second dataset. 
My second dataset now contains images of the five knots from my initial dataset, this time with a non-reflective background.

Next, I decided that I should try knot classification again, although this time, I trained the network on my complete initial dataset and tested the network's accuracy on images I downloaded from ImageNet. 
I call this dataset a ‘wild’ dataset, as the validation images are not part of my original dataset, and there are external variations (such as rope type, background etc.). 
The trained CNN managed an accuracy of 90% after 50 epochs on this ‘wild’ dataset.

Following from last week’s meeting, I also decided to alter my Keras model in my classification script. 
First, I increased the batch_size from 4 to 8 and ran the classification script. 
The batch_size increase immediately improved the accuracy from 90% (attained last week) to 95% after 50 epochs when trained on my initial dataset. 
Next, I experimented with separately adding normalisation layers and a Gaussian noise layer. 
The normalisation layers seemed to decrease the network accuracy slightly. 
However, the addition of one Gaussian noise layer increased the 90% accuracy achieved on the ‘wild’ dataset to 95%. 
In the process of learning about these layers and their purpose, I managed to find many useful papers from the University of Toronto (Hinton etc.), so I plan to spend more time over the coming weeks deepening my understanding of the dropout and normalisation concepts.

Similarly to the normalisation layers, I experimented with the Adam optimiser function in the model.compile method, although the original RMSprop optimiser function seemed to outperform Adam consistently. 
After finding a paper on Adam by Hinton, I also plan to deepen my understanding of optimiser functions during the next week. 
