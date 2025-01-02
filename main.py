from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel
from auth import auth_router, get_current_user, User
from utils.translate import translate_text
from models.history_model import TranslationHistory  
from services.history_service import save_history, get_history  
from datetime import datetime, timezone

# Initialize FastAPI app
app = FastAPI()

# Include authentication router
app.include_router(auth_router)

# Request model for translation
class TranslationRequest(BaseModel):
    text: str
    target_language: str

# Translation endpoint
@app.post("/translation/translate")
async def translate_endpoint(
    request: TranslationRequest,
    current_user: User = Depends(get_current_user)
):
    """
    Translate the given text into the target language. Requires authentication.
    """
    try:
        # Call the translation service
        result = translate_text(request.text, request.target_language)
        
        # Save the translation history
        history = TranslationHistory(
            source_text=request.text,
            translated_text=result,  # Ensure translated_text is properly assigned
            timestamp=datetime.now(timezone.utc)
        )
        save_history(history)
        
        return {"translated_text": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Translation failed: {str(e)}")


# Save translation history endpoint
@app.post("/save-history/")
async def save_translation_history(source_text: str, translated_text: str):
    """
    Save a translation history entry.
    """
    history = TranslationHistory(
        source_text=source_text,
        translated_text=translated_text,
        timestamp=datetime.utcnow()
    )
    save_history(history)
    return {"message": "History saved successfully"}

# Retrieve translation history endpoint
@app.get("/get-history/")
async def retrieve_history():
    """
    Retrieve all saved translation history entries.
    """
    return get_history()


