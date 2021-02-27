#pylint:disable=no-member

import cv2 as cv

img = cv.imread('../Resources/Photos/park.jpg')
cv.imshow('Park', img)

# Converting to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# Blur
blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT) # Increase Blur => increase kernel size
cv.imshow('Blur', blur)

# Edge Cascade
canny = cv.Canny(blur, 125, 175) # Passing blur help detect edge much better
cv.imshow('Canny Edges', canny)

# Dilating the image, dilate: giãn ra, tăng độ thick
dilated = cv.dilate(canny, (7,7), iterations=3) # Increase thickness => increase kernel size
cv.imshow('Dilated', dilated)

# Eroding để đảo ngược dilate
eroded = cv.erode(dilated, (7,7), iterations=3)
cv.imshow('Eroded', eroded)

# Resize
resized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
cv.imshow('Resized', resized)

# Cropping
cropped = img[50:200, 200:400]
cv.imshow('Cropped', cropped)

cv.waitKey(0)