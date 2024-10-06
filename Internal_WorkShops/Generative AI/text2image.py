import requests
import io
from PIL import Image

# Replace 'your-api-key' with the actual API key you generated
API_URL = "https://api-inference.huggingface.co/models/black-forest-labs/FLUX.1-dev"
headers = {"Authorization": "Bearer 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"}

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    
    if response.status_code == 200:
        if 'application/json' in response.headers['Content-Type']:
            print("Received JSON response:")
            print(response.json())
        else:
            return response.content  # Return image bytes if it's valid image data
    else:
        print(f"Error: Received status code {response.status_code}")
        print(response.text)  # Print error message for debugging
        return None

# Make the API call
image_bytes = query({
    "inputs": "astronaut riding horse",
})

if image_bytes:
    try:
        image = Image.open(io.BytesIO(image_bytes))
        image.show()
    except Exception as e:
        print(f"Failed to open the image: {e}")
else:
    print("No image data received.")
