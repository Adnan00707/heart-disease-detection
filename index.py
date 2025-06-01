import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

# Load the dataset
df = pd.read_csv(r"C:\Users\adnan\OneDrive\Desktop\Heartdiseasedetection\heart_disease_data.csv")

# Split into features and target
x = df.drop(columns='target', axis=1)
y = df['target']

# Train-test split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, stratify=y, random_state=23)

# Train model
model = LogisticRegression(max_iter=1000)
model.fit(x_train, y_train)

# Evaluate model
y_pred = model.predict(x_test)

score = accuracy_score(y_test, y_pred)
print("[✓] Model trained successfully!")
print("Accuracy score:", score)

print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# User input
print("\nPlease enter the following health data:")

age = float(input("Age: "))
sex = int(input("Sex (1 = Male, 0 = Female): "))
cp = int(input("Chest Pain Type (0–3): "))
trestbps = float(input("Resting Blood Pressure (mm Hg): "))
chol = float(input("Serum Cholesterol (mg/dl): "))
fbs = int(input("Fasting Blood Sugar > 120 (1 = Yes, 0 = No): "))
restecg = int(input("Resting ECG Results (0–2): "))
thalach = float(input("Maximum Heart Rate Achieved: "))
exang = int(input("Exercise Induced Angina (1 = Yes, 0 = No): "))
oldpeak = float(input("ST Depression Induced by Exercise: "))
slope = int(input("Slope of the ST Segment (0–2): "))
ca = int(input("Number of Major Vessels Colored (0–3): "))
thal = int(input("Thalassemia (1 = Normal, 2 = Fixed Defect, 3 = Reversible Defect): "))

# Define input with column names
input_data = {
    'age': age,
    'sex': sex,
    'cp': cp,
    'trestbps': trestbps,
    'chol': chol,
    'fbs': fbs,
    'restecg': restecg,
    'thalach': thalach,
    'exang': exang,
    'oldpeak': oldpeak,
    'slope': slope,
    'ca': ca,
    'thal': thal
}

input_df = pd.DataFrame([input_data])  # Create DataFrame with column names

# Prediction
prediction = model.predict(input_df)

# Output
print("\n🎯 Prediction result:")
if prediction[0] == 0:
    print("✅ The person has a healthy heart.")
else:
    print("⚠️ The person may have heart disease.")
