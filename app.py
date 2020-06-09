# API conect HTML - GeoRef and Predeict

## Dependencies and Setup
import pandas as pd
import numpy as np
import requests
import scipy.stats as stats
import json
from flask import Flask, jsonify, render_template, request, url_for
import joblib
#from geopy.geocoders import Nominatim

# Google developer API key
google_api_key ="AIzaSyBu--MADrBgOEaTUWY-8jquwBvhFKCp--s"

## 

app = Flask(__name__)

#Call Model:
filename = 'model_74.sav' 
model = joblib.load(filename)

#Call Scaler:
X_Scaler = 'X_scaler.sav' 
X_Scaler = joblib.load(X_Scaler)
y_Scaler = 'y_scaler.sav' 
y_Scaler = joblib.load(y_Scaler)

#################################################
# Flask Routes
#################################################

@app.route('/')
def home():
    "Rutas disponibles:"
    "http://127.0.0.1:5000/predict/<room>/<bathroom>/<construction>/<terrain>/<direction>/<casa>/<casa_en_c>/<depto>/<nuevo>/<remate>"
    "http://127.0.0.1:5000/datos"
    return render_template('index.html')


#################################################

@app.route('/datos')
def datos():
    #"Nada"
    datos = pd.read_csv('Datos_Sel.csv').fillna(0).to_dict(orient = 'records')
    return jsonify(datos)

#################################################
#@app.route('/predict/<room>/<bathroom>/<construction>/<terrain>/<direction>/<casa>/<casa_en_c>/<depto>/<nuevo>/<remate>', methods=['GET'])
@app.route('/predict/<room>/<bathroom>/<construction>/<terrain>/<direction>/<casa>/<casa_en_c>/<depto>/<nuevo>/<remate>')
def predict(room, bathroom, construction, terrain, direction, casa, casa_en_c, depto, nuevo, remate):
    
    # Datos Dummy:
    ###### 
    # http://127.0.0.1:5000/predict/2/1/80/80/Parque%Espa%C3%B1a%20la%Condesa/0/0/1/1/0
    
    # Búsqueda
    ## Function: Locate address
    # Build URL using the Google Maps API
    base_url = "https://maps.googleapis.com/maps/api/geocode/json"
    params = {"address": direction, "key": google_api_key}
    #loop to get all locations from locaitions
    lat = []
    lon = []
    
    try:
        response = requests.get(base_url, params={"address": direction,"key": google_api_key})
        geo      = response.json()
        lat.append(geo["results"][0]["geometry"]["location"]["lat"])
        lon.append(geo["results"][0]["geometry"]["location"]["lng"])
            
    except (KeyError, IndexError):
        notfound.append(index)
        


    float_features = [room, bathroom, construction, terrain, lon[0], lat[0], nuevo, remate, casa, casa_en_c, depto]
    
    float_features = np.array(float_features).reshape(1, -1)
   
    float_features = X_Scaler.transform(float_features)
    #float_features= X_Scaler.fit(float_features).transform(float_features)

    prediction = model.predict(float_features)
    
    prediction = y_Scaler.inverse_transform(prediction)

    output = round(prediction[0], 2)

    # Return
    #return jsonify(output, lon, lat)
    return jsonify(output)

#################################################

if __name__ == "__main__":
    app.run(debug=True)
    
#