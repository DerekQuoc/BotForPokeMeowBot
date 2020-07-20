# this program tests that the discord package is installed correctly
# should output nothing

import discord

class MyClient(discord.Client):
    async def on_ready(self):
        print("logged on as {0}!".format(self.user))
    
    async def on_message(self, message):
        print("Message from {0.author}: {0.content}".format(message))

client = MyClient()
# when we get a server set up with our bot connected, the following line will attach it:
#client.run('TOKEN')