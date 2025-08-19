import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
import pickle

# Load dataset
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/forest-fires/forestfires.csv"
df = pd.read_csv(url)

# Create binary target
df['fire'] = np.where(df['area'] > 0, 1, 0)

# Features & target
X = df[['temp', 'RH', 'wind', 'rain']]
y = df['fire']

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Scale features
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Train Random Forest
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Save model & scaler to output folder
with open("../output/forest_fire_model.pkl", "wb") as f:
    pickle.dump(model, f)
with open("../output/scaler.pkl", "wb") as f:
    pickle.dump(scaler, f)

print("✅ Model trained and saved in output folder!")

import pickle

output_path = "C:/Users/Deepika/Desktop/forest-fire-detection/output"  

# Save model
with open(f"{output_path}/forest_fire_model.pkl", "wb") as f:
    pickle.dump(model, f)

# Save scaler
with open(f"{output_path}/scaler.pkl", "wb") as f:
    pickle.dump(scaler, f)

