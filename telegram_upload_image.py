import os
import random
import telegram
import argparse
from dotenv import load_dotenv
from image_data_utils import get_url_image


def main():
    load_dotenv()
    chat_id = os.environ["TELEGRAM_CHAT_ID"]
    bot = telegram.Bot(token=os.environ["TELEGRAM_BOT_TOKEN"])
    random_image = random.choice(get_url_image())
    parser = argparse.ArgumentParser()
    parser.add_argument("name_image", help="название картинки", nargs="?", default=random_image, type=str)
    args = parser.parse_args()
    with open(f'images/{args.name_image}', 'rb') as file:
        bot.send_document(chat_id=chat_id, document=file)


if __name__ == "__main__":
    main()
