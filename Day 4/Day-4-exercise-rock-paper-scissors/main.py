import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choice_list = [rock, paper, scissors]

play_again = 'y'

while(play_again == "y"):
  random_integer = random.randint(0, 2)

  choice = input("Rock, paper, or scissors? ")
  choice = choice.lower()

  if choice == "rock" or choice == 'r':
    choice = choice_list[0]
  elif choice == "paper" or choice == 'p':
    choice = choice_list[1]
  elif choice == "scissors" or choice == 's':
    choice = choice_list[2]

  print("Player's choice:")
  print(choice)
  print("Computer's choice:")
  print(choice_list[random_integer])

  if(choice == choice_list[random_integer]):
    print("Draw")
  elif(choice == rock and choice_list[random_integer] == paper):
    print("Player loses")
  elif(choice == rock and choice_list[random_integer] == scissors):
    print("Player wins")
  elif(choice == paper and choice_list[random_integer] == rock):
    print("Player wins")
  elif(choice == paper and choice_list[random_integer] == scissors):
    print("Player loses")
  elif(choice == scissors and choice_list[random_integer] == paper):
    print("Player wins")
  elif(choice == scissors and choice_list[random_integer] == rock):
    print("Player loses")
  else:
    print("Error")

  play_again = input("Do you want to play again? (y/n) ")
  play_again = play_again.lower()

  while(play_again != 'y' and play_again != 'n'):
    play_again = input("Do you want to play again? (y/n) ")
    play_again = play_again.lower()

print("Thank you for playing")