# Utility functions for Google Cloud Translate API
from google.cloud import translate_v2 as translate
import os

# Set up Google Translate client
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = os.path.abspath("service-account-key.json")
translate_client = translate.Client()

# Function to perform text translation
def translate_text(text: str, target_language: str):
    try:
        # Translate text
        result = translate_client.translate(text, target_language=target_language)
        # Return structured response
        return {
            "translated_text": result["translatedText"],
            "detected_source_language": result["detectedSourceLanguage"]
        }
    except Exception as e:
        # Handle errors gracefully
        print(f"Error during translation: {e}")
        return {"error": "Failed to translate text"}
