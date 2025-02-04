import os
import random
import time
import telegram
from dotenv import load_dotenv
from image_data_utils import get_url_image


def stop_time(default=14400):
    duration_time = os.environ["DURATION_TIME"]
    if duration_time == "":
        duration_time = default
        return duration_time
    else:
        return int(duration_time)


def upload_endless_image(bot, chat_id, image_files, time_pause):
    while True:
        for image in image_files:
            with open(f'images/{image}', 'rb') as file:
                bot.send_document(chat_id=chat_id, document=file)
            time.sleep(time_pause)
        random.shuffle(image_files)


def main():
    load_dotenv()
    chat_id = os.environ["TELEGRAM_CHAT_ID"]
    bot = telegram.Bot(token=os.environ["TELEGRAM_BOT_TOKEN"])
    image_files = get_url_image()
    time_pause = stop_time()
    upload_endless_image(bot, chat_id, image_files, time_pause)


if __name__ == "__main__":
    main()

