from google.cloud import translate_v2 as translate
import os

# Set up Google Translate client
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = os.path.abspath("service-account-key.json")
translate_client = translate.Client()

# Function to perform text translation
def translate_text(text: str, target_language: str) -> str:
    """
    Translate the given text into the target language using Google Translate API.
    """
    try:
        result = translate_client.translate(text, target_language=target_language)
        
        # Ensure "translatedText" key exists in the response
        translated_text = result.get("translatedText")
        if not translated_text:
            raise ValueError("Translation API response missing 'translatedText'")
        
        return translated_text
    except Exception as e:
        raise ValueError(f"Translation API failed: {str(e)}")

