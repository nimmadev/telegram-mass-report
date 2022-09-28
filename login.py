import asyncio
import json
from pyrogram import Client, errors


# load config
config = (json.load(open("config.json")))
# group target link


def main():
    for account in config["accounts"]:
        phone = account["phone"]
        api_id = account["api_id"]
        api_hash = account["api_hash"]
        print(phone)
        with Client(phone, api_id, api_hash, workdir="session") as app:
            if app.get_me():
                print(phone, "is logined")
            else:
               print(phone, "login failed")
main()
