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
game_rules = input("The outcome of the game is determined by 3 simple rules: \n Rock ('r') wins against scissors ('s').\n Scissors ('s') win against paper ('p').\n Paper ('p') wins against rock ('r').\n Do you want to play? Press 'Y' to continue ")

def game_logic():
    possible_actions = ["rock", "paper", "scissors"]
    user_action = input(f"Hello {user_name}! What do you choose? Type rock, paper or scissors ")
    computer = random.choice(possible_actions)

    computer_score = 0
    user_score = 0
    rounds = 0
    
    if user_action == computer:
        print(f"You choose {user_action}, computer chose {computer}.It's a tie!")

    elif user_action == "rock":
        if computer == "paper":
            print(f"You lose! {computer} covers {user_action}!")
     
        if computer == "scissors":
            print(f'You win! {user_action} smashes {computer}!')
    
    elif user_action == "scissors":
        if computer == "paper":
            print(f"You win! {user_action} cuts {computer}!")
        
        if computer == "rock":
            print(f"You lose! {computer} smashes {user_action}!")

    elif user_action == "paper":
        if computer == "scissors":
            print(f"You lose! {computer} cuts {user_action}!")
        
        if computer == "rock":
            print(f"You win! {user_action} covers {computer}!")

while True:
    game_logic()
    restart = input("Do you want to play again ? Y/N ")
    if restart == "N":
        print("The game has ended!")
        break
    elif restart == "Y":
        continue