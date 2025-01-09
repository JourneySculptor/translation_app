from fastapi import Depends, HTTPException
from fastapi_jwt_auth import AuthJWT
from models.token import TokenData
from pydantic import BaseSettings

# Load configuration from environment variables
class Settings(BaseSettings):
    authjwt_secret_key: str  # Load the JWT secret key

@AuthJWT.load_config
def get_config():
    """
    Load JWT configuration from .env file.
    """
    return Settings()

def get_current_user(Authorize: AuthJWT = Depends()) -> TokenData:
    """
    Validate the JWT token and return the current user information.
    """
    try:
        # Validate the JWT token
        Authorize.jwt_required()

        # Extract user information (e.g., username) from the token
        current_user = Authorize.get_jwt_subject()
        if not current_user:
            raise HTTPException(status_code=401, detail="Invalid user.")
        
        return TokenData(username=current_user)
    except Exception as e:
        raise HTTPException(status_code=401, detail=f"Authentication error: {str(e)}")
