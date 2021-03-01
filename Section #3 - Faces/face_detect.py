#pylint:disable=no-member

import cv2 as cv

# NOTE: face detection uses a classifier, and opencv has a pretrained one

img = cv.imread('../Resources/Photos/group 1.jpg')
cv.imshow('Group of 5 people', img)

# The classifier looks at the edges to detect something is a face or not, so we dont need color
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray People', gray)

haar_cascade = cv.CascadeClassifier('haar_face.xml')

# coordinates of rectangles around faces
# minNeighbors lower => detect more faces, but also more noises
faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=1)

print(f'Number of faces found = {len(faces_rect)}')

for (x,y,w,h) in faces_rect:
    cv.rectangle(img, (x,y), (x+w,y+h), (0,255,0), thickness=2)

cv.imshow('Detected Faces', img)

cv.waitKey(0)