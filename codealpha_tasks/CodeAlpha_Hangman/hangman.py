import random

# List of 5 predefined words
words = ["apple", "tiger", "school", "python", "garden"]

# Choose a random word
word = random.choice(words)

# Store guessed letters
guessed_letters = []

# Number of incorrect guesses
incorrect_guesses = 0
max_guesses = 6

print("Welcome to Hangman!")
print("Guess the word one letter at a time.")
print("You have 6 incorrect guesses.")

# Game loop
while incorrect_guesses < max_guesses:

    # Show the word with blanks
    display_word = ""

    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)
    print("Incorrect guesses:", incorrect_guesses, "/", max_guesses)

    # Check if the player has won
    if "_" not in display_word:
        print("Congratulations! You guessed the word:", word)
        break

    # Ask the player for a letter
    guess = input("Enter a letter: ").lower()

    # Check that the input is one letter
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter one letter only.")
        continue

    # Check if the letter was already guessed
    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    # Add the letter to the guessed list
    guessed_letters.append(guess)

    # Check if the guess is correct
    if guess in word:
        print("Correct guess!")
    else:
        incorrect_guesses += 1
        print("Wrong guess!")

# If the player uses all 6 incorrect guesses
if incorrect_guesses == max_guesses:
    print("\nGame over!")
    print("The word was:", word)

    