from datetime import datetime, timedelta, timezone
from jose import JWTError, jwt
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm, HTTPBearer
from pydantic import BaseModel

# Create a router for authentication routes
auth_router = APIRouter()

# Secret key and algorithm for JWT
SECRET_KEY = "your-secret-key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 15

# Define the token scheme
bearer_scheme = HTTPBearer()

# Dummy user database for testing purposes
fake_users_db = {
    "testuser": {
        "username": "testuser",
        "password": "password"
    }
}

# Define models for user and token
class User(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

# Validate user credentials against the dummy database
def authenticate_user(username: str, password: str):
    """
    Validate user credentials against the dummy database.
    """
    user = fake_users_db.get(username)
    if user and user["password"] == password:
        return User(username=username, password=user["password"])
    return None

# Generate a JWT token with an expiration time
def create_access_token(data: dict, expires_delta: timedelta | None = None):
    """
    Generate a JWT token with an expiration time.
    """
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + (expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire})
    print(f"Token payload: {to_encode}")  # Debugging
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

# Decode the JWT token and extract user information
async def get_current_user(token: str = Depends(bearer_scheme)):
    """
    Decode the JWT token and extract user information.
    """
    try:
        # Debug: Print the received token
        print(f"Received token: {token.credentials}")
        
        # Decode the token to extract payload
        payload = jwt.decode(token.credentials, SECRET_KEY, algorithms=[ALGORITHM])
        
        # Extract username from payload
        username = payload.get("sub")
        
        # Debug: Print the decoded username
        print(f"Decoded username: {username}")
        
        if not username:
            raise HTTPException(status_code=401, detail="Token missing username")
        
        # Return the authenticated user
        return User(username=username, password="not_returned")
    except JWTError as e:
        # Debug: Print the JWT error
        print(f"JWT error: {e}")
        raise HTTPException(status_code=401, detail=f"Invalid token: {str(e)}")

# Login endpoint to authenticate the user and return a JWT token
@auth_router.post("/auth/login")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    """
    Authenticate the user and return an access token.
    """
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid username or password")
    access_token = create_access_token(
        data={"sub": user.username},
        expires_delta=timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    )
    return {"access_token": access_token, "token_type": "bearer"}

# A protected route that requires a valid JWT token
@auth_router.get("/auth/protected")
async def protected_route(current_user: User = Depends(get_current_user)):
    """
    A protected route that requires a valid JWT token.
    """
    return {"message": f"Welcome, {current_user.username}!"}
