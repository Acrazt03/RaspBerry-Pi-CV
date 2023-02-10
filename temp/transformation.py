import cv2 as cv
import numpy as np

img = cv.imread('photos/d0e245d0-70fa-4daf-88a1-08c7640cda9b.jpeg')
cv.imshow('Jariel', img)

# Translation
def translate(img, x, y):
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img , transMat, dimensions)

translated = translate(img, 100,100)
cv.imshow('translated',translated)

# Rotation
def rotate(img, angle, pivotPoint=None):
    (height, width) = img.shape[:2]

    if pivotPoint is None:
        pivotPoint = (height//2, width//2)
    
    rotMat = cv.getRotationMatrix2D(pivotPoint, angle, 1.0)
    dimensions = (width, height)

    return cv.warpAffine(img, rotMat, dimensions)

rotated = rotate(img, 45)
cv.imshow('Rotated Jari', rotated)

cv.waitKey(0)