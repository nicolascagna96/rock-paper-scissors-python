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
---'   ____)____1
          ______)
       __________)
      (____)
---.__(___)
''')

continue_game = True
print("Let's play Rock Paper Scissors!")

 # Get the user's name and validate it.
while True:
    user_name = input('Please input your name: ').capitalize()
    if user_name.isalpha():
        print()
        break
    else:
        print("Invalid entry: players name must be an alphabet")

# game rules and validation
while True:
    game_rules = input("The outcome of the game is determined by 3 simple rules: \n Rock ('r') wins against scissors ('s').\n Scissors ('s') win against paper ('p').\n Paper ('p') wins against rock ('r').\n Do you want to play? Press 'Y' to continue ")
    if game_rules == "Y":
        print()
        break
    else:
        print("Invalid entry: enter 'Y'")

# Logic of the game 
def game_logic():

    """
    This function is the logic of our game and it establishes who wins, loose or draw
    betwween the computer and the user.
    """

    possible_actions = ["rock", "paper", "scissors"]
    user_action = input(f"Hello {user_name}! Enter rock, paper or scissors ")
    computer = random.choice(possible_actions)
  
    if user_action == computer:
        print(f"You choose {user_action}, computer chose {computer}. It's a draw!")
        
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

# ask player to restart the game
def restart():
    '''
    This functions allowed the user to restart or continue the game
    '''
    while True:
        user_restart = input("Enter 'q' to quit, 'n' for a new game and any key to continue")
        if user_restart.lower() == "n":
            game_logic()
        elif user_restart.lower() == "q":
            print(f"The game ended! Bye {user_name}")
            quit()

# I used a while loop to repeat the code multiple time and the user can also restart or quit the game
while True:
    game_logic()
    restart()