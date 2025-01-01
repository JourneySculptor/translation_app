import requests

# Set the URL and token
url = "http://127.0.0.1:8000/translation/translate"
headers = {
    "accept": "application/json",
    "Authorization": "Bearer <YOUR_ACCESS_TOKEN>",  # Replace <YOUR_ACCESS_TOKEN> with your actual token
    "Content-Type": "application/json",
}

# Define the payload
payload = {
    "text": "花",
    "target_language": "en"
}

# Send the POST request
response = requests.post(url, json=payload, headers=headers)

# Print the response
if response.status_code == 200:
    print("Translation Successful!")
    print(response.json())
else:
    print(f"Error: {response.status_code}")
    print(response.text)
