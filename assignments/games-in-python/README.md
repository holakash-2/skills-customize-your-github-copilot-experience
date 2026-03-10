# 📘 Assignment: Hangman Game Challenge

## 🎯 Objective

Build the classic word-guessing game using Python strings, loops, and user input. Create a Hangman game where players guess letters to reveal a hidden word before running out of attempts.

## 📝 Tasks

### 🛠️ Set Up Game Structure and Initialization

#### Description
Create the foundation of your Hangman game by setting up word selection, tracking game state, and initializing variables.

#### Requirements
Completed program should:

- Randomly select a word from a predefined list of words
- Initialize tracking variables for incorrect guesses, guessed letters, and attempts remaining
- Display the starting game state with blanks for unrevealed letters (e.g., `_ _ _ _`)

### 🛠️ Implement Letter Guessing and Display Logic

#### Description
Develop the core gameplay loop where players input letter guesses and see the progress of the hidden word updated.

#### Requirements
Completed program should:

- Accept letter guesses from player input
- Update and display the current progress with correct guesses revealed
- Track which letters have been guessed to prevent duplicates
- Show remaining incorrect guesses count after each turn

### 🛠️ Implement Win/Lose Conditions and Game Flow

#### Description
Add logic to end the game appropriately and provide clear feedback to the player.

#### Requirements
Completed program should:

- Detect when the word is fully guessed and display a win message
- Detect when attempts are exhausted and display a lose message
- Exit the game loop when win/lose conditions are met
