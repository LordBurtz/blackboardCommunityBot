#!/usr/bin/python3

#bot.py

import os, discord, re
from dotenv import load_dotenv
from api import DSBApi

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
GUILD = os.getenv("DISCORD_GUILD")
IDENT = os.getenv("IDENTIFIER")

ident = re.compile(IDENT)

dsbclient = DSBApi("290142", "GyDo2021")

class bbcClient(discord.Client):
    async def on_ready(self):
        print(f'{self.user} has connected to discord.com')
    
    async def on_message(self, message):
        if message.author == self.user:
            return
        if ident.search(message.content):
            if re.compile("entries").search(message.content):
                entries = dsbclient.fetch_entries()
                for entry in entries:
                    print(entries)

            else:
                await message.channel.send('me')

client = bbcClient()
client.run(TOKEN)
