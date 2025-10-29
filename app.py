import streamlit as st
import pickle
import numpy as np

# Load model and encoders
model = pickle.load(open('car_price_model.pkl', 'rb'))
le_fuel = pickle.load(open('le_fuel_type.pkl', 'rb'))
le_seller = pickle.load(open('le_seller_type.pkl', 'rb'))
le_trans = pickle.load(open('le_transmission.pkl', 'rb'))

st.title("Welcome to CarValueAI")

present_price = st.number_input("Present Price (Lakhs)", min_value=0.01, step=0.01)
kms_driven = st.number_input("Kms Driven", min_value=0)
fuel_type = st.selectbox("Fuel Type", ('Petrol', 'Diesel', 'CNG'))
seller_type = st.selectbox("Seller Type", ('Dealer', 'Individual'))
transmission = st.selectbox("Transmission", ('Manual', 'Automatic'))
owner = st.number_input("Owner", min_value=0, max_value=3, step=1)
car_age = st.number_input("Car Age (years)", min_value=0, step=1)

if st.button("Predict"):
    # Encode inputs
    fuel_enc = le_fuel.transform([fuel_type])[0]
    seller_enc = le_seller.transform([seller_type])[0]
    trans_enc = le_trans.transform([transmission])[0]

    features = np.array([[present_price, kms_driven, fuel_enc, seller_enc, trans_enc, owner, car_age]])
    prediction = model.predict(features)[0]
    st.success(f"Predicted Selling Price: ₹{prediction:.2f} Lakhs")
