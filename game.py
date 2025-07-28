import random

# Predefined list of words
words = ["apple", "bread", "chair", "plant", "robot"]

# Randomly select a word from the list
word_to_guess = random.choice(words)
guessed_letters = []
tries = 6

# Create a display version of the word using underscores
display_word = ["_" for _ in word_to_guess]

print("Welcome to Hangman!")
print("Guess the word, one letter at a time.")
print("You have 6 incorrect guesses.\n")

# Game loop
while tries > 0 and "_" in display_word:
    print("Word:", " ".join(display_word))
    print("Guessed letters:", " ".join(guessed_letters))
    guess = input("Enter a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single alphabetical character.\n")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter. Try again.\n")
        continue

    guessed_letters.append(guess)

    if guess in word_to_guess:
        print("Good guess!\n")
        for i in range(len(word_to_guess)):
            if word_to_guess[i] == guess:
                display_word[i] = guess
    else:
        tries -= 1
        print(f"Wrong guess! You have {tries} tries left.\n")

# Result
if "_" not in display_word:
    print("Congratulations! You guessed the word:", word_to_guess)
else:
    print("Sorry, you ran out of tries. The word was:", word_to_guess)