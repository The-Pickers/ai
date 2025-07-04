from flask import Flask, request, jsonify
import base64
import cv2
import numpy as np
from yolo.yolo_detector import detect_trash
from llm.mission_complete import generate_mission_summary
from llm.main_menu import generate_carbon_reduction_message

app = Flask(__name__)

@app.route('/main-message', methods=['POST'])
def carbon_message():
    data = request.json
    carbon_reduction = data.get('carbon_reduction')

    if carbon_reduction is None:
        return jsonify({"error": "carbon_reduction value is required"}), 400

    try:
        carbon_reduction = float(carbon_reduction)
    except ValueError:
        return jsonify({"error": "carbon_reduction must be a number"}), 400

    message = generate_carbon_reduction_message(carbon_reduction)
    return jsonify({"message": message})

@app.route('/analyze', methods=['POST'])
def analyze_image():
    try:
        data = request.get_json()
        base64_str = data.get('image_base64')

        if not base64_str:
            return jsonify({"error": "No image_base64 provided"}), 400        
        
        # YOLO 탐지 → trash_data 생성
        trash_data = detect_trash(base64_str)

        # LLM 메시지 생성 (json 형태로 나옴: message, total_carbon, points)
        summary = generate_mission_summary(trash_data)
    
        response_body = {
            "message": summary['message'],
            "total_carbon": summary['total_carbon'],
            "points": summary['points'],
            "detected_objects": dict(trash_data)
        }
        
        print(f"response_body: {response_body}")

        return jsonify(response_body)

    except Exception as e:
        print(e)
        return jsonify({"error": str(e)}), 500
    
@app.route('/test', methods=['GET'])
def test_api():
    return jsonify({"message": "hello world"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
