# The Number Guessing Game

This is a Python-based number guessing game where the computer randomly selects a number between 1 and 100. The player needs to guess the number within a limited number of attempts, depending on the difficulty level they choose.

## How It Works

1. The computer will randomly select a number between 1 and 100.
2. The player will choose a difficulty level:
   - **Easy**: 10 attempts to guess the correct number.
   - **Hard**: 5 attempts to guess the correct number.
3. The player will make guesses, and the game will indicate whether the guess is:
   - Too High
   - Too Low
   - Correct
4. If the player guesses correctly, they win the game. If they run out of attempts, they lose the game.

## Features

- Difficulty selection (`easy` or `hard`).
- Provides feedback for each guess (too high, too low, or correct).
- Limits the number of guesses based on the difficulty level.

## How to Run

1. Ensure you have Python installed on your machine.
2. Install the `art` module for the logo by running:

    ```bash
    pip install art
    ```

3. Download the Python script and run it:

    ```bash
    main.py
    ```

4. Follow the prompts to start guessing!

## Example Usage

```bash
Choose a difficulty. Type 'easy' or 'hard': easy
You have 10 attempts remaining to guess the number.
make a guess:43
Too Low.
You have 9 attempts remaining to guess the number.
make a guess: 75
Too High.
```
