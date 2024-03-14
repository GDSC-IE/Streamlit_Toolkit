import tensorflow as tf
from PIL import Image
import numpy as np
import streamlit as st
from tensorflow.keras.applications import ResNet50
from tensorflow.keras.applications import VGG16
from tensorflow.keras.applications import Xception
from tensorflow.keras.applications import DenseNet121
from tensorflow.keras.applications import EfficientNetB0
from tensorflow.keras.applications import NASNetMobile

st.title("Image recognition from camera input")

# Here are many models, try uncommenting them 
# and seeing how they respond in the website
model = NASNetMobile(weights='imagenet')
# model = EfficientNetB0(weights='imagenet')
# model = DenseNet121(weights='imagenet')
# model = Xception(weights='imagenet')
# model = VGG16(weights='imagenet')
# model = ResNet50(weights='imagenet')

image = st.camera_input("")

if image is not None:
    st.image(image)

# Defnining function to predict the image when it detects one
def predict(image):
    # Resize image to 224x224 pixels as expected by MobileNetV2
    img = image.resize((224, 224))
    img_array = np.array(img).astype('float32') / 255.0
    img_array = np.expand_dims(img_array, axis=0)  # Model expects a batch of images

    # Make prediction
    predictions = model.predict(img_array)
    # Decode predictions
    decoded_predictions = tf.keras.applications.mobilenet_v2.decode_predictions(predictions, top=1)[0]
    return decoded_predictions[0][1]  # Return the label of the top prediction

# Calling the function if an image is taken.
if image is not None:
    with Image.open(image) as img:
        label = predict(img)
        st.header(f"this is {label}", anchor=None, help=None, divider=True)
