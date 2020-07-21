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
            embedded = [str(embed.to_dict()) for embed in message.embeds][0]
            response = self.logicBot.getResponse(embedded)
            self.messageSender.send(response)

bot = MyClient()
bot.run('NzM0NjU2NDc4NTIyMTE0MTE5.XxYmBg.lTo12m050YZdVJMc4oMnwqz5Rjo')