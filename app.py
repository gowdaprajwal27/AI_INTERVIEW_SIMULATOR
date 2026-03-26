from flask import Flask, request, jsonify
from flask_cors import CORS
from model.evaluator import evaluate_answer
import os

app = Flask(__name__)
CORS(app)

@app.route('/evaluate', methods=['POST'])
def evaluate():
    data = request.json
    user_answer = data['answer']
    expected_answer = data['expected']

    score, feedback = evaluate_answer(user_answer, expected_answer)

    return jsonify({
        "score": score,
        "feedback": feedback
    })

@app.route('/')
def home():
    return "API is running ✅"

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))  # 🔥 IMPORTANT
    app.run(host="0.0.0.0", port=port)