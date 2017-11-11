# Week 3 Meeting Minutes

John and I started the meeting with discussion over the progress of week 2. 
As I mentioned in my status report, I told John that the installation of Keras and Tensorflow had gone smoothly.
Hence, my experience completing the MNIST tutorial was also reasonably smooth and gave me insight to the workflow within Keras.

We then started discussing the dataset. 
I relayed to John that I had found some images of knots on ImageNet, but that I also must make my own dataset for the purposes of this project.
John agreed on this decision, and we then started to discuss my progress on data augmentation.
I told John that I found a tutorial on data augmentation by Francois Chollet on the Keras Blog, and we both stated that the completion of this tutorial would be one of my goals for the next week.
John then proposed that the next step is to think about what variables I want to include/contrast within my dataset.
John also mentioned that there are dertain variables that must be invariant to the classification process, and this is where data augmentation becomes very useful.
I suggested that the rotation of the knot should be invariant, as knots should be classified no matter what the rotation is.
John then suggested that I think about the tension of the rope also, as it would be interesting to classify knots under differing tensions.

We concluded that the goals for week 3 are:
* identifying variables to include in my dataset
* completing the data augmentation tutorial on the keras blog
* setting up a git repository
