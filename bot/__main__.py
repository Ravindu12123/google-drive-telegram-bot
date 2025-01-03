import os
import logging
from pyrogram import Client
from bot import (
  APP_ID,
  API_HASH,
  BOT_TOKEN,
  DOWNLOAD_DIRECTORY
  )
import time
import requests

# Sync time with an external NTP server (optional)
def sync_time():
    try:
        response = requests.get("http://worldtimeapi.org/api/timezone/Etc/UTC")
        current_time = response.json()["unixtime"]
        time_diff = current_time - int(time.time())
        if abs(time_diff) > 5:
            print(f"Time difference: {time_diff}s, syncing time...")
            time.sleep(time_diff)
    except Exception as e:
        print(f"Failed to sync time: {e}")

sync_time()

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
LOGGER = logging.getLogger(__name__)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


if __name__ == "__main__":
    if not os.path.isdir(DOWNLOAD_DIRECTORY):
        os.makedirs(DOWNLOAD_DIRECTORY)
    plugins = dict(
        root="bot/plugins"
    )
    app = Client(
        "RXG-DriveBot",
        bot_token=BOT_TOKEN,
        api_id=APP_ID,
        api_hash=API_HASH,
        plugins=plugins,
        parse_mode="markdown",
        workdir=DOWNLOAD_DIRECTORY
    )
    LOGGER.info('Starting Bot !')
    app.run()
    LOGGER.info('Bot Stopped !')
