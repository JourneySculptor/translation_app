from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel
from auth import auth_router, get_current_user, User
from utils.translate import translate_text

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
        result = translate_text(request.text, request.target_language)
        return {"translated_text": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Translation failed: {str(e)}")
