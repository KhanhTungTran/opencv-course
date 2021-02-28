#pylint:disable=no-member

import cv2 as cv

#NOTE: blurring to smooth or reduce noise in the image

img = cv.imread('../Resources/Photos/cats.jpg')
cv.imshow('Cats', img)

# Averaging: define a kernel pixel -> middle pixel is average of all surrouding pixels
average = cv.blur(img, (3,3))
cv.imshow('Average Blur', average)

# Gaussian Blur: add weight to average
# usually less blur than average
gauss = cv.GaussianBlur(img, (3,3), 0)
cv.imshow('Gaussian Blur', gauss)

# Median Blur: instead of average, find the median of the surrounding image
median = cv.medianBlur(img, 3)
cv.imshow('Median Blur', median)

# Bilateral: the most effective by looking at whether the pixel is edge of the image
# sigmaSpace: whether pixel from faraway can influence the computation of current pixel
bilateral = cv.bilateralFilter(img, 10, 35, 25)
cv.imshow('Bilateral', bilateral)

cv.waitKey(0)