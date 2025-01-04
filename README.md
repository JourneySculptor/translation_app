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
│   ├── history_model.py         # Translation history model
├── routes/                      # Application routes
│   ├── translation.py           # Translation API logic
│   ├── user.py                  # User-related API routes
│   ├── history.py               # Clear history API routes
├── services/                    # Business logic for the application
│   ├── translate_service.py     # Google Translate integration
│   ├── history_service.py       # History management logic
├── utils/                       # Utility functions
│   ├── translate.py             # Google Translate interaction
├── Dockerfile                   # Docker configuration
├── requirements.txt             # Python dependencies
├── .gitignore                   # Files to ignore in Git
├── README.md                    # Project documentation
├── .env                         # Environment variables
├── service-account-key.json     # GCP credentials (ignored in Git)
└── request_translation.py       # Testing script
```

---

## Features

- **Effortless Translation**: Supports multiple languages for accurate translation.
- **Source Language Detection**: No need to specify the input language—it’s auto-detected.
- **Developer-Friendly Interface**: Explore endpoints via Swagger UI.
- **Robust Error Management**: Ensures smooth operation with meaningful error messages.
- **JWT Authentication**: Secure access to endpoints with token-based authentication.
- **Clear Translation History**: Easily reset all saved translation data.

---

## Tech Stack

- **FastAPI**: A fast and modern Python web framework.
- **Google Cloud Translation API**: Industry-leading translation capabilities.
- **FastAPI-JWT-Auth**: Secure and flexible JWT authentication.
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

### Save Translation History
- **URL**: `/save-history/`
- **Method**: `POST`
- **Parameters**:
  - `source_text` (string, required): The original text before translation.
  - `translated_text` (string, required): The translated text.

- **Response Example**:
  ```json
  {
    "message": "History saved successfully"
  }
  ```

### Retrieve Translation History
- **Response Example**:
  ```json
  [
    {
      "source_text": "Hello, I hope this message finds you well. I am sharing the meeting materials.",
      "translated_text": "お世話になっております。会議の資料を共有いたします。",
      "timestamp": "2025-01-02T06:11:39.753698+00:00"
    }
  ]
  ```

### Clear Translation History
- **URL**: `/history/clear-history`
- **Method**: `DELETE`
- **Description**: Deletes all saved translation history entries.
- **Response Example**:
  ```json
  {
    "message": "All translation history has been cleared."
  }
  ```

---

## Translation Examples with Screenshots

### Example 1: Translating from English to Norwegian

**Request Body**:
```json
{
  "text": "Thank you for your email. I will get back to you shortly.",
  "target_language": "no"
}
```
**Response Body**:
```json
{
  "translated_text": "Takk for e-posten din. Jeg vil kontakte deg snart."
}
```
**Screenshot**:
![English to Norwegian Translation Response](https://raw.githubusercontent.com/yourusername/translation_app/main/images/translate_example_en_no_response.png)

### Example 2: Translating from Japanese to French

**Request Body**:
```json
{
  "text": "このプロジェクトについてのご提案ありがとうございます。",
  "target_language": "fr"
}
```
**Response Body**:
```json
{
  "translated_text": "Merci pour votre proposition concernant ce projet."
}
```
**Screenshot**:
![Japanese to French Translation Response](https://raw.githubusercontent.com/yourusername/translation_app/main/images/translate_example_ja_fr_response.png)

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

### 4. Deploy to Google Cloud Run
This application is containerized and deployed on Google Cloud Run for scalable, serverless execution. Follow these steps to deploy:

1. Build the Docker image:
   ```bash
   docker build -t asia-northeast1-docker.pkg.dev/translation-app-443313/translation-repo/translation_app:latest .
   ```
2. Push the Docker image to Google Artifact Registry:
   ```bash
   docker push asia-northeast1-docker.pkg.dev/translation-app-443313/translation-repo/translation_app:latest
   ```
3. Deploy the container to Google Cloud Run:
   ```bash
   gcloud run deploy translation-app \
       --image=asia-northeast1-docker.pkg.dev/translation-app-443313/translation-repo/translation_app:latest \
       --platform=managed \
       --region=asia-northeast1 \
       --allow-unauthenticated
   ```
4. Once deployed, access the application at the provided **Service URL**:
   - [Translation App](https://translation-app-883938623305.asia-northeast1.run.app)

This deployment process demonstrates proficiency in **cloud deployment pipelines** and **serverless architecture**.

---

## Deployed URL

Access the live application: [Translation App](https://translation-app-883938623305.asia-northeast1.run.app)

---

## Future Improvements

This project is ready for real-world deployment and can be further enhanced:
- **Batch Processing**: Support translation of multiple texts in a single request.
- **Speech-to-Text Integration**: Extend functionality with audio processing.
- **Enhanced Authentication**: Implement OAuth2 for improved security.
- **Usage Analytics**: Integrate Google Analytics or a custom dashboard to track translation requests and user engagement.
- **Multi-Cloud Deployment**: Add support for other cloud platforms like AWS Lambda or Azure Functions.
- **End-to-End Tests**: Implement automated testing pipelines using Pytest or similar frameworks.

---

## Contact

For inquiries or collaboration opportunities, connect with me via:
- [LinkedIn](https://www.linkedin.com/in/yuka-yamaguchi-214290342)
- [GitHub Profile](https://github.com/JourneySculptor)

---

## License
MIT License
