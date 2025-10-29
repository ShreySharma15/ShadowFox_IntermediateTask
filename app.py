# Save this as app.py after downloading your .pkl files to a folder

from flask import Flask, request, render_template
import pickle
import numpy as np

# Load model and encoders
model = pickle.load(open('car_price_model.pkl', 'rb'))
le_fuel = pickle.load(open('le_fuel_type.pkl', 'rb'))
le_seller = pickle.load(open('le_seller_type.pkl', 'rb'))
le_trans = pickle.load(open('le_transmission.pkl', 'rb'))

app = Flask("CarValueAI")

@app.route('/', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        # Get data from form
        present_price = float(request.form['present_price'])
        kms_driven = int(request.form['kms_driven'])
        fuel_type = request.form['fuel_type']
        seller_type = request.form['seller_type']
        transmission = request.form['transmission']
        owner = int(request.form['owner'])
        car_age = int(request.form['car_age'])
        
        # Encode string inputs
        fuel_type_enc = le_fuel.transform([fuel_type])[0]
        seller_type_enc = le_seller.transform([seller_type])[0]
        trans_enc = le_trans.transform([transmission])[0]
        
        features = np.array([[present_price, kms_driven, fuel_type_enc, seller_type_enc, trans_enc, owner, car_age]])
        prediction = model.predict(features)[0]
        return render_template('index.html', prediction=round(prediction, 2))
    return render_template('index.html', prediction=..., appname="CarValueAI")

if __name__ == '__main__':
    app.run(debug=True)
