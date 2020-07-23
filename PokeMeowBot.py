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
    userName = "tomeypurkle"
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

# need to move startup message down
    async def on_message(self, message):
        if str(message.content) == self.initialMessage:
            self.userMention = (message.author.mention)

        if str(message.author) == str(self.pokeMeow):
            embedded = [str(embed.to_dict()) for embed in message.embeds]


            #need to take both embedded and not embedded to know message type
            if len(embedded) != 0:
                    embeddedText = (embedded[0])
            else:
                    embeddedText = ""
            
            normalText = str(message.content)

            if self.usernameInMessage(normalText) or self.usernameInMessage(embeddedText):
                if "are you there" in str(message.content) or "incorrect response" in str(message.content):
                    self.Captcha = True
                    response = input()
                    self.send(response)
                    self.Captcha = False
                    return

                if embedded != "":
                    response = self.logicBot.GetResponse(embeddedText)
                else:
                    response = self.logicBot.GetResponse(normalText)

                if response:
                    self.lastMessage = response
                    if ";" in response:
                        waitTime = 12
                    else:
                        waitTime = 5

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
        return self.userName in text or self.userMention in text
 

try:
    f = open("token.txt", "r")
    token = f.readline()
    f.close()
    bot = MyClient()
    bot.run(token)
except:
    print("Couldn't get the token from \'token.txt\'!")
