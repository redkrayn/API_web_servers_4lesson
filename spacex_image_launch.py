import requests
import argparse
from image_data_utils import get_folder_image, save_image


def fetch_spacex_last_launch(launch_id, path):
    spacex_url = f"https://api.spacexdata.com/v5/launches/{launch_id}"
    response = requests.get(spacex_url)
    response.raise_for_status()
    images_launch = response.json().get("links").get("flickr").get("original")
    for index, image in enumerate(images_launch):
        filename = f"spacex_{index}.jpeg"
        save_image(image, path, filename)


def main():
    parser = argparse.ArgumentParser(description="Загружает изображения последнего запуска SpaceX.")
    parser.add_argument("launch_id", help="вставьте id запуска, иначе defalut", nargs="?", default="latest")
    args = parser.parse_args()
    launch_id = args.launch_id
    fetch_spacex_last_launch(launch_id, get_folder_image())


if __name__ == "__main__":
    main()
