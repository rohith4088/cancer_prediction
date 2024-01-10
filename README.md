# Cancer Prediction using K-Nearest Neighbors (KNN)

This is a simple web application for cancer prediction built with Flask and a K-Nearest Neighbors (KNN) machine learning model. The model is trained to predict cancer based on input features, and the application provides a user-friendly interface for making predictions.

## Getting Started

### Prerequisites

Make sure you have the following installed:

- Python
- Flask
- Numpy
- Pandas
- Pickle

You can install the required packages using the following command:

```bash
pip install flask numpy pandas
# Installation

## Clone the repository:

```bash
git clone https://github.com/rohith4088/cancer_prediction.git
cd CANCER_PREDICTION

Run the Flask application:
python app.py
Open your web browser and go to http://localhost:5000 to access the application.

Usage
Visit the home page to input data for cancer prediction.
Alternatively, you can use the /predict_api endpoint to make predictions via API by sending a JSON request.

Model Details
The KNN model for cancer prediction is trained using the data provided.
Feature scaling is applied using a scaler saved as scaling.pkl.
The trained model is saved as knn_model.pkl.

Web Application Routes
Home Page (/): Provides a user interface for entering input data.
Prediction Page (/predict): Accepts input data, processes it, and displays the predicted result.
API Endpoint (/predict_api): Accepts JSON data and returns the predicted result.

Contributing
Feel free to contribute by opening issues or submitting pull requests. Your feedback and contributions are welcome!

License
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgments
Flask
Scikit-learn
Pandas
Numpy
