def monday():
    print("hello world")
    name= input("What Your name?")
    answer=input("Do you like mondays," + name + "?")
    if answer == "yes":
        print("you wrong, stop that")
    elif answer == "no":
        print("you know it")
    else:
        print("What?")
monday()
