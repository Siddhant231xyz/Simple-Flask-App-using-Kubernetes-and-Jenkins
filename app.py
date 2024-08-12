from flask import Flask, request, render_template
import tensorflow as tf
import numpy as np

app = Flask(__name__)

# Load a pre-trained TensorFlow model (e.g., a simple model for demonstration)
model = tf.keras.models.load_model('simple_model.h5')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.form['input_data']
    data = np.array([[float(x) for x in data.split(',')]])
    prediction = model.predict(data)
    return f"Prediction: {prediction[0][0]}"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
