import base64
from ultralytics import YOLO
from collections import Counter
import cv2
import numpy as np

model_yolo = YOLO('train_log/weights/best.pt')

def detect_trash(base64_str):
    # base64 → bytes
    file_bytes = base64.b64decode(base64_str)
    
    # bytes → NumPy array
    npimg = np.frombuffer(file_bytes, np.uint8)
    img = cv2.imdecode(npimg, cv2.IMREAD_COLOR)
    
    # YOLO 추론
    results = model_yolo(img, verbose=False)[0]
    class_ids = results.boxes.cls.tolist()
    class_names = [results.names[int(cls_id)] for cls_id in class_ids]
    counts = Counter(class_names)
    
    return counts
