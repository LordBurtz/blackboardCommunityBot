#!/usr/bin/python3

#bot.py

import os, discord, re
from dotenv import load_dotenv
from api import DSBApi

load_dotenv()
TOKEN = os.getenv("TOKEN")
GUILD = os.getenv("GUILD")
IDENT = os.getenv("IDENTIFIER")
LOGIN=os.getenv("lgin")
PASSWORD=os.getenv("pwds")

ident = re.compile(str(IDENT))

dsbclient = DSBApi(LOGIN, PASSWORD)

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
                    if len(entry) > 999:
                        strs = splitstrings(entry)
                        for s in strs:
                            print(s)
                            print(len(s))
                            await  message.channel.send(s)
                    else:
                        print(entry)
                        await message.channel.send(entry)

            else:
                await message.channel.send('me')
    
    def splitstrings(string):
        res = []
        while len(string) > 999:
            res.append(string[:999])
            string = string[999:]

        return res

client = bbcClient()
client.run(TOKEN)



