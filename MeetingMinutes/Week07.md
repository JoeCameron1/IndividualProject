# Week 7 Meeting Minutes - 09/11/2017

Over the past week, I wrote a python script that could resize images within a dataset, thus allowing full transparency in the process.
I started the meeting by explaining to John why I decided to write the script in python instead of bash.
I explained that while I was writing my bash script, it became very clear that each OS environment would need their own bash tailored bash script to achieve the image resizing.
Therefore, I wrote the script in python instead, using Pillow to perform image resizing.
This allows for portability over many OS environments, users simply need to pip install PIL.
John agreed with this decision, stating that I had shown good awareness.
Next, I explained to John that after thorough testing of the script, I could upload the script and my dataset the following day (Friday).

John then asked how planned to resize the images within the script.
I stated that I would ask users for a percentage of original photo size.
John then suggested that I ask for specific pixel values instead, as this counteracts the bias of specific camera models.
I immediately agreed to this, and updated my python script accordingly.

Next, we discussed my plans for building a Keras model, as John pointed out that I am very close to being able to train my dataset and collect classification results.
John pointed out that I should think carefully about the Input and Output values of the network.
I proposed that the input should be pixel values, and the output should be a 5 dimensional vector, where the index of the highest number corresponds to a knot that has been classified.
John said that this is sensible, but also pointed out that I should perhaps turn all my images to grayscale initially and then worry about RGB values later.

We concluded that over the next week, I should aim to create a basic Keras model (closely based on the model used for the MNIST tutorial), and train this model using my initial dataset and then evalute this model.
