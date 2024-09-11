# Crop Prediction Model

This repository contains a Crop Prediction Model designed to assist farmers in selecting the most suitable crop to grow based on various environmental factors. By leveraging machine learning algorithms, the model predicts the best crop for given soil and weather conditions such as nitrogen, phosphorus, potassium levels, temperature, humidity, pH, and rainfall.

## Table of Contents
- [Introduction](#introduction)
- [Project Structure](#project-structure)
- [How It Works](#how-it-works)
- [Dependencies](#dependencies)
- [Usage](#usage)
- [File Descriptions](#file-descriptions)
  - [farm.ipynb](#farmipynb)
  - [app.py](#apppy)
  - [index.html](#indexhtml)
  - [farmer.csv](#farmercsv)
- [License](#license)

## Introduction

The Crop Prediction Model uses K-means clustering to analyze soil and environmental data, and based on these inputs, it suggests suitable crops for cultivation. The model is built using Python and FastAPI for the backend. It takes inputs from the farmer such as nutrient levels, temperature, humidity, pH, and rainfall to predict crop suitability. 

## Project Structure

- **farm.ipynb**: A Jupyter notebook containing data preprocessing, model training, and analysis steps.
- **app.py**: A FastAPI web service script that provides an endpoint to predict crops based on user input.
- **index.html**: A simple HTML interface for interacting with the model.
- **farmer.csv**: A dataset containing crop information and environmental conditions that the model uses.
- **README.md**: This document.

## How It Works

1. **Input Data**: The model requires the following input parameters from the user:
   - Nitrogen (N), Phosphorus (P), Potassium (K) levels in the soil
   - Temperature (°C)
   - Humidity (%)
   - Soil pH level
   - Rainfall (mm)
   
2. **Data Scaling and Clustering**: The input data is first scaled using the `standard_scaler`. The scaled data is then passed into a pre-trained K-means model to determine the most appropriate crop cluster.
   
3. **Crop Suggestion**: Once the cluster is identified, the model cross-references the dataset (`app_data.csv`) to retrieve a list of suitable crops from that cluster.

4. **API Response**: The model returns a list of crops to the user in JSON format.

## Dependencies

To run the project, you'll need the following dependencies:

- Python 3.7+
- FastAPI
- Pandas
- Scikit-learn
- Uvicorn
- Pydantic
- Jinja2
- Joblib

You can install the required libraries using the following command:

```bash
pip install -r requirements.txt
```

## Usage

To use the project:

1. Clone this repository:
   ```bash
   git clone https://github.com/your-repo-url
   cd crop-prediction
   ```

2. Train or test the model using the `farm.ipynb` notebook.

3. Run the FastAPI server:
   ```bash
   uvicorn app:app --reload
   ```

4. Access the prediction service at `http://127.0.0.1:8000/`.

5. Send a POST request to `/predict` with the following JSON structure:
   ```json
   {
     "N": 50,
     "P": 40,
     "K": 50,
     "temperature": 20.5,
     "humidity": 80,
     "ph": 6.5,
     "rainfall": 200
   }
   ```

   The API will respond with a list of suitable crops.

Alternatively, open `index.html` in a browser for a user-friendly interface to input your data.

## File Descriptions

### farm.ipynb

This Jupyter notebook contains the code for data loading, preprocessing, and model training. Key steps include:

- **Data Preprocessing**: The dataset is cleaned and scaled to ensure proper model input.
- **Model Training**: K-means clustering is applied to the data to categorize crops based on environmental conditions.
- **Evaluation**: The model's performance is evaluated using visualization techniques to ensure proper clustering.

### app.py

This file contains the FastAPI web service that allows users to interact with the model through HTTP requests. Key features of this file include:

- **Predict Route**: The `/predict` route accepts POST requests containing environmental data. It uses the pre-trained K-means model and `standard_scaler` to predict the crop cluster. Based on this, it returns a list of crops from the corresponding cluster【7†source】.
  
- **Index Route**: A root route (`/`) to render a simple HTML page (currently uses Jinja templates).

### index.html

The **index.html** file provides a user-friendly interface for farmers or users to input soil and environmental data through a web form. It collects the following parameters:
- Nitrogen (N)
- Phosphorus (P)
- Potassium (K)
- Temperature (°C)
- Humidity (%)
- pH level
- Rainfall (mm)

Upon form submission, the inputs are sent to the FastAPI backend for crop prediction. The results are displayed on the same page, allowing users to see the recommended crops in real-time. This file is essential for users who are unfamiliar with making direct HTTP requests but still want to interact with the model in a browser environment.

### farmer.csv

This CSV file contains the dataset used to train the model. It includes information on various crops and the conditions in which they thrive. The columns include:
- Nitrogen (N)
- Phosphorus (P)
- Potassium (K)
- Temperature
- Humidity
- pH Level
- Rainfall
- Crop Label

## License

This project is licensed under the MIT License.

---

This update includes the **index.html** file as a key part of the project, explaining how users can utilize it for easy interaction with the crop prediction model.
