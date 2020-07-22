import discord
import time
import datetime
from DiscordMessenger import Messenger
from PokeMeowLogic import PokeMeowBotLogic

class MyClient(discord.Client):
    pokeMeow = 'PokéMeow#6691'
    logicBot = 0
    messageSender = 0

    wakeup = time.time()




    async def on_ready(self):
        print("logged on as {0}!".format(self.user))
        self.messageSender = Messenger()
        self.logicBot = PokeMeowBotLogic()
        response = self.logicBot.StartUp()
        self.messageSender.send(response)
    





    async def on_message(self, message):

        if str(message.author) == str(self.pokeMeow):
            embedded = [str(embed.to_dict()) for embed in message.embeds]
            time.sleep(5)

            self.wakeup = time.time()

             # embedded message
            if len(embedded) != 0:
                response = self.logicBot.GetResponse(embedded[0])

            # regular text
            else:
                response = self.logicBot.GetResponse(str(message.content))
            self.messageSender.send(response)



    
    async def Reboot_Message(self):
        while True:
            self.wakeup += 11
            for i in range(12):
                time.sleep(1)
                print(i)
                if time.time() > self.wakeup:
                    self.messageSender.send(";p")


        
        
            



                



            


            #if logicBot.UnknownMessage == True:

            # file = open("rawBotInput.txt", 'w', encoding="utf-8")
            # file.writelines(response)







bot = MyClient()
bot.run('NzM0NjU2NDc4NTIyMTE0MTE5.XxZwpg.ZR3Fz7dJQw6MLPFkmISthwYpf2Y')