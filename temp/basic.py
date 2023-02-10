import cv2 as cv

img = cv.imread('photos/d0e245d0-70fa-4daf-88a1-08c7640cda9b.jpeg')
#cv.imshow('Jariel', img)

# Convert to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#cv.imshow('Jariel Gray', gray)

# Blur
blur = cv.GaussianBlur(img, (9,9), cv.BORDER_DEFAULT)
#cv.imshow('Blurred Jariel', blur)

# Edge Cascade
canny = cv.Canny(img, 125, 175)
#cv.imshow('Canny Jari', canny)

#Dilating the image
dilated = cv.dilate(canny, (3,3), iterations=3)
#cv.imshow('Dilated Cannyyy Jari', dilated)

# Eroding
eroded = cv.erode(dilated, (3,3), iterations=3)
#cv.imshow('Eroded jari', eroded)

# Resize
resized = cv.resize(img, (500,500))
#cv.imshow('Risized jari', resized)

# Cropping
cropped = img[50:200, 200:400]
cv.imshow('Cropped Jari', cropped)

cv.waitKey(0)