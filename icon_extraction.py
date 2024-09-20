import cv2
import numpy as np
import json
import os

# Load the image
image = cv2.imread('Equity Portfolio.png')

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply thresholding to segment out the icons
_, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

# Find contours in the thresholded image
contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Iterate through the contours and extract the icons
icons = []
for contour in contours:
    x, y, w, h = cv2.boundingRect(contour)
    aspect_ratio = float(w)/h
    if aspect_ratio > 0.5 and aspect_ratio < 2.0:  # Filter out non-rectangular shapes
        icon = image[y:y+h, x:x+w]
        icon_path = f'icon_{len(icons)+1}.png'
        cv2.imwrite(icon_path, icon)
        icons.append({
            'image_path': icon_path,
            'bounds': [x, y, w, h]
        })

# Save the extracted icons to a JSON file
with open('icons.json', 'w') as f:
    json.dump(icons, f, indent=4)

print('Icons extracted and saved to icons.json')
