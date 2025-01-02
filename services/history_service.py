from typing import List
from models.history_model import TranslationHistory

# In-memory storage for translation history(replace with a database if needed)
_translation_history_storage: List[TranslationHistory] = []

def save_history(history: TranslationHistory):
    """
    Save a translation history entry.
    """
    _translation_history_storage.append(history)

def get_history() -> List[TranslationHistory]:
    """
    Retrieve all saved translation history entries.
    """
    return _translation_history_storage


