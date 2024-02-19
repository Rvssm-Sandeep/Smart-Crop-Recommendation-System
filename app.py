from flask import Flask, render_template, request
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import os
import joblib

app = Flask(__name__)

# Load the crop recommendation model
model_path = 'mymodel.pkl'
model_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),'mymodel.pkl')
# load the pickled model
model = joblib.load(model_path)

data = pd.read_csv('Dataset.csv')

# features = ['State_Name', 'Crop_Type', 'N', 'P', 'K', 'pH', 'rainfall', 'temperature', 'Area_in_hectares','Production_in_tons', 'Yield_ton_per_hec']

# Render home page
@app.route('/')
def home():
    return render_template('main.html')

@app.route('/predict', methods=['POST'])
def predict():
    sn =int (request.form.get("State_Name"))
    ct =int(request.form.get("Crop_Type"))
    n = int(request.form['nitrogen'])
    p = int(request.form['phosphorous'])
    k = int(request.form['potassium'])
    ph = float(request.form['pH'])
    rainfall = float(request.form['rainfall'])
    temperature = float(request.form['temperature'])
    area = int(request.form['area'])
    prod = int(request.form['prod'])
    yiel = float(request.form['yiel'])
    # Create a DataFrame with the input data
    input_data = ([[sn, ct, n,p,k, ph, rainfall, temperature, area, prod, yiel]])
    print(input_data)
    # Make predictions
    prediction = model.predict(input_data)[0]
    print(prediction)
    label_mapping = {'apple': 0, 'arecanut': 1, 'ashgourd': 2, 'banana': 3, 'barley': 4, 'beetroot': 5, 'bittergourd': 6,
                 'blackgram': 7, 'blackpepper': 8, 'bottlegourd': 9, 'brinjal': 10, 'cabbage': 11, 'cardamom': 12,
                 'carrot': 13, 'cashewnuts': 14, 'cauliflower': 15, 'coffee': 16, 'coriander': 17, 'cotton': 18,
                 'cucumber': 19, 'drumstick': 20, 'garlic': 21, 'ginger': 22, 'grapes': 23, 'horsegram': 24,
                 'jackfruit': 25, 'jowar': 26, 'jute': 27, 'ladyfinger': 28, 'maize': 29, 'mango': 30, 'moong': 31,
                 'onion': 32, 'orange': 33, 'papaya': 34, 'pineapple': 35, 'pomegranate': 36, 'potato': 37,
                 'pumpkin': 38, 'radish': 39, 'ragi': 40, 'rapeseed': 41, 'rice': 42, 'ridgegourd': 43, 'sesamum': 44,
                 'soyabean': 45, 'sunflower': 46, 'sweetpotato': 47, 'tapioca': 48, 'tomato': 49, 'turmeric': 50,
                 'watermelon': 51, 'wheat': 52}

    # Invert the dictionary to have integers as keys and crop names as values
    int_to_crop = {v: k for k, v in label_mapping.items()}

    # Example usage:
    crop_number = prediction # Replace with the actual crop number you want to look up
    crop_name = int_to_crop.get(crop_number, "Unknown Crop")

    print("Crop Name:", crop_name)


    return render_template('output.html', prediction=crop_name)


if __name__ == '__main__':
    app.run(debug=True)
