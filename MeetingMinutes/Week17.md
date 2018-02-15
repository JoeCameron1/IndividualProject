# Week 17 Meeting Minutes - 15/02/2018

The meeting began with an overview of my progress with my CNN model.
Over the past week, I fixed some bugs in the data augmentation and made some small tweaks to the model architecture which resulted in a training accuracy and a validation accuracy of ~65%.
John mentioned that the model may be actually underfitting now, and suggested that I now train my CNN on Google's Colaboratory GPUs for more epochs.
This added training power may significantly improve the performance.

Next, we discussed my upcoming plans for the GAN, where I wish to manipulate tension.
We both agreed that a Conditional GAN implementation would be the only way to achieve this, and I plan to finish this before March.

The meeting ended with discussion about the dissertation.
John confirmed that the structure I have laid out for the Background chapter so far is appropriate, so I plan to continue writing this chapter over the next week.
Next, John asked me for my plans on the evaluation.
I stated that I plan to run experiments on how the dataset influences the classification, and how the model influences the classification.
John thought this was sensible and suggested that I take experiment with the model by taking out certain layers and observing the results.
I then reiterated that I plan to use the same approach with the dataset experiments.
Next, I also discussed my plans to run evaluation of the entire dataset and entire neural network for performance evaluation.
John also stressed that I use confusion matrices to display the results, as these can uncover certain phenomena in the classification, such as consistent misclassification for another knot.
