# Crop Yield Prediction Using Machine Learning

## Project Overview

**Crop Yield Prediction Using Machine Learning** is an application designed to assist Indian farmers by predicting crop yields based on real-time soil and climatic inputs. The project integrates advanced machine learning techniques to analyze a variety of factors affecting crop output.

### Features:
- **Real-time analysis** of soil parameters for predicting yield.
- Incorporates multiple environmental factors such as:
  - Climatic data (rainfall, temperature, humidity)
  - Soil properties (macronutrients, soil type, topography)
  - Management practices (irrigation, fertilizer usage)
- Uses **Support Vector Regression (SVR)**, **Random Forest**, and **Bagging** algorithms to ensure accurate predictions.

The primary goal of the project is to empower farmers with data-driven insights to optimize agricultural productivity. Additionally, a research paper detailing this work has been published: [Research Paper](https://link.springer.com/chapter/10.1007/978-981-99-8476-3_7).

---


## Getting Started

### Prerequisites

To run this project locally, you'll need the following installed on your system:

- **Docker**: [Install Docker](https://docs.docker.com/get-docker/)
- **Docker Compose**: [Install Docker Compose](https://docs.docker.com/compose/install/)

### Running the Project

Follow these steps to get the application running locally:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Muntazir17/Crop-Yield-Prediction-Using-Machine-Learning.git
   ```

2. **Navigate to the `app` directory**:
   ```bash
   cd Crop-Yield-Prediction-Using-Machine-Learning/crop-yield/app
   ```

3. **Build and run the application using Docker Compose**:
   Run the following command to build the Docker image and start the services:
   ```bash
   docker-compose up --build
   ```

   This will:
   - Build the Docker image for the Flask application.
   - Start the application on `http://localhost:5000`.

4. **Access the Application**:
   Open your web browser and go to:
   ```bash
   http://localhost:5000
   ```

   You should see the web interface for the crop yield prediction application.

### Stopping the Application

To stop the application, run the following command:
```bash
docker-compose down
```

This will stop and remove the containers created by Docker Compose.

---

## Technologies Used

- **Machine Learning Algorithms**:
  - Support Vector Regression (SVR)
  - Random Forest
  - Bagging
- **Python**:
  - Flask for the web framework
  - PyTorch for machine learning computations
- **Frontend**:
  - HTML, CSS, JavaScript

---

## Future Enhancements

Some possible future features and improvements include:
- Adding more complex models for better prediction accuracy.
- Expanding the app to support additional crops and geographic regions.
- Integrating real-time weather data APIs for more dynamic predictions.

---
