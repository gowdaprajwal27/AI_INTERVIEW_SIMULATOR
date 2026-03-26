from flask import Flask, request, jsonify
from flask_cors import CORS 
from model.evaluator import evaluate_answer

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

if __name__ == '__main__':
    app.run(debug=True)