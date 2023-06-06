from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load the trained model
model = pickle.load(open("D:\\My Programming\\tox21trainingdata.sdf\\xgboost3_model.pkl", 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    features = [float(x) for x in request.form.values()]
    input_data = np.array(features).reshape(1, -1)
    toxicity_score = model.predict(input_data)[0]
    return render_template('index.html', prediction=toxicity_score)

if __name__ == '__main__':
    app.run(debug=True)
