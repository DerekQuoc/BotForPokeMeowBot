# this file is where all the game-playing logic goes

#1.Request a pokemon encounter
    #a send ;p message every 7-20seconds (rand)
#2. Find/verify response message
#3.Check if there is bot check message and respond if not
    #3.Respond with appropriate ball
#4.Check amount of balls and restock if necessary
    #a reading amount of balls
    #b using buy command knowing how much each ball costs

def getResponse(message):
    # message is a string with the last message from pokemeow
    # return a string that you wish to send in response
    return "wow!"