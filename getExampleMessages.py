# run this script with the correct token
# whenever pokemeow sends a message, it will be saved to rawText.txt

import discord

class MyClient(discord.Client):
    pokeMeow = 'PokéMeow#6691'

    async def on_ready(self):
        print("logged on as {0}!".format(self.user))
        print(self.pokeMeow)
    
    async def on_message(self, message):
        if str(message.author) == str(self.pokeMeow):
            print("got a pokemeow message!")
            print("user = " + str(message.author))

            embedded = [str(embed.to_dict()) for embed in message.embeds]

            if len(embedded) != 0:
                text = embedded[0]
            else:
                text = str(message.content)

            file = open("rawText.txt", 'w', encoding="utf-8")
            file.writelines(text)


bot = MyClient()
bot.run('NzM0NjU2NDc4NTIyMTE0MTE5.XxZwpg.ZR3Fz7dJQw6MLPFkmISthwYpf2Y')