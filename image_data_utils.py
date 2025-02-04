import os
import requests
from pathlib import Path


def get_folder_image():
    folder_path = Path("images")
    folder_path.mkdir(parents=True, exist_ok=True)
    return folder_path


def save_image(url, path, filename, payload=None):
    response = requests.get(url, payload)
    response.raise_for_status()
    image_path_filename = path / filename
    with open(image_path_filename, 'wb') as file:
        file.write(response.content)
    return image_path_filename


def get_url_image():
    image_extensions = ('.png', '.jpg', '.jpeg', '.gif', '.bmp')
    image_files = []
    for _, _, files in os.walk(get_folder_image()):
        for file in files:
            if file.lower().endswith(image_extensions):
                image_files.append(file)
    return image_files

