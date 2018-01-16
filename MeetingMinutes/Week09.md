# Week 9 Meeting Minutes

The meeting started with an overview of what I had achieved over the past week.
John noted that my results for classification of the wild dataset were very good.
I then proceeded to show John examples of images that I used to obtain this result.
John then suggested that I expand the validation dataset, from 40 images to 80 images, or as much as possible.
It's also a good idea for me to create another dataset of 'wild' images that I have downloaded from Google, although it must be noted that I can only distribute my own images, not those from ImageNet or Google.
Furthermore, we talked about possible licensing for my dataset.
I have decided to eventually release my dataset on a service such as Kaggle, with a permissive license such as MIT.

Continuing discussion about datasets, John also pointed out that I should now try to take as many photos of knots as possible in a variety of situations.
For example, I should take photos with different types of rope (nylon, floss, ribbon etc.) and different backgrounds (shipyards, mountains, cluttered desk etc.).
I plan to contact knot enthusiasts for more images to expand this dataset, as a bigger dataset can increase the validity of the classification accuracy.
I aim to gather all data before Christmas on an ongoing basis, as this will leave plenty of time to focus on other details of the project next semester.

Next, we talked about further experimentation on the classifier.
John suggested that I flip the training and validation datasets (train on the 'wild' dataset and validate on my controlled dataset).
It would certainly be interesting to see what results this flip will bring.

We then spent the latter half of the meeting discussing the next steps for the network implementation and network visualisation.
John suggested that I should certainly add Binary Dropout layers to my network, even if it results in slight decreases of accuracy, as it has been shown to combat overfitting particularly with larger datasets.
Next, John mentioned that I should start laying the groundwork to make a multi-output neural network, where, along with my existing 5-node output that classifies knots, I have an extra node that classifies tension in the rope.
There are examples of how to do this on John's TSNE repo.
This extra classification could provide very exciting possibilities for future implementations of GANs, where I could start thinking of scenarios.
One possible scenario for a GAN could be that given an image of a loose knot, the GAN could produce a representation of that knot but with a set tension.
This is one particularly useful scenario for a GAN.

John also mentioned that I should use the tools on his TSNE repo to start visualising the network.
With visualisation, we can start to gauge (based on my network) what knots are similar, where they lie on the plane, and perhaps start predicting where knots should be positioned on the plane.
I also want to find a way where we can easily see what the network is learning at every layer, so we can gain insight into what the network is doing to learn the knot representations.
