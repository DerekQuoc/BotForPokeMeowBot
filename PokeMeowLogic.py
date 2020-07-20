# this file is where all the game-playing logic goes

#1.Request a pokemon encounter
    #a send ;p message every 7-20seconds (rand)
#2. Find/verify response message
#3.Check if there is bot check message and respond if not
    #3.Respond with appropriate ball
#4.Check amount of balls and restock if necessary
    #a reading amount of balls
    #b using buy command knowing how much each ball costs
class PokeMeowBotLogic:
    def buyBall():
        if RebuyPokeball = True:
            return ";shop buy pokeball VarNum"
        if RebuyGreatball = True:
            return ";shop buy greatball VarNum"


    def getResponse(message):
        if "Pokeballs: 1 ": in message
            RebuyPokeballs = True
        if "Greatballs: 1 " in message
            RebuyGreatballs = True
        if "Ultraballs: 1 " in message
            RebuyUltraballs = True
        if "Masterballs: 1 " in message
            RebuyMasterballs = True

        if "Common" in message:
            return "pb"
        if "Uncommon" in message:
            return "pb"
        if "Rarity: Rare" in message:
            return "gb"
        if "Rarity: Super Rare" in message:
            return "ub"
        if "Legendary" in message:
            return "mb"
        else
            return "ub"
    # message is a string with the last message from pokemeow
    # return a string that you wish to send in response
    return "wow!"