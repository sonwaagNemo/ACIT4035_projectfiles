import serial
import csv
import time

# Prompt for a filename to save the data
filename = input("Enter the filename to save IMU data (without extension): ") + ".csv"

# Prompt for the recording duration
duration = float(input("Enter the duration to record data in seconds: "))

# Set up serial connection
ser = serial.Serial('COM5', 9600, timeout=1)  # Adjust the port and baud rate as needed
ser.flush()

# Record the start time
start_time = time.time()

# Temporary storage for accelerometer and gyroscope data
accel_data = [None, None, None]
gyro_data = [None, None, None]

try:
    # Open the CSV file in write mode
    with open(filename, "w", newline='') as csv_file:
        writer = csv.writer(csv_file)
        
        # Write header row
        writer.writerow(["AccelX", "AccelY", "AccelZ", "GyroX", "GyroY", "GyroZ"])

        print(f"Recording IMU data for {duration} seconds. Press Ctrl+C to stop early.")
        while True:
            # Check if the specified duration has passed
            elapsed_time = time.time() - start_time
            if elapsed_time >= duration:
                print("Time limit reached. Stopping recording.")
                break

            if ser.in_waiting > 0:
                line = ser.readline().decode('utf-8').strip()
                print(line)  # Display each line of IMU data on the console

                # Parse accelerometer data
                if line.startswith("Accel"):
                    parts = line.replace("Accel X: ", "").replace("Y: ", "").replace("Z: ", "").split()
                    accel_data = [float(parts[0]), float(parts[1]), float(parts[2])]
                    
                # Parse gyroscope data
                elif line.startswith("Gyro"):
                    parts = line.replace("Gyro X: ", "").replace("Y: ", "").replace("Z: ", "").split()
                    gyro_data = [float(parts[0]), float(parts[1]), float(parts[2])]

                # Once both accelerometer and gyroscope data are available, write them to the CSV
                if None not in accel_data and None not in gyro_data:
                    writer.writerow(accel_data + gyro_data)
                    # Reset the temporary storage
                    accel_data = [None, None, None]
                    gyro_data = [None, None, None]

except KeyboardInterrupt:
    print("\nStopped by user before time limit.")

finally:
    ser.close()
