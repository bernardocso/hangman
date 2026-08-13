# Hangman

A command-line Hangman game built in Python. The player has six lives to uncover a randomly selected word by guessing individual letters, consecutive letter sequences, or the complete word.

## Features

* Randomly selects a word from a predefined word list
* Gives the player six lives
* Accepts single-letter guesses
* Accepts valid consecutive letter sequences
* Accepts complete-word guesses
* Reveals all matching letters when a correct guess is made
* Tracks previous guesses and rejects exact repeats
* Rejects empty and non-alphabetic input
* Handles input case-insensitively
* Tracks the number of valid guesses
* Ends the game when the word is completed or all lives are lost

## How to Run

1. Make sure Python 3 is installed.

2. Clone the repository:

```bash
git clone https://github.com/bernardocso/hangman.git
```

3. Move into the project directory:

```bash
cd hangman
```

4. Run the game:

```bash
python3 hangman.py
```

## What I Practised

- Breaking a larger programming problem into smaller pieces
- Using loops and conditionals to control game flow
- Tracking and updating program state across multiple guesses
- Working with strings, lists, and membership checks
- Rebuilding a displayed word based on previously guessed letters
- Validating and normalising user input
- Handling duplicate, invalid, and incorrect guesses
- Using the `random` module to select a word
- Debugging logical errors and edge cases through repeated testing
- Separating internal game state from display formatting

## Development

This project was built from scratch as part of my ongoing programming and software development journey. I focused on developing the game logic independently, testing edge cases, and debugging problems as they appeared rather than following a completed implementation.