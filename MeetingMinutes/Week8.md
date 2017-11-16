# Week 8 Meeting Minutes

The meeting started with an overview of goals achieved in week 7.
I started by explaining my knot classifier, and the results it achieved on my initial dataset.
John first stated that he was very pleased with my knot classifier so far, and emphasised that the next step is to find the network's breaking point.
This is important, as my analysis section of the dissertation will partly consist of analysis into what variable changes make for a good or bad knot classifier.

Next, John relayed some general advice on the network model itself.
John noticed that during the later epochs of training, my network can fluctuate in accuracy.
In order to fix this, John reccommended adding the 'adam' optimser to my model's compilation method.
Furthermore, John reccommended adding a normalisation layer in between every convolution and activation layer.
The purpose of this is to help reduce overfitting, but I should explore this further.
John also suggested that I should consider adding dropouts to the network in strategic locations.

Next, John also pointed out that I could expand my data augmentation.
One way to do this is to add Gaussian noise to the images, this could reduce overfitting.
This coming week, I will spend some time exploring ways to expand my data augmentation.

The conclusion of the meeting revolved around the dissertation.
Specifically, John pointed out that I should start thinking about ways to visualise my results, by way of graphs.
Another goal for the upcoming week is to display results via graphs, and start thinking of various methods to do this.
