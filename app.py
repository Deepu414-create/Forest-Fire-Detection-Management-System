
import streamlit as st
import pickle
import numpy as np
import pandas as pd

# Load model + scaler
model = pickle.load(open("../output/forest_fire_model.pkl", "rb"))
scaler = pickle.load(open("../output/scaler.pkl", "rb"))

st.title("🔥 Forest Fire Detection System")

# Single input prediction
st.header("Single Prediction")
temp = st.number_input("Temperature (°C)", 0, 50, 25)
humidity = st.number_input("Humidity (%)", 0, 100, 50)
wind = st.number_input("Wind Speed (km/h)", 0, 100, 10)
rain = st.number_input("Rain (mm)", 0, 50, 0)

if st.button("Predict Fire Risk"):
    input_data = np.array([[temp, humidity, wind, rain]])
    input_data = scaler.transform(input_data)
    prediction = model.predict(input_data)[0]
    if prediction == 1:
        st.error("⚠️ High Risk of Forest Fire!")
    else:
        st.success("✅ No Fire Risk Detected")

# Batch prediction
st.header("Batch Prediction (CSV)")
uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    features = df[['temp', 'RH', 'wind', 'rain']]
    features_scaled = scaler.transform(features)
    predictions = model.predict(features_scaled)
    df['fire_prediction'] = predictions
    st.dataframe(df)
    st.download_button("Download Predictions", df.to_csv(index=False), file_name="predictions.csv")

import pickle

output_path = "C:/Users/Deepika/Desktop/forest-fire-detection/output"  # same path

model = pickle.load(open(f"{output_path}/forest_fire_model.pkl", "rb"))
scaler = pickle.load(open(f"{output_path}/scaler.pkl", "rb"))
