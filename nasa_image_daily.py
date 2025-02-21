import os
import requests
import argparse
import urllib.parse
from dotenv import load_dotenv
from image_data_utils import get_folder_image, save_image


def separate_extension(url):
    parsed_url = urllib.parse.urlsplit(url)
    extension = os.path.splitext(parsed_url.path)
    return extension[1]


def fetch_nasa_daily_photo(path, count, api_key):
    nasa_daily_url = "https://api.nasa.gov/planetary/apod"
    payload = {"api_key": api_key, "count": count}
    response = requests.get(nasa_daily_url, params=payload)
    response.raise_for_status()
    for index, images in enumerate(response.json()):
        image_url = images["url"]
        extension = separate_extension(images["url"])
        filename = f"nasa_apod_{index}{extension}"
        save_image(image_url, path, filename)


def main():
    load_dotenv()
    parser = argparse.ArgumentParser(description="Загружает ежедневные фото.")
    parser.add_argument("count", help="количество снимков которое нужно получить", nargs="?", default="1", type=str)
    args = parser.parse_args()
    api_key = os.environ["NASA_API_TOKEN"]
    fetch_nasa_daily_photo(get_folder_image(), args.count, api_key)


if __name__ == "__main__":
    main()
