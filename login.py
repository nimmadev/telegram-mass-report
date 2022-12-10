import asyncio
import json
import re
from pyrogram import Client, errors


# load config
config = (json.load(open("config.json")))
# group target link
group_target_id = input('group_source_username or link to join for report')
gi = re.sub("(@)|(https://)|(http://)", "", group_target_id)
#workdir = 'session/'


def main():
    for account in config["accounts"]:
        phone = account["phone"]
        api_id = account["api_id"]
        api_hash = account["api_hash"]
        print(phone)
        with Client(phone, api_id, api_hash, workdir="session") as app:
            if app.get_me():
                print(phone, "is logined")
                try:
                    app.join_chat(gi)
                except errors.UserAlreadyParticipant:
                    app.get_chat(gi)
                except:
                    print("couldnt join chat")
            else:
               print(phone, "login failed")
main()
