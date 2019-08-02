import random

# A list of words that
potential_words = ["cars", "butterfly", "honey", "rainbow", "cheer"]

word = random.choice(potential_words)

# Use to test your code:
# print(word)

# Converts the word to lowercase
word = word.lower()

print("The word you are guessing is" +  " " + str(len(word)) + "letters long")
# Make it a list of letters for someone to guess
current_word = ["_", "_"] # TIP: the number of letters should match the word

# Some useful variables
guesses = []
maxfails = 7
fails = 0

while fails < maxfails:guess = input("Guess a letter: ")
    if not (guess.isalpha() and len(guess)== 1 and guess.islower()):
        print("the word you guessed needs to be single,lowercase letter, TRY AGAIN.")
    elif guess in word:
        print("correct guess!!!")
    else:
        print("That letter is not in your word")

	# check if the guess is valid: Is it one letter? Have they already guessed it?

	# check if the guess is correct: Is it in the word? If so, reveal the letters!

	print(current_word)

	fails = fails+1
	print("You have " + str(maxfails - fails) + " tries left!")
