#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

logo = """
 _   _                 _                 _____                     _             
| \ | |               | |               |  __ \                   (_)            
|  \| |_   _ _ __ ___ | |__   ___ _ __  | |  \/_   _  ___  ___ ___ _ _ __   __ _ 
| . ` | | | | '_ ` _ \| '_ \ / _ \ '__| | | __| | | |/ _ \/ __/ __| | '_ \ / _` |
| |\  | |_| | | | | | | |_) |  __/ |    | |_\ \ |_| |  __/\__ \__ \ | | | | (_| |
\_| \_/\__,_|_| |_| |_|_.__/ \___|_|     \____/\__,_|\___||___/___/_|_| |_|\__, |
                                                                            __/ |
                                                                           |___/ 
                         _____                                                   
                        |  __ \                                                  
                        | |  \/ __ _ _ __ ___   ___                              
                        | | __ / _` | '_ ` _ \ / _ \                             
                        | |_\ \ (_| | | | | | |  __/                             
                         \____/\__,_|_| |_| |_|\___|      
                         
"""   

print(logo)

import random

secret_number = random.randint(1, 100)

is_game_over = False
EASY_MODE = 10
HARD_MODE = 5

guesses = 0

limit = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
if limit == "easy":
  limit = EASY_MODE
elif limit == "hard":
  limit = HARD_MODE

while not is_game_over and guesses <= limit:
  guess = int(input("\nGuess a number between 1-100: "))

  if guess == secret_number:
    is_game_over = True
    print("You guessed the secret number, {secret_number}!")
  elif guess > secret_number:
    print("Too high")
    guesses += 1
  elif guess < secret_number:
    print("Too low")
    guesses += 1

  guesses_left = limit - guesses

  if guesses < limit:
    print(f"Guesses remaining: {guesses_left}")
  if guesses >= limit:
    is_game_over = True
    print(f"No more guesses, secret number was {secret_number}")
  