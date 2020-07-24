import discord
import asyncio
import time
import datetime
import random #use to randomize sending message timer
from DiscordMessenger import Messenger
from PokeMeowLogic import PokeMeowBotLogic

class MyClient(discord.Client):
    pokeMeow = 'PokéMeow#6691'
    logicBot = 0
    messageSender = 0
    timeOfLastSend = 0
    timeOfLastGet = 0
    lastMessage = ""
    Captcha = False
    userName = "DerekQuoc"
    userMention = ""
    initialMessage = ""


    async def on_ready(self):
        print("logged on as {0}!".format(self.user))
        self.messageSender = Messenger()
        self.logicBot = PokeMeowBotLogic()
        
        self.timeOfLastGet = time.time()
        self.timeOfLastSend = time.time()
        self.bg_task = self.loop.create_task(self.check_no_response())

        self.initialMessage = "PokeMeow Bot Running for:  " + self.userName + "!"
        self.messageSender.send(self.initialMessage)

        await asyncio.sleep(2)

        response = self.logicBot.StartUp()
        self.messageSender.send(response)


    #async def on_message_edit(self, message):

    # need to move startup message down
    async def on_message(self, message):
        if str(message.content) == self.initialMessage:
            self.userMention = str(message.author.mention)
            print(self.userMention)

        if str(message.author) == str(self.pokeMeow):

            text = str(message.content)
            embedded = [str(embed.to_dict()) for embed in message.embeds]
            
            if len(embedded) != 0:
                    text += " " + str(embedded[0])
            
            if self.usernameInMessage(text): #or (ballthrow flag == true and oh you're egg is ready to hatch! in text):
                if "are you there" in text or "incorrect response" in text:
                    print("captcha found!")
                    self.Captcha = True
                    response = input("CAPTCHA: ")
                    self.send(response)
                    self.Captcha = False
                    return

                response = self.logicBot.GetResponse(text)

                if response:
                    self.lastMessage = response
                    if ";" in response:
                        waitTime = 12
                    else:
                        waitTime = 5
                        #setflag for egg check
                    await asyncio.sleep(waitTime)
                    self.send(response)

                await asyncio.sleep(10)
                self.buyBalls()


    async def check_no_response(self):
        await self.wait_until_ready()
        while not self.is_closed():
            if self.Captcha == False:
                if ";" not in self.lastMessage:
                    waitTime = 15
                else:
                    waitTime = 20

                if time.time() - self.timeOfLastSend > waitTime:
                    print("Timeout")
                    if not self.buyBalls():
                        self.send(";p")

                await asyncio.sleep(5) # task runs every 5 seconds

    def send(self, txt):
        self.messageSender.send(txt)
        self.timeOfLastSend = time.time()

    def buyBalls(self):
        if self.logicBot.NeedBall():
                print("Need to buy a ball")
                response = self.logicBot.BuyBall()
                self.lastMessage = response
                self.send(response)


    def usernameInMessage(self, text):
        return (self.userName in text) or (self.userMention in text)
 

try:
    f = open("token.txt", "r")
    token = f.readline()
    f.close()
    bot = MyClient()
    bot.run(token)
except:
    print("Couldn't get the token from \'token.txt\'!")
