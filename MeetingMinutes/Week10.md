# Week 10 Meeting Minutes - 30/11/2017

The meeting started with a review of the work I had done over the past week.
John was happy to hear that I had obtained a 90% accuracy when flipping the training and validation datasets, as this shows that the classifier is actually working.
He was also happy to see that I had obtained more data that I can add to my datasets, and had added dropout layers to my CNN model.

Next, John suggested that I should certainly focus on expanding my dataset over the next two weeks, and I certainly agree.
The more data I obtain, the better.
Flickr could be a good source of images for this.
Another way I could expand my dataset is by using Blender to create 3D renderings of knots.
This could also provide useful insights to the behaviour of the classifier, will the accuracy if I train on synthesised data and validate on real data etc.
John also suggested that it would be good to think about two-stage training, where I train first on synthesised data, and then take those weights and train again on real data, and then validate on a small number of real data.

John also suggested that I should consider gathering data to be able to classfify 10 knots.
I agree with this, and furthermore, it would be interesting to see whether I can classify a single fisherman's knot from a double fisherman's knot and vice versa.
