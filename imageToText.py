
import requests
import os
from dotenv import load_dotenv

load_dotenv()

# Accessing environment variables
hf_key = os.getenv('HF_KEY')

API_URL = "https://api-inference.huggingface.co/models/Salesforce/blip-image-captioning-base"
headers = {"Authorization": f"Bearer {hf_key}"}

def query(filename):
    with open(filename, "rb") as f:
        data = f.read()
    response = requests.post(API_URL, headers=headers, data=data)
    return response.json()
