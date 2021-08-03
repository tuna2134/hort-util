# このモジュールは簡単にデータベースに保存したり読み取ったりするやつです。
from motor import motor_asyncio as motor

dbclient = motor.AsyncIOMotorClient("mongodbのurl")
db = dbclient["myFirstDatabase"]
db = db.guild

class database:
  async def read(self, guildid):
    data=await db.find_one({
      "guildid": int(guildid)
    })
    if data is None:
      await db.insert_one({
        "guildid": int(guildid)
      })
      data["guildid"]=int(guildid)
    return data
    
  async def write(self, guildid, data):
    await db.replace_one({
      "guildid": int(guildid)
    }, data)
