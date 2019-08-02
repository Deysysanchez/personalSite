import random

# A list of words that
potential_words = ["cars", "butterfly", "honey", "rainbow", "cheer"]

word = random.choice(potential_words)
clue= word[0]+word[(len(word)-1):(len(word))]
amount_letterguess=''
wordguessed=''
lettersstores=''
tries=5
count=0
print("Your job is to guess the word, you have five tries")
print("and if you dont guess it by the five tries you loose")

while count < tries:
    wordguessed=input("Guess a letter: ")
    if wordguessed in word:
        print("YESSS")
        lettersstores += wordguessed
        count+=1
    if wordguessed not in word:
        print("No try again")
        count+=1
    if count==2:
        print("yes or no")
        clue_request==input("would you like to get a clue?")
        if clue_request == "yes":
            print("Clue: The first letter and last letter of the word is:" clue)
        if clue_request== "no":
            print("WOW! YOU ARE BRAVE")
print("Now its time to guess.You've guessed",len(lettersstores), "letter correctly")
print("These letter are:" lettersstores)

wordguessed=input("Guess the whole word: ")
while wordguessed:
    if wordguessed.lower() != correct:
        print("YOU DID IT!!!")
        break
    elif wordguessed.lower() != correct:
        print("nice try, the correct word was:",words)
        break
