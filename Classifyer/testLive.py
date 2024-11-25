import joblib
import pandas as pd
import serial
import time

# Load the Random Forest model
rf_model = joblib.load(r'.\Classifyer\random_forest_model.joblib')

# Feature names for the classifier
feature_names = ['AccelX', 'AccelY', 'AccelZ', 'GyroX', 'GyroY', 'GyroZ']

# Set up serial connection
ser = serial.Serial('COM5', 9600, timeout=1)
ser.flush()

print("Starting real-time classification. Press Ctrl+C to stop.")

try:
    while True:
        if ser.in_waiting > 0:
            line = ser.readline().decode('utf-8').strip()
            print("Received:", line)  # For debugging, prints raw serial data

            # Parse the IMU data
            if line.startswith("Accel"):
                accel_values = line.replace("Accel X: ", "").replace("Y: ", "").replace("Z: ", "").split()
                accel_data = [float(value) for value in accel_values]

            elif line.startswith("Gyro"):
                gyro_values = line.replace("Gyro X: ", "").replace("Y: ", "").replace("Z: ", "").split()
                gyro_data = [float(value) for value in gyro_values]

                # When both accelerometer and gyroscope data are available
                if accel_data and gyro_data:
                    # Combine accel and gyro data into a single feature set
                    feature_set = accel_data + gyro_data

                    # Format the data as a DataFrame for the classifier
                    input_data = pd.DataFrame([feature_set], columns=feature_names)

                    # Make a prediction
                    prediction = rf_model.predict(input_data)
                    print("Predicted Position:", prediction[0])

                    # Clear data for the next loop
                    accel_data, gyro_data = None, None

            time.sleep(0.1)  # Adjust based on data rate

except KeyboardInterrupt:
    print("Real-time classification stopped by user.")

finally:
    ser.close()
    