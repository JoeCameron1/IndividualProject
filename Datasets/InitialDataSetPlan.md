# Plan for Initial Dataset

This initial dataset will include the following knots:

* The Overhand Knot
* The Fisherman's Knot
* The Reef Knot
* The Alpine Butterfly Knot
* The Bowline Knot

The images will contain only two types of climbing rope at most, and one constant background (a wooden surface). 
For the Fisherman's Knot, both types of climbing rope will be used to tie it, as it is a bend knot. 
Bend knots are used to join two lengths of rope together.
Although the reef knot is not classified as a bend knot (it is strictly classified as a binding knot), both types of rope will also be used to tie it.
For the other knots, only one type of rope will be used in each knot.

Every knot will be photographed in three various lighting conditions, in order to reduce overfitting to one specific method of lighting. 
These light conditions will be categorised as follows: 
* Diffuse lighting
* Direct source lighting from overhead
* Direct source lighting from the side

For every lighting condition, every knot will also be rotated in the z-axis every 90 degrees. 
This is to reduce overfitting to one specific 3d rotation. 

Furthermore, for every lighting condition and z-axis rotation, every knot will be photographed at different tensions.
This is to reduce overfitting to one specific knot tension.
These tensions will be categorised as follows:
* Very Loose 
* Loose
* Set

Many other variables will be factored later, by performing data augmentation via the ImageDataGenerator class in Keras.
The goal of data augmentation is to promote certain variables to become invariant in the classification process and to reduce overfitting.
The data augmented variables will be:
* Image Rotation in the 2D plane
* Image Brightness
* Image Contrast
* Image Orientation (Horizontal/Vertical Flip)