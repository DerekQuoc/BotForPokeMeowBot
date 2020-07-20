import discord
from DiscordMessenger import Messenger
from PokeMeowResponse import getResponse

class PokeMeowBot(discord.Client):
    pokeMeow = 'PokéMeow#6691'
    messageSender = 0

    def __init__(self):
        self.messageSender = Messenger()

    async def on_ready(self):
        print("logged on as {0}!".format(self.user))
    
    async def on_message(self, message):
        if message.author == self.pokeMeow:
            response = getResponse(message.content)
            self.messageSender.send(response)

bot = PokeMeowBot()
bot.run('the bots secret token goes here!')