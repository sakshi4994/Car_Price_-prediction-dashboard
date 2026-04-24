import streamlit as st
import pandas as pd
import pickle


try:
    with open('final_model.pkl', 'rb') as f:
        model = pickle.load(f)
except FileNotFoundError:
    st.error("Model file not found. Please run your Jupyter Notebook first to save 'final_model.pkl'.")

d1={'Comprehensive':0,'Third Party insurance':1,'Zero Dep':2,'Not Available':3,'Third Party':1}
d2 = {'Petrol':0,'Diesel':1,'CNG':2}
d3={'Manual':0,'Automatic':1}
d4={'First Owner':1,'Second Owner':2, 'Third Owner':3, 'Fifth Owner':5}

st.title("🚗 Car Price Prediction Dashboard")
st.write("Enter the car details below to estimate the market price in lakhs.")

col1, col2 = st.columns(2)

with col1:
    ins_val = st.selectbox("Insurance Validity", list(d1.keys()))
    fuel_type = st.selectbox("Fuel Type", list(d2.keys()))
    transmission = st.selectbox("Transmission", list(d3.keys()))

with col2:
    seats = st.number_input("Number of Seats", min_value=2, max_value=10, value=5)
    kms_driven = st.number_input("Kilometers Driven", min_value=0, value=10000, step=500)
    ownership = st.selectbox("Ownership Status", list(d4.keys()))


if st.button("Predict Price"):
    ins_val_encoded = d1[ins_val]
    fuel_type_encoded = d2[fuel_type]
    transmission_encoded = d3[transmission]
    ownership_encoded = d4[ownership]
    kms_driven_encoded = int(kms_driven)
    seats_encoded = int(seats)
    test = [[ins_val_encoded, fuel_type_encoded, seats_encoded, kms_driven_encoded, ownership_encoded, transmission_encoded]]
    
    yp = model.predict(test)[0]

    st.success(f"### Predicted Car Price: {yp:.2f} Lakhs")
    st.balloons()

