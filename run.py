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

while True:
    possible_actions = ["r", "p", "scissors"]
    user_action = input(f"Hello {user_name}! What do you choose? Type (r, p, s)")
    possible_actions = ["r", "p", "s"]
    computer = random.choice(possible_actions)

    if user_action == computer:
            print(f"You choose {user_action}, computer chose {computer}.It's a draw!")

    elif user_action == "r" and computer == "s":
        print(f"You choose {user_action}, computer chose {computer}.You win!")
     
    elif user_action == "p" and computer == "r":
         print(f'You choose {user_action}, computer chose {computer}. You lose! Try again!')
    
    elif user_action == "s" and computer == "p":
        print(f"You choose {user_action}, computer chose {computer}. You won!")

    else:
        print(f"You choose {user_action}, computer chose {computer}.You lose! Try again!")

    



