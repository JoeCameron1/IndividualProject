# Week 14 Meeting Minutes - 25/01/2018

The meeting started with a review of my progress this week, mainly a review of my iOS app. 
John and I tested the app out on knots tied with rope.
John was pleased with the initial idea/interface, although noticed some flaws in the classification.
I agreed, and proposed that the issue might be related to the fact that I'm currently not scaling images in my CoreML model, as I do in my Keras model.

The rest of the meeting was a discussion about ironing out some of the problems I had experienced with t-SNE and the multi-output CNN over the past week.
For t-SNE, John suggested that I consider making a 2D output layer in my CNN, as this will satisfy the requirements of the t-SNE algorithm.
For the multi-output, we both concluded that I need to gain further control over how my dataset is fed into the network and how the class labels are created.
Once I get a hold of this, the multi-output CNN classifying both knot type and tension should become a reality. 

My goal over the next week is to fix these two issues.
