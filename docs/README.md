# Telugu Speech API Documentation

## Overview

The Telugu Speech API is a service designed for recognizing Telugu digits (0-9) from audio input. It integrates a pre-trained CNN-based model to process audio data and return predictions. The application is built using FastAPI and Dockerized for ease of deployment.

---

## Folder Structure

```
project-root/
├── model/                      # Pre-trained machine learning models
├── utils/                      # Helper scripts (e.g., audio preprocessing)
├── src/                        # Main application code
│   ├── app.py                  # Entry point for the FastAPI application
│   ├── client_request.py       # Handles client-side logic-to get prediction
├── tests/                      # Contains audio files to test using client_request.py
├── docker/                     # Docker-related files
│   ├── docker-compose.yml      # Docker Compose configuration
│   ├── Dockerfile              # Docker image build configuration
│   └── .dockerignore           # Files and directories to ignore during build
├── docs/                       # Documentation
│   └── README.md               # Main documentation file
├── requirements.txt            # Python dependencies
└── .gitignore                  # Git ignored files
```

---

## Key Components

### 1. **Model**

- **Location**: `model/`
- **Purpose**: Contains the trained CNN model for Telugu digit recognition.
- **File Format**: `.h5`

### 2. **Utils**

- **Location**: `utils/`
- **Purpose**: Houses utility scripts for:
  - Audio preprocessing

### 3. **Source Code**

- **Location**: `src/`
- **Purpose**: Main application logic.
  - `app.py`: Defines the FastAPI application, initializes routes, and serves the API.
  - `client_request.py`: Handles requests and prepares input for the model.

### 4. **Docker**

- **Location**: `docker/`
- **Files**:
  - `Dockerfile`: Instructions for building the Docker image.
  - `docker-compose.yml`: Configuration for multi-container setups (if applicable).
  - `.dockerignore`: Lists files/directories to exclude during the image build.

---
## Installation

### Prerequisites

1. Python 3.10 or higher
2. Docker and Docker Compose
3. Git

### Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/umaalugubilli/Telugu-Speech-Recogniser-API
   cd speech-api
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the application locally:
   ```bash
   uvicorn src.app:app --host 0.0.0.0 --port 8000
   ```
4. Run using Docker:
   ```bash
   docker-compose up --build
   ```

---

## API Endpoints

### 1. **Prediction Endpoint**

- **URL**: `/`recognize
- **Method**: `POST`
- **Description**: Accepts an audio file and returns the predicted digit.
- **Request Format**:
  - **Headers**: `Content-Type: multipart/form-data`
  - **Body**: An audio file (e.g., `.wav`, mono, 16 kHz)
- **Response**:
  ```json
  {
    "predicted_digit": 5,
  }
  ```

---

## Docker Configuration

### Dockerfile

```dockerfile
# Base image with Python
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy application files
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt
RUN apt-get update && apt-get install -y libsndfile1

COPY . /app

# Expose port 8000
EXPOSE 8000

# Command to run the application
CMD ["uvicorn", "src.app:app", "--host", "0.0.0.0", "--port", "8000"]
```

### Docker Compose

```yaml
version: '3.8'

services:
  telugu-speech-app:
    build:
      context: .
      dockerfile: docker/dockerfile
    ports:
      - "8000:8000"
    volumes:
      - .:/app
    environment:
      - ENV=production
```

---

## Deployment

### Local Deployment

1. Ensure Docker is installed.
2. Build and run the application:
   ```bash
   docker-compose up --build
   ```

### Cloud Deployment

1. Use a cloud provider like AWS, Azure, or GCP.
2. Set up a CI/CD pipeline for automatic deployment.
3. Ensure security measures such as HTTPS and authentication.

---

## Future Improvements

1. Add live streaming support for real-time digit recognition.
2. Enhance the model to handle background noise and accents.
3. Expand to multi-digit recognition.
4. Integrate with a frontend for an interactive user experience.

---

## Contact

For support or inquiries, contact:

- **Name**: Uma Maheshwararao Alugubilli
- **Email**: maheshalugubilli@gmail.com
- **GitHub**: https://github.com/umaalugubilli/Telugu-Speech-Recogniser-API.git

