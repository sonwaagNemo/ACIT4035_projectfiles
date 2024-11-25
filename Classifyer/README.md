# Arm position Classifier

This repository contains the code and model files required to run the pre-trained machine learning classifier. The classifier should return the arm position relative its distance from the body, close, mid, or far. The model expects 6 parameters, accelerometer and gyroscope axes.

## Files in the Repository

1. **classifier.py** - This Python script loads the model and provides functions to make predictions on new data.
2. **random_forest_model.joblib** - This file contains the pre-trained Random Forest model, saved using the `joblib` library.
3. **requirements.txt** - Lists the dependencies needed to run the classifier and use the pre-trained model.

## Requirements

Before running the code, ensure that the necessary dependencies are installed. Use the `requirements.txt` file for easy installation.

### Setting Up a Python Virtual Environment

To keep your project dependencies organized and isolated, it's recommended to use a virtual environment.

#### Windows

1. **Navigate to the Project Directory**:
   Open a command prompt and change to your project directory:
   ```cmd
   cd path\to\your\project

2. **Create a Virtual Environment**:
    Run the following command to create a virtual environment named venv
   ```cmd
    python -m venv venv


3.**Activate the Virtual Environment Windows**:
 Once created, activate the virtual environment with:
    ```cmd
    venv\Scripts\activate

3.**Activate the Virtual Environment MacOS**:
 Once created, activate the virtual environment with:
    ```cmd
    source venv\Scripts\activate


4. **Install the Required Packages**: After activating the environment, install the dependencies with:
   ```cmd
    pip install -r requirements.txt


## Using the Classifier
1. **Inside the classifier.py**:
    Change the new_data variable coordinates to the new one to predict.
2. **From terminal**:
You can start making predictions using the following command from terminal
   ```cmd
    python classifier.py

## Notes

- Ensure your input data matches the format expected by the model, which is likely specified in `classifier.py`.
- The Random Forest model has been trained with a specific dataset, so generalization may vary depending on the data provided.
