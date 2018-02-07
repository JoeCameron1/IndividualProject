# Week 15 Status Report

This week, I began with a test of my t-SNE validation on MNIST data, and it appeared to work very smoothly as noticeable clusters were formed. 
The t-SNE visualisation produced is attached as ’tsneVisualisation.jpg’. 
Hence, it was good to confirm that t-SNE was working as it should.

I then decided to further tackle the issue of overfitting I spotted in my classifier last week. 
This time, I trained my network on my controlled datasets and validated on the ‘wild’ dataset. 
Unfortunately, the results were not good initially (approximately 90% training accuracy with 20% validation accuracy), but then I made a few changes to my CNN model architecture (committed to GitHub) by adding more BatchNormalization and Dropout and improved the validation accuracy to approximately 40% with the same training accuracy. 
Realising that my classifier is constrained by the data, I decided to implement transfer learning, by adding the InceptionV3 model on top of a simple dense layer neural network and turning the InceptionV3 layers to non-trainable. 
However, transfer learning did not seem to improve anything in terms of validation accuracy, so I’m not sure if this is a sensible avenue to pursue.

Next, I wrote a draft of the introduction to my dissertation and added some new structure to the rest of the dissertation. 
I have attached my dissertation PDF as ‘dissertation.pdf’ for you to review.

The final thing I managed to do this week was implement a convolutional autoencoder to encode my dataset images and decode into a new synthesised image. 
Although the image does not appear to be clear and can appear blurry, the outline of the knot is visible. 
The code for this is now on my repository. 
