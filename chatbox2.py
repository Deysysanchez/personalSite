class Personality():
    hiResponse= "🤖HELLO🤖"
    whatsUpResponse= ""
    howAreYouResponse= ""

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
    mean= {"Hi," : "🤖CAN YOU LEAVE",
            "What's up?" : "🤖DON'T SPEAK TO ME FOOL",
            "How are you?" : "🤖TERRIBLE, THAT IM TALKING TO YOU"}
    nice= {"Hi,": "🤖 HI, IT'S SO NICE TO MEET YOU",
            "What's up?" : "🤖 OH, I'M JUST TALKINGTO THE MOST INTERESTING PERSON",
            "How are you?" : "🤖OH I'M JUST LOVELY"}
    nervous= {"Hi,": "🤖  🤖",
            "Whats' up?":"🤖...UMMM HI",
            "How are you?": "🤖NERVOUS!"}
    userChoice= choosepersonality()
    if userChoice == "Nice":
        personality= nice
    elif userChoice == "Nervous":
        personality = nervous
        
    intro()
    while True:
        answer= input("(What will you say?)")



# DON'T TOUCH! Setup code that runs your main() function.
if __name__ == "__main__":
  main()
