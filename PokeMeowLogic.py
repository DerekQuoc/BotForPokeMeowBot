class PokeMeowBotLogic():
    Coins = 0
    Pokeballs = 0
    Greatballs = 0
    Ultraballs = 0
    Masterballs = 0

    NumEggs = 0
    AddEgg = False

    NeedQuest = False

    UnknownMessage = False


    def StartUp(self):
        return ";inv"

    def ConstructInv(self, message):
        InitialCoins = ""
        CoinLocationStart = message.find("n<:PokeCoin:666879070650236928>") +len("n<:PokeCoin:666879070650236928>")-1
        CoinLocationEnd = message.find("**x PokeCoins")
        CoinStr = message[CoinLocationStart:CoinLocationEnd]
        for word in CoinStr:
            if word.isdigit():
                InitialCoins = InitialCoins + word
        self.Coins = int(InitialCoins)
        print(self.Coins)

        InitialPB = ""
        PBallLocationStart = message.find("pokeball:671848138935500836>") + len("pokeball:671848138935500836>") -1
        PBallLocationEnd = message.find ("*x Pokeballs")
        PBallStr = message[PBallLocationStart:PBallLocationEnd]
        for word in PBallStr:
            if word.isdigit():
                InitialPB = InitialPB + word
        self.Pokeballs = int(InitialPB)
        print(self.Pokeballs)

        InitialGB = ""
        GBallLocationStart = message.find("greatball:671848794823852032>") + len("greatball:671848794823852032>") -1
        GBallLocationEnd = message.find ("**x Greatballs")
        GBallStr = message[GBallLocationStart:GBallLocationEnd]
        for word in GBallStr:
            if word.isdigit():
                InitialGB = InitialGB + word
        self.Greatballs = int(InitialGB)
        print(self.Greatballs)

        InitialUB = ""
        UBallLocationStart = message.find("ultraball:671849433419481119>") + len("ultraball:671849433419481119>") - 1
        UBallLocationEnd = message.find("*x Ultraballs")
        UBallStr = message[UBallLocationStart:UBallLocationEnd]
        for word in UBallStr:
            if word.isdigit():
                InitialUB = InitialUB + word
        self.Ultraballs = int(InitialUB)
        print(self.Ultraballs)

        InitialMB = ""
        MBallLocationStart = message.find("masterball:671850509879083020>") +len("masterball:671850509879083020>") -1
        MBallLocationEnd = message.find("*x Masterballs")
        MBallStr = message[MBallLocationStart:MBallLocationEnd]
        for word in MBallStr:
            if word.isdigit():
                InitialMB = InitialMB + word
        self.Masterballs = int(InitialMB)
        print(self.Masterballs)

        InitialEgg =""
        EggLocationStart = message.find("685341229587890208>") +len("685341229587890208>") -1
        EggLocationEnd = message.find("*x Eggs")
        EggStr = message[EggLocationStart:EggLocationEnd]
        for word in EggStr:
            if word.isdigit():
                InitialEgg = InitialEgg + word
        self.NumEggs = int(InitialEgg)
        print(self.NumEggs)

        

    def UpdateEgg(self, message):
        if "you're now holding an egg" in message:
            self.AddEgg = False
            self.NumEggs -= 1

        #print out eggs
        
    def UpdateBalls(self, message):
        print("updating inventory")
        NumBalls = ""
        NumLocationStart = message.find("bought") + len("bought") - 1
        NumLocationEnd = message.rfind("x")
        NumStr = message[NumLocationStart:NumLocationEnd]
        for word in NumStr:
            if word.isdigit():
                NumBalls = NumBalls + word
        NumBalls = int(NumBalls)

        if "pokeball" in message:
            self.Coins = self.Coins - 200*NumBalls
            self.Pokeballs += NumBalls

        elif "greatball" in message:
            self.Coins = self.Coins - 500*NumBalls
            self.Greatballs += NumBalls

        elif "ultraball" in message:
            self.Coins = self.Coins - 1500*NumBalls
            self.Ultraballs += NumBalls
        
        elif "masterball" in message:
            self.Coins = self.Coins - 100000*NumBalls
            self.Masterballs += NumBalls

        print("Coins = "        + str(self.Coins))
        print("Pokeballs = "    + str(self.Pokeballs))
        print("Greatballs = "   + str(self.Greatballs))
        print("Ultraballs = "   + str(self.Ultraballs))
        print("Masterballs = "  + str(self.Masterballs))


    def NeedBall(self):
        return ((self.Pokeballs == 0 and self.Coins >200) or (self.Greatballs == 0 and self.Coins > 500) or (self.Ultraballs == 0 and self.Coins > 1500) or (self.Masterballs == 0 and self.Coins >200000))

    def BuyBall(self):
        #remove coin check and instead buy up to maximum set 
        
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

        if  self.Masterballs == 0:
            return ";shop buy 4 1"


    def HatchableEgg(self):
        if self.NumEggs > 0:
            self.AddEgg = True
        return ";egg hatch"

    def AddQuest(self):
        self.NeedQuest = True
        
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
            # returning False = "don't send a response to this message"
            return False

        if "you bought" in message:
            self.UpdateBalls(message)
            # returning False = "don't send a response to this message"
            return False

        if "you're now holding an egg" in message:
            self.UpdateEgg(message)

        if "A wild Pokemon" in message:
            return self.GottaCatchEmAll(message)
        
        if "Your egg is ready to hatch" in message:
            return self.HatchableEgg()

        if "completed the quest" in message:
            self.AddQuest()

        if "Complete your quests" in message:
            self.NeedQuest = False

        if self.NeedQuest == True:
            return ";quest"

        if  self.AddEgg == True:
            return ";egg hold"

        return ";p"



        #quest
        #hunt
        #hatchable egg


        