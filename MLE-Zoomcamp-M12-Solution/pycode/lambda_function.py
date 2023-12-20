#!/usr/bin/env python
# coding: utf-8

import tflite_runtime.interpreter as tflite
from keras_image_helper import create_preprocessor

interpreter = tflite.Interpreter(model_path='car_tfmodel_v214.tflite')
interpreter.allocate_tensors()
input_index  = interpreter.get_input_details()[0]['index']
output_index = interpreter.get_output_details()[0]['index']

classes = [
    'crack',
    'scratch',
    'tire_flat',
    'dent',
    'glass_shatter',
    'lamp_broken'
]

preprocessor = create_preprocessor('xception', target_size=(600, 800))

def predict(url):
    X = preprocessor.from_url(url)

    interpreter.set_tensor(input_index, X)
    interpreter.invoke()    
    preds = interpreter.get_tensor(output_index)
    
    float_predictions = preds[0].tolist()

    return dict(zip(classes, float_predictions))


def lambda_handler(event, context):
    url    = event['url']
    result = predict(url)
    return result