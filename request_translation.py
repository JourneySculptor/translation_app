import requests

# API server base URL
BASE_URL = "http://127.0.0.1:8000"

# Test login endpoint
def test_login():
    """
    Test the login endpoint to get a JWT token.
    """
    url = f"{BASE_URL}/auth/login"
    payload = {"username": "testuser", "password": "password"}
    response = requests.post(url, data=payload)  
    print("Login Test Response:", response.json())
    assert response.status_code == 200  
    assert "access_token" in response.json() 
    return response.json()["access_token"]  

# Test translation endpoint
def test_translate(token):
    """
    Test the translation endpoint using the provided JWT token.
    """
    url = f"{BASE_URL}/translation/translate"
    headers = {"Authorization": f"Bearer {token}"}
    payload = {"text": "花", "target_language": "en"}
    response = requests.post(url, headers=headers, json=payload)
    print("Translate Test Response:", response.json())
    assert response.status_code == 200  # Status check
    assert "translated_text" in response.json()  # Translation result

# Test clear history endpoint
def test_clear_history(token):
    """
    Test the clear history endpoint using the provided JWT token.
    """
    url = f"{BASE_URL}/history/clear-history"
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.delete(url, headers=headers)
    print("Clear History Test Response:", response.json())
    assert response.status_code == 200  # Status check
    assert response.json()["message"] == "All translation history has been cleared."

# Run all tests
if __name__ == "__main__":
    # Get a valid token
    access_token = test_login()
    
    # Test translation with the token
    test_translate(access_token)
    
    # Test clearing history with the token
    test_clear_history(access_token)
