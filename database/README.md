# database.py

このモジュールは保存や読み取りをかんたんにするためのやつです。

## 使い方
```py
import database
import discord

client=discord.Client()

@client.event
async def on_ready():
  print("botが起動しました
