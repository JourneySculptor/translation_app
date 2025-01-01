# User endpoint for managing user-related information
from fastapi import APIRouter, Depends
from auth import get_current_active_user
from models.user_model import User

# Create a router for the user endpoint
router = APIRouter()

# GET endpoint for retrieving current user details
@router.get("/users/me", response_model=User)
def get_me(current_user: User = Depends(get_current_active_user)):
    return current_user
