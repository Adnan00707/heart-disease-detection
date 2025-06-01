from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load the saved model
model = pickle.load(open('heart_model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')  # Make sure index.html exists in 'templates/' folder

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = [float(x) for x in request.form.values()]
        input_data = np.array(data).reshape(1, -1)
        prediction = model.predict(input_data)

        if prediction[0] == 0:
            result = "✅ The person has a healthy heart."
        else:
            result = "⚠️ The person may have heart disease."

        return render_template('index.html', prediction_text=result)
    except Exception as e:
        return render_template('index.html', prediction_text=f"Error: {e}")

if __name__ == "__main__":
    app.run(debug=True)
