import cv2 as cv

def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

def changeRes(width, height): #only works for live video
    capture.set(3,width)
    capture.set(4, height) #the numbers represent properties of the video

capture = cv.VideoCapture('videos/2022-03-23 19-40-36.mkv') #it also takes an idex port for connected webcams

while True:
    isTrue, frame = capture.read()

    frame_resized = rescaleFrame(frame)

    cv.imshow('Video', frame_resized)

    if cv.waitKey(20) & 0xFF==ord('d'): #This reads the d key
        break


capture.release()
cv.destroyAllWindows()