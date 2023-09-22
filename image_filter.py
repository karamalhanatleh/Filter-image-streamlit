# -*- coding: utf-8 -*-
"""
Created on Fri Sep 22 12:18:58 2023

@author: Karam Alhanatlh
"""

import streamlit as st
from PIL import Image
import numpy as np

# Capture an image from the camera
pic = st.camera_input("Take a pic")

if pic:
    # Open the captured image using PIL
    img = Image.open(pic)
    
    # Convert the image to a NumPy array and apply some processing (e.g., inverting colors)
    arr_img = np.array(img)
    inverted_img = 255 - arr_img  # Invert the colors
    
    # Display the processed image without a white border
    st.image(inverted_img, use_column_width=True)

    st.image(150 - arr_img, use_column_width=True)



