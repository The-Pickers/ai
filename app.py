from flask import Flask, request, jsonify
import base64
import cv2
import numpy as np
from yolo.yolo_detector import detect_trash
from llm.mission_complete import generate_mission_summary

app = Flask(__name__)

@app.route('/analyze', methods=['POST'])
def analyze_image():
    try:
        data = request.get_json()
        base64_str = data.get('image_base64')

        if not base64_str:
            return jsonify({"error": "No image_base64 provided"}), 400

        # base64 → 이미지 변환
        img_bytes = base64.b64decode(base64_str)
        npimg = np.frombuffer(img_bytes, np.uint8)
        img = cv2.imdecode(npimg, cv2.IMREAD_COLOR)

        # YOLO 탐지 → trash_data 생성
        trash_data = detect_trash(img)

        # LLM 메시지 생성
        message = generate_mission_summary(trash_data)

        return jsonify({"message": message})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
