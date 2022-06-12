import random

rock = print('''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''')

paper = print('''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
''')

scissors = print('''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
''')
print("Let's play Rock Paper Scissors!")

user_name = input("Enter your name to start the game ")
game_rules = input("The outcome of the game is determined by 3 simple rules: \n Rock ('r') wins against scissors ('s').\n Scissors ('s') win against paper ('p').\n Paper ('p') wins against rock ('r').\n Press 'Y' to continue ")

def game_logic():
    possible_actions = ["r", "p", "s"]
    user_action = input(f"Hello {user_name}! What do you choose? Type (r, p, s) ")
    possible_actions = ["r", "p", "s"]
    computer = random.choice(possible_actions)

    if user_action == computer:
            print(f"You choose {user_action}, computer chose {computer}.It's a draw!")

    elif user_action == "r" and computer == "s":
        print(f"You choose {user_action}, computer chose {computer}.You win!")
     
    elif user_action == "p" and computer == "r":
         print(f'You choose {user_action}, computer chose {computer}. You lose!')
    
    elif user_action == "s" and computer == "p":
        print(f"You choose {user_action}, computer chose {computer}. You won!")

    else:
        print(f"You choose {user_action}, computer chose {computer}.You lose!")

    
while True:
    game_logic()
    restart = input("Do you want to play again ? Y/N")
    if restart == "N":
        break
    elif restart == "Y":
        continue



