# Menstrual Health Risk Prediction System

 A machine learning–based web application that predicts menstrual health risks such as **Normal**, **PCOS**, **Hormonal Imbalance**, and **High Risk** based on user-reported symptoms and cycle patterns.

The system leverages supervised machine learning techniques to analyze multiple health indicators and provide accurate risk classification. It is designed with a strong emphasis on medical safety, ensuring that high-risk cases are prioritized and not missed.

In addition to risk prediction, the application offers decision support features such as medical guidance and next menstrual cycle estimation, making it suitable for real-world use. The project integrates machine learning with a secure, user-friendly web interface, demonstrating an end-to-end approach from data preprocessing and model evaluation to deployment-ready application design.

##  Features

-    Secure user authentication (Login & Register)
-    Machine learning–based risk prediction
-    Random Forest model with **98.5% accuracy**
-    Balanced dataset with class-wise evaluation
-    High-risk case prioritization (100% recall for high-risk cases)
-    Next menstrual cycle prediction
-    Light/Dark mode user interface
-    End-to-end web application (ML + Backend + Frontend)

---

##  Machine Learning Details

- **Algorithms Used:**  
  - Random Forest (Primary Model)  
  - XGBoost (Benchmark Model)

- **Why Random Forest?**  
  Random Forest was selected because it achieved high accuracy while ensuring **no high-risk cases were missed**, which is critical for medical prediction systems.

- **Model Performance:**  
  - Accuracy: **98.5%**
  - High Risk Recall: **100%**
  - Evaluation Metrics: Accuracy, Precision, Recall, F1-score, Confusion Matrix

---

##  Technologies Used

- **Programming Language:** Python  
- **Machine Learning:** Scikit-learn, XGBoost  
- **Backend:** Flask  
- **Database:** SQLite  
- **Frontend:** HTML, CSS, JavaScript  
- **Security:** Password hashing, session management  

---

##  Project Structure
```
 Menstrual-Health-Risk-Prediction/
│
├── app.py # Flask backend application
├── model.py # Machine learning training script
├── requirements.txt # Project dependencies
├── balanced_dataset.csv # Dataset used for training
├── generate_dataset.py # Dataset generation/preprocessing script
│
├── templates/ # HTML templates
│ ├── index.html
│ ├── login.html
│ └── register.html
│
├── static/ # Static files
│ ├── style.css
│ └── script.js
│
├── rf_risk_model.pkl # Trained Random Forest model
├── xgb_risk_model.pkl # Trained XGBoost model
├── scaler.pkl # Feature scaler
└── label_encoder.pkl # Label encoder
```
## Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/NisuBharti32/Menstrual-Health-Risk-Prediction.git
cd Menstrual-Health-Risk-Prediction
```
### 2. Create Virtual Environment
``` python -m venv venv
source venv/Scripts/activate   # on Windows
```
### 3. Install Dependencies
```
 pip install -r requirements.txt
```
 ### 4. Train the Machine Learning Model
```
 python model.py

```
 
 ### 5. Run the Application
 ```
    python app.py
 ```
Open the browser and go to:
 ```
 http://127.0.0.1:5000


 ```

## Use Case

- Enables users to monitor menstrual health patterns using symptom-based inputs.
- Predicts potential health risks such as PCOS, hormonal imbalance, and high-risk conditions.
- Helps in early risk identification to encourage timely medical consultation.
- Provides basic medical guidance based on predicted risk levels.
- Estimates the next menstrual cycle date to support personal health tracking.

##  Future Enhancements

- Integration with real clinical datasets
- Explainable AI (SHAP) for feature importance
- Mobile application version
- Doctor/Admin dashboard
- Cloud deployment (AWS/Render)

##  Disclaimer

This project is intended for educational and research purposes only.
It is not a substitute for professional medical diagnosis or treatment.

##  Author

Developed as a Machine Learning and Web Development project.

## License

This project is licensed under the MIT License.

