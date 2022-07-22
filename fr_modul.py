# Imports
import os
import cv2


# Face detection
# Classifier
casc_path = os.path.dirname(cv2.__file__)+"/data/haarcascade_frontalface_default.xml"
face_cascade = cv2.CascadeClassifier(casc_path)

# From video feed
def video_detection():
    video = cv2.VideoCapture(0)

    while True:
        # Frame by frame capture
        ret, frames = video.read()

        # Convertion to greyscale
        grey = cv2.cvtColor(frames, cv2.COLOR_BGR2GRAY)

        faces = face_cascade.detectMultiScale(
            grey,
            scaleFactor=1.1,
            minNeighbors=3,
            minSize=(30,30),
            flags=cv2.CASCADE_SCALE_IMAGE
        )

        # Highlight faces
        for (x, y, w, h) in faces:
            cv2.rectangle(frames, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Dispaly video
        cv2.imshow('Video', frames)

        # Exit condition
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    video.release()
    cv2.destroyAllWindows()

# From photo
def photo_detection():
    KNOWN_FACES_DIR = 'knownFaces'

    # Variables
    known_faces = []
    known_names = []

    # Process files
    for directory in os.listdir(KNOWN_FACES_DIR):
        for file in os.listdir(f'{KNOWN_FACES_DIR}/{directory}'):
            known_faces.append(f'{KNOWN_FACES_DIR}/{directory}/{file}')
            known_names.append(directory)


    for _ in range(len(known_faces)):
        image = cv2.imread(known_faces[_])

        grey = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        faces = face_cascade.detectMultiScale(
            grey,
            scaleFactor=1.1,
            minNeighbors=5,
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