import pandas as pd
import numpy as np

# Set random seed
np.random.seed(42)

# Number of samples per class
n = 500

# Feature generation function
def generate_features(risk_level, n):
    data = []
    for _ in range(n):
        if risk_level == 'Normal':
            row = {
                'age': np.random.randint(18, 35),
                'cycle_length': np.random.randint(25, 30),
                'period_duration': np.random.randint(3,6),
                'flow_level': np.random.randint(1,3),
                'cramps': 0,
                'mood_swings': 0,
                'acne': 0,
                'weight_gain': 0,
                'hair_fall': 0,
                'fatigue': 0,
                'irregular_periods': 0,
                'missed_periods': 0,
                'risk_level': risk_level
            }
        elif risk_level == 'Hormonal Imbalance':
            row = {
                'age': np.random.randint(18, 40),
                'cycle_length': np.random.randint(26, 35),
                'period_duration': np.random.randint(4,7),
                'flow_level': np.random.randint(1,3),
                'cramps': 1,
                'mood_swings': 1,
                'acne': 0,
                'weight_gain': 0,
                'hair_fall': 0,
                'fatigue': 1,
                'irregular_periods': 0,
                'missed_periods': 0,
                'risk_level': risk_level
            }
        elif risk_level == 'PCOS':
            row = {
                'age': np.random.randint(18, 40),
                'cycle_length': np.random.randint(35, 60),
                'period_duration': np.random.randint(5,9),
                'flow_level': np.random.randint(2,4),
                'cramps': 1,
                'mood_swings': 1,
                'acne': 1,
                'weight_gain': 1,
                'hair_fall': 1,
                'fatigue': 1,
                'irregular_periods': 1,
                'missed_periods': np.random.randint(1,3),
                'risk_level': risk_level
            }
        else: # High Risk
            row = {
                'age': np.random.randint(25, 45),
                'cycle_length': np.random.randint(40, 70),
                'period_duration': np.random.randint(7,12),
                'flow_level': 3,
                'cramps': 1,
                'mood_swings': 1,
                'acne': 1,
                'weight_gain': 1,
                'hair_fall': 1,
                'fatigue': 1,
                'irregular_periods': 1,
                'missed_periods': np.random.randint(2,4),
                'risk_level': risk_level
            }
        data.append(row)
    return data

# Generate data for all classes
data = []
for cls in ['Normal','Hormonal Imbalance','PCOS','High Risk']:
    data.extend(generate_features(cls, n))

df = pd.DataFrame(data)

# Shuffle the dataset
df = df.sample(frac=1, random_state=42).reset_index(drop=True)

# Save to CSV
df.to_csv('balanced_dataset.csv', index=False)
print("Balanced dataset created with shape:", df.shape)
