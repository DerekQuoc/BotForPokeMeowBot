import discord
from DiscordMessenger import Messenger
from PokeMeowLogic import getResponse

class MyClient(discord.Client):
    pokeMeow = 'PokéMeow#6691'
    messageSender = 0

    async def on_ready(self):
        print("logged on as {0}!".format(self.user))
        self.messageSender = Messenger()
    
    async def on_message(self, message):
        if str(message.author) == str(self.pokeMeow):
            print("got a pokemeow message!")
            response = getResponse(message.content)
            self.messageSender.send(response)
        else:
            print("got a NON-pokemeow message!")

bot = MyClient()
bot.run('NzM0NjU2NDc4NTIyMTE0MTE5.XxYYTg.NQA4LIZVOtn3pkYSYLBKMFzbMsw')