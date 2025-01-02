import google.auth
from google.cloud import translate_v2 as translate

# Initialize the client
client = translate.Client()

def translate_text(text: str, target_language: str) -> str:
    """
    Translate text into the target language using Google Translate API.
    """
    try:
        # Perform the translation
        result = client.translate(text, target_language=target_language)
        # Extract translated text
        translated_text = result.get("translatedText")
        if not translated_text:
            raise ValueError("Translation result is empty")
        return translated_text
    except Exception as e:
        print(f"Translation error: {e}")  # Debugging output
        raise ValueError(f"Translation failed: {str(e)}")


