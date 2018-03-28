# IndividualProject - Joseph M. Cameron
## Using Machine Learning to Understand Knot Topology
This repository contains the code, log, meeting minutes and status reports for my individual dissertation project, which was undertaken during my 4th year at the University of Glasgow.

This project's aim is to classify knots based on their topology.

Knot classification is achieved by a convolutional neural network implemented in Keras.
The convolutional neural network training software is located within the python script knotClassifier.py located in the KnotClassifier folder.
Make sure to download and install the latest versions of all required pip packages including Keras (2.1.3), Tensorflow (1.3.0), sklearn, numpy, scipy, coremltools (0.8) and others to correctly run the training software.

Furthermore, an iOS application was developed to serve as an interface to utilise the trained Keras convolutional neural network to predict knots in real-time via an iPhone's camera.
The iOS application is called The Knot Classifier, and is located within the iOSApp folder as an Xcode project.
Also within this folder is the knotClassifier.mlmodel file, which is the converted Keras convolutional neural network that was converted by the convertModel.py script located within the KnotClassifier folder.
Simply drag the knotClassifier.mlmodel file into the Xcode project to use the model.
The iOS application has been implemented to run on an iPhone 6s Plus, and so the interface has been designed to match that phone's screen size.

Overall, this software provides the capability to classify ten knots, with the ten knots being:
* The Alpine Butterfly Knot
* The Bowline Knot
* The Clove Hitch
* The Figure-8 Knot
* The Figure-8 Loop
* The Fisherman's Knot
* The Flemish Bend
* The Overhand Knot
* The Reef Knot
* The Slip Knot

A controlled dataset containing images of these ten knots in differing conditions is available on Kaggle at https://www.kaggle.com/josephcameron/10knots.
This dataset is called 10Knots, and was used to train and validate the convolutional neural network implemented in Keras.

A demonstration video detailing the implementation can be found at https://www.youtube.com/watch?v=OvO8Q4mA0ac&t=411s.
