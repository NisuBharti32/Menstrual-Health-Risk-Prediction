 
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import pickle
 
# Step 1: Load dataset
 
df = pd.read_csv("balanced_dataset.csv")
print("Balanced dataset loaded successfully")

# Step 2: Separate features & target
 
X = df.drop("risk_level", axis=1)
y = df["risk_level"]

 
# Step 3: FIXED Label Encoding
 
label_encoder = LabelEncoder()
label_encoder.fit([
    "Normal",
    "PCOS",
    "Hormonal Imbalance",
    "High Risk"
])

y_encoded = label_encoder.transform(y)

pickle.dump(label_encoder, open("label_encoder.pkl", "wb"))
 
# Step 4: Train-Test Split 
 
X_train, X_test, y_train, y_test = train_test_split(
    X, y_encoded,
    test_size=0.2,
    random_state=42,
    stratify=y_encoded
)
 
# Step 5: Feature Scaling
 
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

pickle.dump(scaler, open("scaler.pkl", "wb"))
 
# Step 6: Random Forest (MAIN MODEL)
rf_model = RandomForestClassifier(
    n_estimators=200,
    max_depth=10,
    class_weight="balanced",
    random_state=42
)

rf_model.fit(X_train_scaled, y_train)
 
# Step 7: Evaluate Random Forest 
rf_preds = rf_model.predict(X_test_scaled)
rf_labels = label_encoder.inverse_transform(rf_preds)
y_test_labels = label_encoder.inverse_transform(y_test)

print("\nRandom Forest Accuracy:", accuracy_score(y_test_labels, rf_labels))
print("Random Forest Report:\n", classification_report(y_test_labels, rf_labels))
print("Random Forest Confusion Matrix:\n",
      confusion_matrix(y_test_labels, rf_labels))
 
# Step 8: XGBoost (BENCHMARK) 
xgb_model = XGBClassifier(
    n_estimators=300,
    max_depth=6,
    learning_rate=0.1,
    subsample=0.8,
    colsample_bytree=0.8,
    objective="multi:softmax",
    num_class=4,
    eval_metric="mlogloss",
    random_state=42
)

xgb_model.fit(X_train_scaled, y_train)
 
# Step 9: Evaluate XGBoost 
xgb_preds = xgb_model.predict(X_test_scaled)
xgb_labels = label_encoder.inverse_transform(xgb_preds)

print("\nXGBoost Accuracy:", accuracy_score(y_test_labels, xgb_labels))
print("XGBoost Report:\n", classification_report(y_test_labels, xgb_labels))
print("XGBoost Confusion Matrix:\n",
      confusion_matrix(y_test_labels, xgb_labels))
 
# Step 10: Save models 
#pickle.dump(rf_model, open("rf_risk_model.pkl", "wb"))
#pickle.dump(xgb_model, open("xgb_risk_model.pkl", "wb"))

#print("\nModels, scaler, and label encoder saved successfully!")
