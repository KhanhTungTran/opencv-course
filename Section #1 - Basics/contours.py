#pylint:disable=no-member

import cv2 as cv
import numpy as np

# NOTE: Contour: boundary of object (same as edges in mathematical view)
# NOTE: Should try canny then find contours than threshold and find contours

img = cv.imread('../Resources/Photos/cats.jpg')
cv.imshow('Cats', img)

blank = np.zeros(img.shape, dtype='uint8')
cv.imshow('Blank', blank)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

blur = cv.GaussianBlur(gray, (5,5), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

canny = cv.Canny(blur, 125, 175)
cv.imshow('Canny Edges', canny)

# cv.threshold to binarize form of image
# ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
# cv.imshow('Thresh', thresh)

# CHAIN_APPROX_SIMPLE VS. CHAIN_APPROX_NONE: ví dụ có một line, none sẽ trả về tất cả các điểm trên line, trong khi simple chỉ trả về điểm bắt đầu và điểm kết thúc => simple compress points
contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)    # look at the edges of image, find the hierachies of image
print(f'{len(contours)} contour(s) found!')

cv.drawContours(blank, contours, -1, (0,0,255), 1)
cv.imshow('Contours Drawn', blank)

cv.waitKey(0)