import discord
from DiscordMessenger import Messenger
from PokeMeowLogic import PokeMeowBotLogic

class MyClient(discord.Client):
    pokeMeow = 'PokéMeow#6691'
    logicBot = 0
    messageSender = 0

    async def on_ready(self):
        print("logged on as {0}!".format(self.user))
        self.messageSender = Messenger()
        self.logicBot = PokeMeowBotLogic()
    
    async def on_message(self, message):
        if str(message.author) == str(self.pokeMeow):
            print("got a pokemeow message!")
            response = self.logicBot.getResponse(message.content)
            self.messageSender.send(response)
        else:
            print("got a NON-pokemeow message!")

bot = MyClient()
bot.run('TOKEN')