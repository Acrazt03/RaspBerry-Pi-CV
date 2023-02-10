import cv2 as cv

img = cv.imread('photos/d4fb4b98-aa04-4d20-a7b6-308943ffe4be.jpeg')

cv.imshow('Jariel', img)

cv.waitKey(0)

capture = cv.VideoCapture('videos/2022-03-23 19-40-36.mkv') #it also takes an idex port for connected webcams

while True:
    isTrue, frame = capture.read()
    cv.imshow('Video', frame)

    if cv.waitKey(20) & 0xFF==ord('d'): #This reads the d key
        break


capture.release()
cv.destroyAllWindows()
