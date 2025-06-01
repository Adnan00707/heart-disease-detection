# 💓 Heart Disease Detection Web App

This project is a machine learning-based web application that predicts the likelihood of heart disease based on user input. It is designed to be user-friendly, fast, and visually appealing.It provides doctors and medical professionals with a quick, data-driven assessment tool, making their work faster and more efficient

🔗 **Live App**: [Heart Disease Detector](https://heart-disease-detectorgunicorn-app-app.onrender.com)

---

## 🧰 Technologies Used

| Technology     | Purpose                                  |
|----------------|-------------------------------------------|
| **Python**     | Programming language                     |
| **Flask**      | Web framework for backend logic          |
| **scikit-learn** | Model training (Logistic Regression)   |
| **HTML/CSS**   | Frontend interface & custom styling      |
| **Gunicorn**   | Production-ready WSGI server             |
| **Render**     | Hosting and deployment                   |
| **pandas, numpy** | Data handling and preprocessing       |

---

## 🌟 Features

- 🎯 Predicts if a person is likely to have heart disease
- ✅ Logistic Regression model trained on real clinical data
- 🧠 Classification report displayed in terminal
- 📊 13 input fields used for prediction
- 🎨 Heart-themed UI design with responsive layout

---

![image](https://github.com/user-attachments/assets/ceed9a33-5207-4ef8-94af-2a34878ee9cb)


---

## 🧪 How to Use

1. Go to: [https://heart-disease-detectorgunicorn-app-app.onrender.com](https://heart-disease-detectorgunicorn-app-app.onrender.com)
2. Enter the following medical inputs:
   - Age
   - Sex (1 = Male, 0 = Female)
   - Chest Pain Type (0–3)
   - Resting Blood Pressure
   - Cholesterol Level
   - Fasting Blood Sugar > 120 (1 = Yes, 0 = No)
   - ECG Results (0–2)
   - Maximum Heart Rate Achieved
   - Exercise Induced Angina (1 = Yes, 0 = No)
   - ST Depression
   - Slope of ST Segment (0–2)
   - Major Vessels (0–3)
   - Thalassemia (1 = Normal, 2 = Fixed, 3 = Reversible)
3. Click the **Predict** button
4. View result: ✅ *Healthy* or ⚠️ *At Risk*

---

## 📁 Project Structure
HeartDiseaseDetection/
│
├── app.py # Flask backend
├── model.py # Trains and saves Logistic Regression model
├── model.pkl # Trained model file
├── requirements.txt # Dependencies
├── static/
│ └── style.css # Custom CSS with heart background
├── templates/
│ └── index.html # HTML page for UI

✅ Sample Input & Output

When you run the program, it will prompt you to enter the following health details one by one:
Age: 55
Sex (1 = Male, 0 = Female): 1
Chest Pain Type (0–3): 2
Resting Blood Pressure (mm Hg): 140
Serum Cholesterol (mg/dl): 250
Fasting Blood Sugar > 120 (1 = Yes, 0 = No): 1
Resting ECG Results (0–2): 1
Maximum Heart Rate Achieved: 150
Exercise Induced Angina (1 = Yes, 0 = No): 0
ST Depression Induced by Exercise: 1.5
Slope of the ST Segment (0–2): 2
Number of Major Vessels Colored (0–3): 0
Thalassemia (1 = Normal, 2 = Fixed Defect, 3 = Reversible Defect): 3
After entering the data, you will see the model’s prediction and accuracy score like this:
[✓] Model trained successfully!
Accuracy score: 0.85

🎯 Prediction result:
⚠️ The person may have heart disease.
________________________________________
🛠️ Technologies Used
•	Python
•	pandas
•	scikit-learn (Logistic Regression, model selection, evaluation)
________________________________________
📌 How to Run
1.	Clone the repository or download the .py file.
2.	Ensure you have the dataset in the same folder or correct path.

👨‍💻 Author
Adnan
________________________________________
📄 License
This project is for educational purposes


