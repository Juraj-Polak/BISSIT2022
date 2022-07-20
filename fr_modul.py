# Imports
import os
import cv2

# Constants
KNOWN_FACES_DIR = 'knownFaces'
UNKNOWN_FACES_DIR = 'unknownFaces'
TOLERANCE = 0.7
FRAME_THICKNESS = 3
FONT_THICKNESS = 2
MODEL = 'cnn'

# Variables
known_faces = []
known_names = []

for directory in os.listdir(KNOWN_FACES_DIR):
    for file in os.listdir(f'{KNOWN_FACES_DIR}/{directory}'):
        known_faces.append(f'{KNOWN_FACES_DIR}/{directory}/{file}')
        known_names.append(directory)

# for _ in range(len(known_faces)):
#     cv2.imshow('xicht', cv2.imread(known_faces[_]))
#     cv2.waitKey(0)

# cv2.destroyAllWindows 