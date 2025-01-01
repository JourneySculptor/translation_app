
# Translation API

**A FastAPI-based translation service** powered by Google Cloud Translation API. This project demonstrates expertise in **API development**, **cloud integration**, and **backend engineering**—tailored for professional portfolios and global job applications.

---

## Overview

The **Translation API** enables seamless text translation with:
- **Language Detection**: Automatically identifies the source language.
- **Text Translation**: Converts text into the specified target language.
- **Error Handling**: Provides clear responses for invalid or unsupported requests.

This project showcases proficiency in:
- Developing RESTful APIs using FastAPI.
- Integrating Google Cloud services.
- Deploying high-performance applications.

---

## Project Structure

```
translation_app/
├── main.py                      # Main application file
├── auth.py                      # Authentication and JWT logic
├── models/                      # Pydantic models for API and user handling
│   ├── user_model.py            # User and UserInDB models
│   ├── token.py                 # Token models
├── routes/                      # Application routes
│   ├── translation.py           # Translation API logic
│   ├── user.py                  # User-related API routes
├── utils/                       # Utility functions and helpers
│   ├── translate.py             # Google Translate integration
├── .env                         # Environment variables
├── .gitignore                   # Ignored files for Git
├── README.md                    # Project documentation
├── requirements.txt             # Dependencies
├── service-account-key.json     # GCP credentials file (ignored in Git)
└── request_translation.py       # Script for testing the API
```

---

## Features

- **Effortless Translation**: Supports multiple languages for accurate translation.
- **Source Language Detection**: No need to specify the input language—it’s auto-detected.
- **Developer-Friendly Interface**: Explore endpoints via Swagger UI.
- **Robust Error Management**: Ensures smooth operation with meaningful error messages.

---

## Tech Stack

- **FastAPI**: A fast and modern Python web framework.
- **Google Cloud Translation API**: Industry-leading translation capabilities.
- **Python-dotenv**: Secure management of environment variables.
- **Uvicorn**: ASGI server for high-speed API hosting.

---

## API Endpoints

### Translate Text
- **URL**: `/translation/translate`
- **Method**: `POST`
- **Request Body**:
  ```json
  {
    "text": "Hello, world!",
    "target_language": "es"
  }
  ```
- **Response Example**:
  ```json
  {
    "translated_text": "¡Hola Mundo!",
    "source_language": "en"
  }
  ```

---

## Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/translation_app.git
cd translation_app
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Configure Google Cloud API
- Enable the **Google Cloud Translation API** in your GCP project.
- Create and download a **service account key** JSON file.
- Save the file in the project directory as `service-account-key.json`.

### 4. Run the Application
```bash
uvicorn main:app --reload
```

### 5. Explore the API
- Visit the **Swagger UI** at `http://127.0.0.1:8000/docs` for interactive testing.

---

## Future Improvements

This project is ready for real-world deployment and can be further enhanced:
- **Authentication**: Add user login and token-based security.
- **Docker Integration**: Simplify deployment and scaling.
- **Batch Processing**: Support translation of multiple texts in a single request.
- **Speech-to-Text Integration**: Extend functionality with audio processing.

---

## Why This Project?
- Built with a **clean and scalable architecture** to impress potential employers.
- Demonstrates **practical use of cloud services** and cutting-edge technology.
- Designed to highlight **core API development skills** required for modern backend engineering roles.

---

## Contact

For inquiries or collaboration opportunities, connect with me on [LinkedIn](https://www.linkedin.com/in/yuka-yamaguchi-214290342).

---

## License
MIT License
