from flask import Flask, render_template, request
import cv2
import numpy as np
from PIL import Image
import json
import urllib.request

def match_island(input_image_path):
    # Convert the input image to a numpy array
    with open(input_image_path, 'rb') as input_image:
        input_array = np.asarray(bytearray(input_image.read()), dtype='uint8')
        input_array = cv2.imdecode(input_array, cv2.IMREAD_COLOR)

    if input_array is None:
        raise ValueError('Input image could not be loaded or decoded.')

    # Iterate over the loaded island images and find the best match
    best_match = None
    best_match_score = float('inf')
    for island_name, island_image in island_images.items():
        if island_image is None:
            raise ValueError('Island image "{}" could not be loaded or decoded.'.format(island_name))

        # Compare the input image to the current island image using mean squared error
        score = cv2.matchTemplate(island_image, input_array, cv2.TM_SQDIFF_NORMED)
        min_score, _, _, _ = cv2.minMaxLoc(score)

        # Update the best match if the current island image has a lower score (i.e., closer match)
        if min_score < best_match_score:
            best_match_score = min_score
            best_match = islands[island_name]

    if best_match is None:
        raise ValueError('No matching island image found.')

    print(best_match)
    return best_match


# Create a dictionary to store the coordinates of each island
islands = {}

# Load the islands.json file into memory
with open('islands.json') as f:
    islands = json.load(f)

# Iterate over the dictionary and load the images into memory from island_images folder
island_images = {}
for island in islands:
    url = islands[island]['Image']
    with open(url, 'rb') as url_response:
        image = np.asarray(bytearray(url_response.read()), dtype='uint8')
        image = cv2.imdecode(image, cv2.IMREAD_COLOR)
        island_images[island] = image

best_match = match_island('test1.png')
