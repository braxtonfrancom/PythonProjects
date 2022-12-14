import cv2

#Loading the cascade
face_cascade = cv2.CascadeClassifier('faceDetectionAlgorithm.xml.html')
#Read the input image
img = cv2.imread('weddingpic.jpg')
#Convert into grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#Detect faces
faces = face_cascade.detectMultiScale(gray, 1.1, 4)

#Draw rectangle around the faces
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 8)
    #cv2.circle(img, (x + 400, y + 350), 500, cv2.COLOR_BAYER_GRBG2RGBA, 8)

cv2.imshow('img', img)
cv2.waitKey()