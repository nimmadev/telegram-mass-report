from pyrogram import Client, filters
import asyncio
import json
from pyrogram.raw.functions.account import ReportPeer
from pyrogram.raw.types import *


listofchoise = ['Report for child abuse', 'Report for copyrighted content', 'Report for impersonation', 'Report an irrelevant geogroup', 'Report an illegal durg','Other', 'Report for offensive person detail', 'Reason for Pornography', 'Report for spam"']
def get_reason(text):
    if text == "Report for child abuse":
        return InputReportReasonChildAbuse()
    elif text == "Report for impersonation":
        return InputReportReasonFake()
    elif text == "Report for copyrighted content":
        return InputReportReasonCopyright()
    elif text == "Report an irrelevant geogroup":
        return InputReportReasonGeoIrrelevant()
    elif text == "Reason for Pornography":
        return InputReportReasonPornography()
    elif text == "Report an illegal durg":
        return InputReportReasonIllegalDrugs()
    elif text == "Report for offensive person detail":
        return InputReportReasonSpam()
    elif text == "Report for spam":
        return InputReportReasonPersonalDetails()

#report = app.send(report_peer)

async def main():
     config = (json.load(open("config.json")))
     #resportreason = "Report for copyrighted content"
     for x in listofchoise:
        print(x)
     resportreas = int(input("whats ur  reason: type 1-8: "))
     resportreaso = listofchoise[resportreas - 1]
     resportreason = get_reason(resportreaso)
     print("")
     print(resportreason)
     print("")
    # resportreason = input("whats ur pepoet reason: ")
     dat =  input("How do you want to report username or id: " )
     if dat.lower() == "username":
        pee = input("type username of Channel or group : ")
     elif dat.lower() == "id":
        pee = input("type id of Channel or group  without -100: ")
        pee = int(str(-100)+str(pee))
     for account in config["accounts"]:
        phone = account["phone"]
        async with Client(phone, workdir="session") as app:
            if dat.lower() == "username" or 'id':
                #await app.get_chat(-1001433138571)
                peer = await app.resolve_peer(pee)
                peer_id = peer.channel_id
                access_hash = peer.access_hash
                channel = InputPeerChannel(channel_id=peer_id, access_hash=access_hash)
            elif dat.lower() == "user":
                peer = await app.resolve_peer(pee)
                
                user_id = int(peer.user_id)
                access_hash = str(peer.access_hash)
                channel = InputPeerUser(user_id=user_id, access_hash=access_hash)
            
            report_peer = ReportPeer(
                                        peer=channel, 
                                        reason=resportreason, 
                                        message=resportreaso
                                    )

            try:
                result = await app.invoke(report_peer)
                print(result, 'reported by number', phone)
                 
            except BaseException as e:
                print(e)
                print("failed to report from :", phone)
            
                
asyncio.run(main())