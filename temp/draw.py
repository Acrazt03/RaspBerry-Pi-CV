import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3), dtype='uint8')

cv.imshow('Blank Img', blank)

blank[:] = 0,0,255
cv.imshow('Green Img', blank)

cv.rectangle(blank, (100,100),(200,200), (0,255,0), thickness=cv.FILLED)

cv.imshow('rectangle Img', blank)

cv.waitKey(0)