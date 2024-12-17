import joblib
import numpy as np
import time
import json
import sys
import random
from flask import Flask, jsonify

app = Flask(__name__)


def load_config():
    with open('../config.json', 'r') as file:
        config = json.load(file)
    return config

start_time = time.time()
config = load_config()
video_length = config.get("video_length", 10)  # Default to 10 if not found
complexity_score = config.get("complexity_score", 3.5)  # Default to 3.5 if not found
model_path = config.get("model_path")
model = joblib.load(model_path)


def get_predicted_time(video_length, complexity_score):
    X = np.array([[video_length, complexity_score]])
    predicted_time = model.predict(X)[0]  
    return predicted_time

@app.route('/status', methods=['GET'])
def get_status():
    global start_time
    elapsed_time = time.time() - start_time 
    predicted_time = get_predicted_time(video_length, complexity_score)
    print('Predicted Time:', predicted_time)
    if elapsed_time < predicted_time:
        return jsonify({"result": "pending", "predicted_time": predicted_time})
    else:
        if random.random() < 0.9:
            return jsonify({"result": "completed", "predicted_time": predicted_time})
            
        else:
            return jsonify({"result": "error", "predicted_time": predicted_time})
if __name__ == '__main__':
    app.run(debug=True)
