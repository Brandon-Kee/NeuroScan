from flask import Flask, render_template, request, send_from_directory
from tensorflow.keras.models import load_model
from keras.preprocessing.image import load_img, img_to_array
import numpy as np
import os

app = Flask(__name__)

# Load trained model
model = load_model('model.keras')

# Class labels
class_labels = ['pituitary', 'notumor', 'glioma', 'meningioma']