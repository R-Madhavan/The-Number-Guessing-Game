from art import logo
import random
#written by madhavan
computer_guess = random.randint(1,100)
print(computer_guess)
attempt = 0
user_guess = ""
print(logo)
#This is a function that ask or guessing number and check whether the user guess is equal to or higher or lower than computer guess.
def guess():
    global user_guess
    user_guess = int(input("make a guess: "))
    if user_guess > computer_guess:
        print("Too High.")
    elif user_guess < computer_guess:
        print("Too Low.")
    elif user_guess == computer_guess:
        print(f"You got it! The answer was {computer_guess}")

#This ask for difficulty level, if easy level then attempt = 10 or if its hard then attempt = 5.
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
if difficulty == "easy":
    attempt = 10
elif difficulty == "hard":
    attempt = 5
else:
    print("Invalid, Re-run program!")

#this section loops through the number of attempt to ask for guessing a number. if attempt = 0 or user and computer guesses are equal then ends.
for i in range(1, attempt+1):
    print(f"You have {attempt} attempt remaining to guess the number.")
    attempt -= 1
    guess()
    if user_guess == computer_guess:
        break
    elif attempt == 0:
        print("You run out of guesses, you lose.")
