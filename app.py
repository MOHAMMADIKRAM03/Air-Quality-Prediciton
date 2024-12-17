from flask import Flask, render_template, request
import pickle
import numpy as np
import os

# Load the Random Forest Classifier model
filename = 'random_forest_regression_model.pkl'
classifier = pickle.load(open(filename, 'rb'))

# Initialize the Flask app, specifying the template folder as the root directory
app = Flask(__name__, template_folder=os.getcwd())  # Points to the root directory

# Home route to render the index page
@app.route('/')
def home():
    return render_template('index.html')

# Predict route to handle form submission and prediction
@app.route('/predict', methods=['POST'])
def predict():
    try:
        if request.method == 'POST':
            # Retrieve and convert input data from form
            T = float(request.form['T'])
            TM = float(request.form['TM'])
            Tm = float(request.form['Tm'])
            SLP = float(request.form['SLP'])
            H = float(request.form['H'])
            VV = float(request.form['VV'])
            V = float(request.form['V'])
            VM = float(request.form['VM'])

            # Create input array for prediction
            data = np.array([[T, TM, Tm, SLP, H, VV, V, VM]])

            # Perform prediction using the loaded model
            my_prediction = classifier.predict(data)[0]  # Extracting first element of the prediction result

            # Return result page with prediction
            return render_template('result.html', prediction=round(my_prediction, 2))
    except Exception as e:
        # In case of an error, return an error page with the message
        return render_template('error.html', error_message=str(e))

if __name__ == '__main__':
    app.run(debug=True)
