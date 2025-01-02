from pydantic import BaseModel
from datetime import datetime

class TranslationHistory(BaseModel):
    """
    Model for storing translation history.
    """
    source_text: str
    translated_text: str
    timestamp: datetime
    