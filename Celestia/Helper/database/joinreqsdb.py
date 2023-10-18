from typing import Dict, List, Union
from config import MONGO_URL
from motor.motor_asyncio import AsyncIOMotorClient as MongoCli


mongo = MongoCli(MONGO_URL).Rankings

jreq = mongo.joinreqs




async def add_join(chat_id : int):
    return await jreq.insert_one({"chat_id" : chat_id})
    
async def rm_join(chat_id : int):   
    chat = await jreq.find_one({"chat_id" : chat_id})
    if chat: 
        return await jreq.delete_one({"chat_id" : chat_id})
