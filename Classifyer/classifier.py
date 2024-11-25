import joblib
import pandas as pd

# Load the Random Forest model
rf_model = joblib.load('random_forest_model.joblib')

# Feature names and new input data
feature_names = ['AccelX', 'AccelY', 'AccelZ', 'GyroX', 'GyroY', 'GyroZ']

# Arm position to classify
new_data = pd.DataFrame([[-0.86,0.18,0.4,2.44,0.55,0.31]], columns=feature_names)

# Make a prediction
prediction = rf_model.predict(new_data)
print("Predicted Position:", prediction[0])
