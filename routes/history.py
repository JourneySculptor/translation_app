from fastapi import APIRouter

# Create an instance of APIRouter
router = APIRouter()

# In-memory storage for translation history
history_storage = []

@router.delete("/clear-history", summary="Clear all translation history")
async def clear_translation_history():
    """
    Endpoint to clear all translation history.
    """
    global history_storage
    history_storage = []
    return {"message": "All translation history has been cleared."}
