import pickle
from flask import Flask,request,jsonify,render_template
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)



# import ridge regressor and standard scaler pickle

ridge_model = pickle.load(open("models/ridge.pkl","rb"))
standard_scaler = pickle.load(open("models/scaler.pkl","rb"))

# new_data_scaled = standard_scaler.transform([[29,4,6,7,9,5,3,2,5]])
# ridge_model.predict(new_data_scaled)
# print(ridge_model)

@app.route("/")
def index():
   
    return  render_template('index.html')

@app.route('/predictdata',methods=["GET","POST"])
def predict_datapoint():
    if request.method=="POST":
        data = request.get_json()
    
        try:
            # Correct: remove commas
            temperatur = float(data["Temperature"])
            rh = float(data["RH"])
            ws = float(data["Ws"])
            rain = float(data["Rain"])
            ffmc = float(data["FFMC"])
            dmc = float(data["DMC"])
            isi = float(data["ISI"])
            classes = float(data["Classes"])
            region = float(data["Region"])

            # Put into DataFrame with correct shape
            feature_dict = {
                "Temperature": temperatur,
                "RH": rh,
                "Ws": ws,
                "Rain": rain,
                "FFMC": ffmc,
                "DMC": dmc,
                "ISI": isi,
                "Classes": classes,
                "Region": region
            }

            df = pd.DataFrame([feature_dict])
            new_data_scaled = standard_scaler.transform(df)

            prediction = ridge_model.predict(new_data_scaled)
            fwi_value = round(float(prediction[0]), 2)

            return jsonify({"fwi": fwi_value})

        except Exception as e:
            print(e)
            return jsonify({"error": str(e)})

             
    else:
        return render_template('home.html')

if __name__=="__main__":
    app.run(host="0.0.0.0")