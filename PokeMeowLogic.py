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
    Pokeballs = 0
    Greatballs = 0
    Ultraballs = 0
    Masterballs = 0

    NumEggs = 0
    HatchableEgg = False
    NeedNewEgg = False
    

    Coins = 0

    def StartUp(self):
        return ";inv"

    def ConstructInv(self, message):
        

    def NeedBall(self):

        return (PokeBalls == 0 or Greatballs == 0 or Ultraballs == 0 or Masterballs == 0)

    def BuyBall(self):

        if self.Pokeballs == 0:
            if self.Coins > 10000:
                return ";shop buy 1 50"
            else:
                return ";shop buy 1 1"

        if self.Greatballs == 0:
            if self.Coins > 15000:        
                return ";shop buy 2 30"
            else:
                return ";shop buy 2 1"

        if self.Ultraballs == 0:
            if self.Coins > 7500:
                return ";shop buy 3 5"
            else:
                return ";shop buy 3 1"

        if  self.Masterballs == 0 and self.Coins > 300000:
            return ";shop buy 4 1"
        else:
            return ";p"
        
    def GottaCatchEmAll(self, message):
        if "Common" in message:
            self.Pokeballs -= 1
            return "pb"

        if "Uncommon" in message:
            self.Pokeballs -= 1
            return "pb"

        if "Rare" in message:
            if "Super" in message:
                self.Ultraballs -= 1
                return "ub"
            else:
                self.Greatballs -= 1
                return "gb"

        if "Legendary" in message:
            self.Masterballs -= 1
            return "mb"

        else:
            self.Ultraballs -= 1
            return "ub"

    def GetResponse(self, message):
        if "item inventory" in message:
            self.ConstructInv(message)

        if "you bought" in message:
            self.UpdateInv(message)
            return ";p"

        if self.NeedBall():
            BuyBall()

        if "A wild Pokemon":
            return self.GottaCatchEmAll(message)
        else
            return ";p"

        #quest
        #hunt
        #hatchable egg


        