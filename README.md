# Forest-Fire-Detection-Management-System
An intelligent Forest Fire Detection System that uses AI and sensors to monitor forests in real-time, detecting fire outbreaks early to prevent large-scale damage. It enhances safety and enables rapid response to protect wildlife and ecosystems.
# 🌲 Forest Fire Detection Management System

**Author:** Poodu Deepika  
**Roll Number:** 22781A3134  
**Department:** CSE-AI  

---

## 🔹 Project Description

This project is a **Forest Fire Detection Management System** built using **Python, Machine Learning, and Streamlit**.  
The system predicts the risk of forest fire based on environmental features like **temperature, humidity, wind, and rainfall**.  

It uses a **Random Forest Classifier** trained on the **UCI Forest Fires dataset**.  
A **GUI interface** allows users to input values or upload a CSV file to predict fire risk for single or multiple entries.

---

## 🔹 Features

- 🔥 Predict forest fire risk based on environmental data  
- 🌡️ Input temperature, humidity, wind speed, and rainfall  
- 📊 Supports batch predictions via CSV upload (optional)  
- 🌐 Accessible GUI using **Streamlit** with a public link via **ngrok/localtunnel**  
- ✅ Shows prediction results clearly: High Risk / No Risk  

---

## 🔹 Dataset

- Dataset source: [UCI Forest Fires Dataset](https://archive.ics.uci.edu/ml/datasets/forest+fires)  
- Features used:  
  - `temp` – Temperature (°C)  
  - `RH` – Relative Humidity (%)  
  - `wind` – Wind Speed (km/h)  
  - `rain` – Rainfall (mm)  
- Target: `fire` – 1 if forest fire occurs, 0 if no fire  

---

## 🔹 Installation & Setup

1. Clone the repository:  
```bash
git clone https://github.com/YourUsername/forest-fire-detection.git
cd forest-fire-detection
pip install streamlit pandas scikit-learn matplotlib pyngrok
streamlit run app.py
!ngrok config add-authtoken 31UhRYOOiBM9CqQyz94fhRssXY6_3j7PwG1CFKpEwhtQ7EimP
1.Usage

Open the Streamlit GUI (local or public link).

Enter the environmental values (temperature, humidity, wind, rain).

Click Predict Fire Risk to see the result.

(Optional) Upload a CSV file for batch prediction and view all results.

2.Technologies Used

Python 3.x

Streamlit (GUI)

Scikit-learn (Random Forest Classifier)

Pandas, NumPy (Data processing)

Matplotlib (Optional for graphs)

3.Future Enhancements

Add real-time alerts for forest fire risk

Add map visualization of high-risk zones

Integrate IoT sensors for live environmental data
