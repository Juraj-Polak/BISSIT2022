# Imports
import os
import cv2
import face_recognition
import numpy as np
from datetime import datetime

# Face detection
# Classifier
casc_path = os.path.dirname(cv2.__file__)+"/data/haarcascade_frontalface_default.xml"
face_cascade = cv2.CascadeClassifier(casc_path)

# Prepare images for encoding
images = []
encoded_known = []
names = []
path = './train'

for file in os.listdir(path):
    current_image = cv2.imread(f'{path}/{file}')
    images.append(current_image)
    names.append(os.path.splitext(file)[0])

# Encode known faces
encodings = []

def encode_faces(image_list):
    for image in image_list:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(image)[0]
        encodings.append(encode)
    return encodings


# Take attendance
def take_attendance(name):
    name_list = []
    with open('attendance.csv', 'r+') as file:
        data = file.readlines()
        for line in data:
            text = line.split(',')
            name_list.append(text[0])
        
        if name not in name_list:
            time = datetime.now()
            time = time.strftime('%H:%M:%S')
            file.writelines(f'\n[{name},{time}')


# From video feed
def video_detection():
    encoded_known = encode_faces(images)
    video = cv2.VideoCapture(0)

    while True:
        # Frame by frame capture
        _, frames = video.read()

        # Convertion to RGB
        frames = cv2.cvtColor(frames, cv2.COLOR_BGR2RGB)
        frames_small = cv2.resize(frames, (0,0), None, 0.25, 0.25)

        # Encode faces from video
        faces = face_recognition.face_locations(frames_small)
        encoded_unknown = face_recognition.face_encodings(frames_small, faces)

        # Compare found faces with known faces
        for encode_face, face_location in zip(encoded_unknown, faces):
            matches = face_recognition.compare_faces(encoded_known, encode_face)
            face_distance = face_recognition.face_distance(encoded_known, encode_face)
            match_index = np.argmin(face_distance)
            
            # Higlight faces
            if matches[match_index]:
                name = names[match_index]
                take_attendance(name)
            else:
                name = 'unknown'

            y1, x2, y2, x1 = face_location
            x1, x2, y1, y2 = x1*4, x2*4, y1*4, y2*4
            cv2.rectangle(frames, (x1, y1), (x2, y2), (0, 255, 0), 2)
            
            # Show name
            cv2.rectangle(frames, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
            cv2.putText(frames, name, (x1 + 5, y2 - 5), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
 
        # Dispaly video
        cv2.imshow('Video', frames)

        # Exit condition
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    video.release()
    cv2.destroyAllWindows()


# From photo
def photo_detection():
    KNOWN_FACES_DIR = './test'

    # Variables
    known_faces = []

    # Process files
    for file in os.listdir(f'{KNOWN_FACES_DIR}'):
        known_faces.append(f'{KNOWN_FACES_DIR}/{file}')


    for _ in range(len(known_faces)):
        image = cv2.imread(known_faces[_])
        image = cv2.resize(image, (0,0), None, 0.25, 0.25)

        grey = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        faces = face_cascade.detectMultiScale(
            grey,
            scaleFactor=1.3,
            minNeighbors=3,
            minSize=(30,30),
            flags=cv2.CASCADE_SCALE_IMAGE
        )

        # Highlight faces
        for (x, y, w, h) in faces:
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Display photo
        cv2.imshow('Photo', image)
        
        # Exit condition
        cv2.waitKey(0)

    cv2.destroyAllWindows