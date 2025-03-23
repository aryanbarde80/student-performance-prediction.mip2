from flask import Flask, request, jsonify
import pickle
import numpy as np

app = Flask(__name__)

# Model Load kar rahe hain
model = pickle.load(open('student_performance_model.pkl', 'rb'))

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    features = np.array([data['features']])  # Example: [2,1,0,1,20,...]
    prediction = model.predict(features)
    return jsonify({'prediction': int(prediction[0])})

if __name__ == '__main__':
    app.run(debug=True)
