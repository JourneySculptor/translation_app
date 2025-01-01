from fastapi import APIRouter, Depends
from fastapi.security import HTTPBearer
from fastapi_jwt_auth import AuthJWT
from pydantic import BaseModel

router = APIRouter()

http_bearer = HTTPBearer()

# Translation request model
class TranslationRequest(BaseModel):
    text: str
    target_language: str

@router.post("/translate", tags=["Translation"])
def translate(
    request: TranslationRequest,
    Authorize: AuthJWT = Depends()
):
    """
    Translate the given text into the target language. Requires authentication.
    """
    Authorize.jwt_required()
    current_user = Authorize.get_jwt_subject()
    translated_text = f"Translated '{request.text}' to '{request.target_language}'"
    return {"translated_text": translated_text, "requested_by": current_user}
