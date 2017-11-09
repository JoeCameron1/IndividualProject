# Week 6 Status Report

One of the primary goals for this week was to develop a script that could resize images within my dataset for use within Keras. 
I managed to write a python script (utilising Pillow) that can resize images within a directory. 
Initially, I thought about writing a script for this in bash. 
However, it soon became clear that writing a script that could execute within multiple operating environments is quite challenging. 
For example, on macOS, it is possible to resize images using a tool called ‘sips’. 
Although, ‘sips' is only designed to be executed on macOS; therefore a different script would be required for Linux etc. 
I want to create software that will run in every popular OS environment; hence a python script became the most obvious way for me to achieve this portability. 
I use Pillow (imported as PIL) to accomplish the image resizing. 
I will add this script to my repository once I have time to thoroughly test it over various scenarios.

This week, I also managed to gather more data to add to my initial dataset. 
Specifically, data was gathered from the Overhand Knot and the Alpine Butterfly Knot, both with non-reflective backgrounds. 
More data will be collected (on the other five knots) with a non-reflective background over the next week. 

Finally, over the last week, I have identified more knots to add to my dataset. 
Next, I plan to gather data on the Figure-8 Loop (popularly used in climbing), the Clove Hitch knot, the Savoy Knot (also known as a Figure-8 knot which is different to a Figure-8 loop), the Flemish Bend Knot and the Slip Knot. 
Before gathering data on these knots, I plan to train a neural network model with my initial dataset of five knots.
