import asyncio
import json, os
from pyrogram import Client, enums
#loads config

#workdir = 'session/'disconect
async def main():
     config = (json.load(open("config.json")))
     for account in config["accounts"]:
        phone = account ["phone"]
        async with Client(phone, workdir="session") as app:
            print( phone, "is logined") if await app.get_me() else print(phone, "login failed")
            async for dialog in app.get_dialogs():
                print(dialog.chat.first_name or dialog.chat.title)
            
            

            
asyncio.run(main())
