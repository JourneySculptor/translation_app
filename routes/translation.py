from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import HTTPBearer
from fastapi_jwt_auth import AuthJWT
from pydantic import BaseModel
from models.token import TokenData
from utils.translate import translate_text
from dependencies import get_current_user
from models.translation_model import BatchTranslationRequest

router = APIRouter(prefix="/translation")  # Prefix remains

http_bearer = HTTPBearer()

# Model for single translation request
class TranslationRequest(BaseModel):
    text: str
    target_language: str

# Endpoint for single translation
@router.post("/translate", tags=["Translation"])  # No need to repeat "translation"
def translate(
    request: TranslationRequest,
    Authorize: AuthJWT = Depends()
):
    """
    Translate the given text into the target language. Requires authentication.
    """
    Authorize.jwt_required()
    current_user = Authorize.get_jwt_subject()
    translated_text = translate_text(request.text, request.target_language)
    return {"translated_text": translated_text, "requested_by": current_user}

# Endpoint for batch translation
@router.post("/batch-translate", tags=["Translation"])  # Removed redundant "translation"
async def batch_translate(
    data: BatchTranslationRequest,
    Authorize: AuthJWT = Depends()
):
    """
    Translate multiple texts into the specified target language.
    """
    try:
        # Require and decode JWT token
        Authorize.jwt_required()
        current_user = Authorize.get_jwt_subject()
        print(f"Authenticated user: {current_user}")
    except Exception as e:
        print(f"Authentication error: {e}")
        raise HTTPException(status_code=401, detail=f"Authentication error: {str(e)}")
    
    # Log incoming request
    print(f"Received batch translation request: {data}")

    # Validate input
    if not data.texts or not isinstance(data.texts, list):
        raise HTTPException(status_code=400, detail="Invalid or missing 'texts' field.")
    if not data.target_language or not isinstance(data.target_language, str):
        raise HTTPException(status_code=400, detail="Invalid or missing 'target_language' field.")

    # Perform translation
    results = []
    for text in data.texts:
        try:
            translated = translate_text(text, data.target_language)
            results.append({"source_text": text, "translated_text": translated})
        except Exception as e:
            print(f"Error translating '{text}': {e}")
            results.append({"source_text": text, "error": str(e)})

    return {"translations": results, "requested_by": current_user}
