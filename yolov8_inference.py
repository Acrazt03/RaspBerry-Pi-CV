from ultralytics import YOLO
from ultralytics.yolo.v8.detect.predict import DetectionPredictor

import cv2

model = YOLO('yolov8s-seg-filtro-mangera-v1.pt')

results = model.predict(source="0",conf=0.8, show=True)

print(results)
