from pydantic import BaseModel
from typing import List

class BatchTranslationRequest(BaseModel):
    """
    Model for handling batch translation requests.
    """
    texts: List[str]  
    target_language: str  

    