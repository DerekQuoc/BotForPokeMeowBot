# this file is where all the game-playing logic goes

#1.Request a pokemon encounter
    #a send ;p message every 7-20seconds (rand)
#2. Find/verify response message
#3.Check if there is bot check message and respond if not
    #3.Respond with appropriate ball
#4.Check amount of balls and restock if necessary
    #a reading amount of balls
    #b using buy command knowing how much each ball costs
class PokeMeowBotLogic():
    RebuyPokeball = False
    RebuyGreatball = False
    RebuyUltraballs = False
    RebuyMasterballs = False

    def buyBall(self):
        if self.RebuyPokeball == True:
            return ";shop buy pokeball VarNum"
        if self.RebuyGreatball == True:
            return ";shop buy greatball VarNum"


    def getResponse(self, message):
        if "Pokeballs: 1 " in message:
            self.RebuyPokeballs = True
        if "Greatballs: 1 " in message:
            self.RebuyGreatballs = True
        if "Ultraballs: 1 " in message:
            self.RebuyUltraballs = True
        if "Masterballs: 1 " in message:
            self.RebuyMasterballs = True

        if "Common" in message:
            return "pb"
        if "Uncommon" in message:
            return "pb"
        if "Rare" in message:
            if "Super" in message:
                return "ub"
            else:
                return "gb"
        if "Legendary" in message:
            return "mb"
        else:
            return "ub"