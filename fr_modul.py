# Imports
import os
import cv2


# Face detection
# Classifier
casc_path = os.path.dirname(cv2.__file__)+"/data/haarcascade_frontalface_default.xml"
face_cascade = cv2.CascadeClassifier(casc_path)

# Video feed
video = cv2.VideoCapture(0)

while True:
    # Frame by frame capture
    ret, frames = video.read()

    # Convertion to greyscale
    grey = cv2.cvtColor(frames, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(
        grey,
        scaleFactor=1.1,
        minNeighbors=5,
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