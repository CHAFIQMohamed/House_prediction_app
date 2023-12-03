# Machine Learning Lifecycle with MLflow, FastAPI, and Flask

## Introduction

This repository showcases an end-to-end machine learning lifecycle, incorporating data preprocessing, model training, deployment as REST APIs, and application consumption. We leverage MLflow, FastAPI, and Flask to seamlessly orchestrate each phase.

## Steps

### 1. Using MLflow

- **Data Preprocessing:**
  Start by preparing and cleaning your dataset.

- **Train 5 ML Models:**
  Utilize a diverse set of machine learning models for training.

- **Track Models:**
  Implement model tracking with MLflow to monitor performance, versions, and parameters.

- **Save Best Model:**
  Save the best-performing model in ONNX format and its dedicated preprocessing transformations using the Transformers API in pickle format.

### 2. Using FastAPI

- **Create a REST API:**
  Develop a FastAPI-based REST API for deploying your machine learning model.

- **Package Model as a Container:**
  Package your model as a container using Docker, ensuring portability and scalability.

- **Consume APIs using Postman:**
  Utilize Postman to interact with and test your deployed APIs.

### 3. Using Flask

- **Create a Dedicated Application:**
  Develop a dedicated Flask application designed to consume your deployed API.

- **Package Application as a Container:**
  Package your Flask application as a container using Docker for efficient deployment.

## Getting Started

Follow these steps to run the project locally:

1. Clone this repository:
   ```bash
   git clone [Your GitHub Repository URL]
   cd [Repository Directory]
