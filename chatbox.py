class Personality():
    hiResponse= "🤖HELLO🤖"
    whatsUpResponse= ""
    howAreYouResponse= ""

    def processInput(self,response):
        if response == "hi":
            print(self.hiResponse)
        elif response == "Whats up?":
            print(self.whatsUpResponse)
        elif response == "How are you?":
            print(self.howAreYouResponse)
        else:
            print(self.otherResponse)
#----Define your functions below----

def intro():
    print("🤖HELLO, I AM CHATBORT 🤖")
    print("🤖LET'S TALK🤖")
    print("🤖 [INSTRUCTIONS FOR USE] 🤖")

def choosepersonality():
    print("Choose a Personality to talk to. You can choose")
    choice= input("Mean,Nice, or Nervous")
    return choice
# --- Define your functions below! ---

def main():
    userChoice= choosepersonality()
    print(userChoice)

    niceRobot= Personality()
    niceRobot.hiResponse="🤖 HI, IT'S SO NICE TO MEET YOU"
    niceRobot.whatsUpResponse="🤖 OH, I'M JUST TALKINGTO THE MOST INTERESTING PERSON"
    niceRobot.howAreYouResponse="🤖OH I'M JUST LOVELY"
    niceRobot.otherResponse="🤖I DONT UNDERSTAND"

    meanRobot=Personality()
    meanRobot.hiResponseponse="🤖CAN YOU LEAVE"
    meanRobot.whatsUpResponse="🤖DON'T SPEAK TO ME FOOL"
    meanRobot.howAreYouResponse="🤖TERRIBLE, THAT IM TALKING TO YOU"
    meanRobot.otherResponse="🤖I DONT UNDERSTAND YOUR GIBBERISH, SWINE"

    nervousRobot=Personality()
    nervousRobot.hiResponseponse="🤖  🤖 "
    nervousRobot.whatsUpResponse="🤖...UMMM HI"
    nervousRobot.howAreYouResponse="🤖NERVOUS!"
    nervousRobot.otherResponse="🤖THE WORLD IS LARGE AND CONFUSING"


    intro()
    while True:
        answer = input (("What will you say?"))
        if userChoice == "Nice":
            niceRobot.processInput(answer)

        elif userChoice =="Mean":
            meanRobot.processInput(answer)
        elif userChoice == "Nervous":
            nervousRobot.processInput(answer)

# DON'T TOUCH! Setup code that runs your main() function.
if __name__ == "__main__":
  main()
