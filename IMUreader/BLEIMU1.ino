#include <Arduino_BMI270_BMM150.h>  // IMU library

void setup() {
  Serial.begin(9600);
  while (!Serial);

  // Initialize IMU
  if (!IMU.begin()) {
    Serial.println("Failed to initialize IMU!");
    while (1);
  }
  Serial.println("IMU initialized.");
}

void loop() {
  // Check if accelerometer data is available
  if (IMU.accelerationAvailable()) {
    float ax, ay, az;

    // Read accelerometer data
    IMU.readAcceleration(ax, ay, az);

    // Print accelerometer data to Serial
    Serial.print("Accel X: "); Serial.print(ax);
    Serial.print(" Y: "); Serial.print(ay);
    Serial.print(" Z: "); Serial.println(az);
  }

  // Check if gyroscope data is available
  if (IMU.gyroscopeAvailable()) {
    float gx, gy, gz;

    // Read gyroscope data
    IMU.readGyroscope(gx, gy, gz);

    // Print gyroscope data to Serial
    Serial.print("Gyro X: "); Serial.print(gx);
    Serial.print(" Y: "); Serial.print(gy);
    Serial.print(" Z: "); Serial.println(gz);
  }

  delay(1500); // Adjust delay for preferred data transmission rate
}


