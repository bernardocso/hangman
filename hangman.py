#Hangman game

import random

words = ["Octopus", "Garden", "Location", "Inhibition", "Bounty"]
selected_word = random.choice(words).casefold()
lives_count = 6
guess_count = 1
guessed_letters = []
user_guesses = []
current_word = ""
display_current_word = ""
for letter in selected_word:
    current_word += "_"
    display_current_word += "_ "


print("Welcome to Hangman!")
print("Guess the correct letters to uncover the word. You have 6 lives.")

while current_word != selected_word and lives_count > 0:
    print("————————————————————————————————————————————————————————————")
    print(f"Guess {guess_count}:")
    print(display_current_word)
    user_guess = input("Guess a letter or word: ").strip().casefold()

    if not user_guess or user_guess.isalpha() == False:
         print("You must guess either a letter or word.")
    elif user_guess in user_guesses:
        if len(user_guess) > 1:
            print("You have already guessed this word or sequence. Try again!")
        else:
             print("You have already guessed this letter. Try again!")
        print(f"You have {lives_count} lives left")
    else:
        user_guesses.append(user_guess)
        if len(user_guess) > 1:
            print(f'You guessed "{user_guess}".')

            if user_guess in selected_word:
                for letter in user_guess:
                    if letter not in guessed_letters:
                        guessed_letters.append(letter)
                print("Correct!")
                print(f"You have {lives_count} lives left")
                current_word = ""
                display_current_word = ""
                for letter in selected_word:
                    if letter in guessed_letters:
                            current_word += letter
                            display_current_word += letter + " "
                    else:
                            current_word += "_"
                            display_current_word += "_ "
            else:
                print("Wrong!")
                lives_count -= 1
                print(f"You have {lives_count} lives left")
             
        else:
            print(f'You guessed "{user_guess}".')

            if user_guess in selected_word:
                guessed_letters.append(user_guess)
                print("Correct!")
                print(f"You have {lives_count} lives left")
                current_word = ""
                display_current_word = ""
                for letter in selected_word:
                    if letter in guessed_letters:
                            current_word += letter
                            display_current_word += letter + " "
                    else:
                            current_word += "_"
                            display_current_word += "_ "
            else:
                print("Wrong!")
                lives_count -= 1
                print(f"You have {lives_count} lives left")
        guess_count += 1



if lives_count == 0:
        print("Game over. Hangman is no longer with us.")
        print(f'''The word was "{selected_word.capitalize()}", but you don't care, do you?''')

if current_word == selected_word:
    print(f'Congratulations! You found the word: "{selected_word.capitalize()}".')
    if guess_count - 1 > 1:
         print(f"It took you {guess_count - 1} guesses to find the word.")
    else:
         print(f"It took you 1 guess to find the word.")
    print("Long live Hangman!")
    