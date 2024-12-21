import requests
import os

hf_key = os.getenv('HF_kEY')

API_URL = "https://api-inference.huggingface.co/models/Salesforce/blip-image-captioning-base"
headers = {"Authorization": f"Bearer {hf_key}"}

def query(filename):
    print(hf_key)
    with open(filename, "rb") as f:
        data = f.read()
    response = requests.post(API_URL, headers=headers, data=data)
    return response.json()
