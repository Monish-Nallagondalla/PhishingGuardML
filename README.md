
# PhishingGuardML

PhishingGuardML is a machine learning-based project designed to detect phishing websites by analyzing URL and website features. This repository leverages a robust pipeline for data ingestion, transformation, validation, and model training, integrated with FastAPI for serving predictions and MLflow for experiment tracking. The project is hosted on [DagsHub](https://dagshub.com/Monish-Nallagondalla/PhishingGuardML) and uses GitHub Actions for CI/CD to deploy the application on AWS ECS.

## Table of Contents
- [Project Overview](#project-overview)
- [Features](#features)
- [Dataset](#dataset)
- [Installation](#installation)
- [Project Structure](#project-structure)
- [Usage](#usage)
- [CI/CD Pipeline](#cicd-pipeline)
- [MLflow Integration](#mlflow-integration)
- [Contributing](#contributing)
- [License](#license)

## Project Overview
PhishingGuardML aims to identify phishing websites using a machine learning model trained on a dataset of website features. The project includes a modular pipeline for data processing, model training, and deployment. It uses FastAPI for creating a web API to serve predictions and MLflow for tracking experiments, integrated with DagsHub for version control and experiment management.

## Features
- **Data Ingestion**: Loads and processes data from CSV files stored in the `Network_Data` directory.
- **Data Transformation**: Preprocesses features for model training.
- **Data Validation**: Ensures data quality and checks for data drift.
- **Model Training**: Trains machine learning models and saves them in the `final_model` directory.
- **FastAPI Integration**: Provides a RESTful API for real-time phishing detection.
- **MLflow Tracking**: Logs experiments, parameters, and metrics on DagsHub.
- **CI/CD Pipeline**: Automates testing, building, and deployment to AWS ECS using GitHub Actions.
- **Dockerized Deployment**: Runs the application in a Docker container for scalability.

## Dataset
The dataset (`phisingData.csv`) contains features related to website URLs and properties, such as:
- `having_IP_Address`
- `URL_Length`
- `Shortining_Service`
- `having_At_Symbol`
- `double_slash_redirecting`
- `Prefix_Suffix`
- ... (and more, see the dataset for the full list)
- `Result`: The target variable indicating whether a website is phishing (-1) or legitimate (1).

The dataset is stored in the `Network_Data` directory and is processed through the pipeline for training and validation.

## Installation
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Monish-Nallagondalla/PhishingGuardML.git
   cd PhishingGuardML
   ```

2. **Set Up a Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

   The `requirements.txt` includes:
   ```
   python-dotenv
   pandas
   numpy
   pymongo
   certifi
   pymongo[srv]==3.6
   scikit-learn
   mlflow
   pyaml
   dagshub
   fastapi
   uvicorn
   python-multipart
   ```

4. **Set Up Environment Variables**:
   Create a `.env` file in the root directory with necessary configurations (e.g., MongoDB URI, AWS credentials, DagsHub tokens).

5. **Run the Application**:
   ```bash
   uvicorn networksecurity:app --reload
   ```

   The FastAPI application will be available at `http://localhost:8000`.

## Project Structure
```
PhishingGuardML/
├── .gitignore
├── app.py                    # FastAPI application entry point
├── Dockerfile                # Docker configuration for deployment
├── LICENSE                   # License file
├── main.py                   # Main script for running the pipeline
├── push_data.py              # Script for pushing data to storage
├── README.md                 # This file
├── requirements.txt          # Python dependencies
├── setup.py                  # Setup script for the project
├── test_mongo.py             # Unit tests for MongoDB
├── test_mongodb.py           # Additional MongoDB tests
├── Artifacts/                # Stores pipeline artifacts (data, models, reports)
│   ├── 06_09_2025_23_01_44/  # Timestamped artifact directories
│   ├── ...                   # Other timestamped directories
│   ├── data_ingestion/       # Ingested data
│   ├── data_transformation/  # Transformed data
│   ├── data_validation/      # Validation reports
│   ├── feature_store/        # Feature storage
│   ├── final_model/          # Trained models (model.pkl, preprocessor.pkl)
├── data_schema/              # Schema definitions
│   ├── schema.yaml
├── mlruns/                   # MLflow experiment tracking
├── Network_Data/             # Input dataset
│   ├── phisingData.csv
├── networksecurity/          # Core project modules
│   ├── __init__.py
│   ├── cloud/                # Cloud-related utilities (e.g., s3_syncer.py)
│   ├── components/           # Pipeline components (data ingestion, transformation, etc.)
│   ├── constant/             # Constants and configurations
│   ├── entity/               # Data entities (artifact_entity.py, config_entity.py)
│   ├── exception/            # Custom exceptions
│   ├── logging/              # Logging utilities
│   ├── pipeline/             # Training pipeline
│   ├── utils/                # Utility functions
├── notebooks/                # Jupyter notebooks for experimentation
├── templates/                # HTML templates for FastAPI
│   ├── table.html
```

## Usage
1. **Run the Pipeline**:
   Execute `main.py` to run the full data ingestion, transformation, validation, and model training pipeline:
   ```bash
   python main.py
   ```

2. **Access the API**:
   Start the FastAPI server:
   ```bash
   uvicorn networksecurity:app --reload
   ```
   Visit `http://localhost:8000/docs` for the interactive API documentation.

3. **View MLflow Experiments**:
   Access MLflow tracking on DagsHub: [https://dagshub.com/Monish-Nallagondalla/PhishingGuardML](https://dagshub.com/Monish-Nallagondalla/PhishingGuardML).

4. **Deploy with Docker**:
   Build and run the Docker container:
   ```bash
   docker build -t phishingguardml .
   docker run -d -p 8080:8080 phishingguardml
   ```

## CI/CD Pipeline
The project uses GitHub Actions for continuous integration and continuous deployment (CI/CD). The workflow is defined in `.github/workflows/workflow.yml` and includes:
- **Continuous Integration**:
  - Lints the code and runs unit tests on every push to the `main` branch.
- **Continuous Delivery**:
  - Builds a Docker image and pushes it to Amazon ECR.
- **Continuous Deployment**:
  - Deploys the Docker image to AWS ECS on a self-hosted runner.

To configure the CI/CD pipeline, ensure the following secrets are set in your GitHub repository:
- `AWS_ACCESS_KEY_ID`
- `AWS_SECRET_ACCESS_KEY`
- `AWS_REGION`
- `ECR_REPOSITORY_NAME`
- `AWS_ECR_LOGIN_URI`

## MLflow Integration
MLflow is integrated with DagsHub for experiment tracking. All experiments, parameters, metrics, and models are logged to the DagsHub MLflow server. To view experiments:
1. Visit [https://dagshub.com/Monish-Nallagondalla/PhishingGuardML](https://dagshub.com/Monish-Nallagondalla/PhishingGuardML).
2. Navigate to the MLflow section to explore logged runs and artifacts.

## Contributing
Contributions are welcome! Please follow these steps:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit (`git commit -m "Add feature"`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a pull request on GitHub.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.