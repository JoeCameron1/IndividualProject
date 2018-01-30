# convertModel.py
# Author = Joseph M. Cameron
# This script converts a loaded Keras model into a CoreML model
# The CoreML model is then saved with the '.mlmodel' extension for use in iOS app development

# Script Usage: python convertModel.py
# For example: When this script is in the same directory as the Keras model 'first_try.h5',
# simply enter: python convertModel.py

# -----------------------------------------------------------

# IMPORT STATEMENTS

from keras.models import load_model
import coremltools

# -----------------------------------------------------------

# MODEL CONVERSION

model = load_model('first_try.h5')
classes = ['Alpine Butterfly Knot','Bowline Knot', 'Clove Hitch', 'Figure-8 Knot', 'Figure-8 Loop', 'Fisherman Knot', 'Flemish Bend', 'Overhand Knot', 'Reef Knot', 'Slip Knot']

coreml_model = coremltools.converters.keras.convert(model,
                                                    input_names=['image'],
                                                    image_input_names='image',
                                                    class_labels=classes,
                                                    image_scale=1/255.)

# -----------------------------------------------------------

# ADD COREML MODEL INFORMATION

coreml_model.author = 'Joseph Cameron'
coreml_model.license = 'MIT'
coreml_model.short_description = 'This model classifies knots.'
coreml_model.input_description['image'] = 'A 150x150 pixel image.'
coreml_model.output_description['output1'] = 'A one-hot MultiArray where the array index with the largest float value between 0 and 1 is the recognised knot.'

# -----------------------------------------------------------

# SAVE THE COREML MODEL

coreml_model.save('knotClassifier.mlmodel')
