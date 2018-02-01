# Week 14 Status Report

The first accomplishment I managed this week was uploading my updated Keras to CoreML model converter script to the repository. 
The script is called ‘convertModel.py’. 
This update has now made my knot classification app slightly more accurate and far more precise regarding prediction accuracy when compared to last week’s version.

Furthermore, this week, I managed to make some observations and insights into my knot classification. 

Firstly, I noticed that my original models were massively overfitting to the original datasets, as the training accuracy was approximately 90%, whereas the validation accuracy never increased over 50%. 
Upon noticing this observation, I decided to immediately rearrange my dataset. 
Originally, my model trained and validated on different lighting conditions. 
Now, my model is trained on all of my controlled reflective background data and some ‘wild’ data. 
The validation set was a random selection of photos from the training set, until I reached a desirable 80% training - 20% validation split. 
Of course, these validation images were removed from the training dataset. 
After training/validating my model on this new dataset, I reached a training accuracy of approximately 75%-80% and a validation accuracy of approximately 60%-65%. 
This is a far more desirable result and shows that the model trained on this new dataset does not overfit as much. 
This means that I can possibly conclude that lighting can impact the classification accuracy significantly. 
The plot of the original model’s training history is illustrated in the attached image ‘original_TrainingHistory.jpg’ and the plot of the new model’s training history is illustrated in the attached image ’new_TrainingHistory.jpg’.

Secondly, I managed to implement t-SNE visualisation of my model’s learned representations. 
An example of the t-SNE plot produced is illustrated in the attached image ’tsneVisualisation.jpg’. 
The code to achieve this is located in the ‘knotClassifier.py’ script.

Lastly, I have also given the multi-output CNN classifier much thought by fully researching data generators in Keras. 
It seems that the Data Augmentation functionality is the major advantage of using data generators, therefore I plan to continue using them. 
Thankfully, I now understand these structures more thoroughly, as shown by their use in my t-SNE visualisation code in the ‘knotClassifier.py’ script. 
So far I’m using a separate CNN trained on another dataset (with the tensions representing classes), however, I’m still coming up with a way to join all of these classifications into one single CNN.
