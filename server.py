#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 15 17:10:36 2022

@author: sree
"""

# Import libraries
import numpy as np
from flask import Flask, request, jsonify
import pickle
app = Flask(__name__)
# Load the model
model = pickle.load(open('model.pkl','rb'))
@app.route('/api',methods=['POST'])
def predict():
    # Get the data from the POST request.
    data = request.get_json(force=True)
    # Make prediction using model loaded from disk as per the data.
    prediction = model.predict([[np.array(data['exp'])]])
    # Take the first value of prediction
    output = prediction[0]
    return jsonify(output)

@app.route('/hi', methods=['GET'])
def hi():
    return "Hello Word"
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)