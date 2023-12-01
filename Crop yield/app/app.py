# Importing essential libraries and modules

from flask import Flask, render_template, request, Markup
import numpy as np
import pandas as pd
import requests
import pickle
# ==============================================================================================

# -------------------------LOADING THE TRAINED MODELS -----------------------------------------------

# Loading crop recommendation model

# crop_recommendation_model_path = 'models/RandomForest.pkl'
# crop_recommendation_model = pickle.load(
#     open(crop_recommendation_model_path, 'rb'))



# ===============================================================================================
# ------------------------------------ FLASK APP -------------------------------------------------


app = Flask(__name__)

# render home page


@ app.route('/')
def home():
    title = 'Farming - Home'
    return render_template('index.html', title=title)

# render crop Yield form page

@ app.route('/crop-recommend')
def crop_recommend():
    title = 'Farming - Crop Recommendation'
    return render_template('crop.html', title=title)

# render fertilizer recommendation form page

@ app.route('/fertilizer')
def fertilizer_recommendation():
    title = 'Farming - Fertilizer Suggestion'
    return render_template('fertilizer.html', title=title)

# render crop Recommendation form page

@ app.route('/crop-re')
def crop_recommendation():
    title = 'Farming - Crop Recommendation'
    return render_template('crop-r.html', title=title)


# ===============================================================================================

# RENDER PREDICTION PAGES

# render crop Yield result page

@ app.route('/crop-predict', methods=['POST'])
def crop_prediction():
    title = 'Farming - Crop Yield Prediction'
    if request.method == 'POST':
        pH = float(request.form['pH'])
        S = float(request.form['salinity'])
        OC = float(request.form['oC'])
        N = float(request.form['nitrogen'])
        P = float(request.form['phosphorous'])
        K = float(request.form['pottasium'])
        rainfall = float(request.form['rainfall'])
        H = float(request.form['humidity'])
        MinT = float(request.form['min_Temp'])       
        MaxT = float(request.form['max_Temp'])       
        W = float(request.form['wind_Speed'])        
        Crop = request.form.get("crop")       
        season = request.form.get("season")

        # data = np.array([[N, P, K, temperature, humidity, ph, rainfall]])
        # my_prediction = crop_recommendation_model.predict(data)
        final_prediction = "Done"

        return render_template('crop-y.html', prediction=final_prediction, title=title)



# render fertilizer recommendation result page

@ app.route('/fertilizer-predict', methods=['POST'])
def fert_recommend():
    title = 'Farming - Fertilizer Suggestion'
    if request.method == 'POST':
        N = float(request.form['nitrogen'])
        print(N)
        P = float(request.form['phosphorous'])
        print(P)
        K = float(request.form['pottasium'])
        print(K)
        Temp= float(request.form['temperature'])
        print(Temp)
        H = float(request.form['humidity'])
        print(H)
        M = float(request.form['moisture'])
        print(M)
        crop_name = str(request.form['cropname'])
        print(crop_name)
        soil_name = str(request.form['soilname'])
        print(soil_name)

    print(request.form)
    response = "name"

    return render_template('fertilizer-result.html', recommendation=response, title=title)



# render crop recommendation result page

@ app.route('/crop-pred', methods=['POST'])
def c_recommend():
    title = 'Farming - recommendation Suggestion'
    if request.method == 'POST':
        N = float(request.form['nitrogen'])
        print(N)
        P = float(request.form['phosphorous'])
        print(P)
        K = float(request.form['pottasium'])
        print(K)
        Temp= float(request.form['temperature'])
        print(Temp)
        H = float(request.form['humidity'])
        print(H)

        pH = float(request.form['ph'])
        print(pH)
        rainfall = float(request.form['rainfall'])
        print(rainfall)

    print(request.form)
    final_prediction = "crop"
    return render_template('crop-result.html', prediction=final_prediction, title=title)



# ===============================================================================================
if __name__ == '__main__':
    app.run(debug=False)
