import os
import requests
def download_image(image_url, folder_path='temp'):
 
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    file_extension = os.path.splitext(image_url.split('/')[-1])[-1]
    
    file_name = os.path.join(folder_path, f"file{file_extension}")
    response = requests.get(image_url, stream=True)
    if response.status_code == 200:
        with open(file_name, 'wb') as file:
            for chunk in response.iter_content(1024):
                file.write(chunk)
        print(f"Image successfully downloaded: {file_name}")
        return file_name
    else:
        print("Error downloading the image.")
        return None

def process_image(image_path):
    print(f"Processing image at {image_path}...")

def delete_image(image_path):
    if os.path.exists(image_path):
        os.remove(image_path)
        print(f"Image deleted: {image_path}")
    else:
        print("Image not found.")