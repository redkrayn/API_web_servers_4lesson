import os
import requests
from itertools import islice
from dotenv import load_dotenv
from image_data_utils import get_folder_image, save_image


def fetch_nasa_epic_photo(path, api_key):
    url_nasa_epic = "https://epic.gsfc.nasa.gov/api/natural"
    response = requests.get(url_nasa_epic)
    response.raise_for_status()
    for index, _ in islice(enumerate(response.json()),10):
        epic_image = response.json()[index]["image"]
        date_image = response.json()[index]["date"]
        final_date = date_image.replace('-', '/').split(' ')[0]
        url = f"https://api.nasa.gov/EPIC/archive/natural/{final_date}/png/{epic_image}.png"
        payload = {"api_key": api_key}
        filename = f"nasa_epic_{index}.png"
        save_image(url, path, filename, payload)


def main():
    load_dotenv()
    api_key = os.environ["NASA_API_TOKEN"]
    fetch_nasa_epic_photo(get_folder_image(), api_key)


if __name__ == "__main__":
    main()
