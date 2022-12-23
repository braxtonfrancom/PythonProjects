import cv2

# Load the cascade
face_cascade = cv2.CascadeClassifier("faceDetectionAlgorithm.xml.html")

# To capture video from webcam.
capture = cv2.VideoCapture(0)
   #If i wanted to use a video file as an input, use --> capture = cv2.VideoCapture('filename.mp4')

while True:
    # Read the frame
    _, img = capture.read()

    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Detect the faces
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    # Draw the rectangle around each face
    for (x, y, h, w) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 8)

    # Display
    cv2.imshow('img', img)
    # Stop if escape key is pressed
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

capture.release()
