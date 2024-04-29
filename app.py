from flask import Flask, jsonify, request
from joblib import load 

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()

    model = load("predict.joblib")
    prediction = model.predict(data['input'])

    return jsonify({'prediction': prediction.tolist()})

if __name__ == '__main__':
    app.run(debug=True)