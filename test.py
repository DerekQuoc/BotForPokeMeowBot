import time
MESSAGE = 0
InitialMessage = ""
message = "Hey there 12,34 I love you"
MessageStart = message.find("there") + 5
MessageEnd = message.find("I love you")
MessageStr = message[MessageStart:MessageEnd]
print(MessageStr)
for word in MessageStr:
    if word.isdigit():
        InitialMessage = InitialMessage + word
MESSAGE = int(InitialMessage)
print(MESSAGE)
        
wakeup = time.time()
print(wakeup)
while True:
    wakeup += 11
    for i in range(11):
        time.sleep(1)
        print(i)
        if time.time() > wakeup:
            print(";p")
            return

wakeup = time.time()
print(wakeup)