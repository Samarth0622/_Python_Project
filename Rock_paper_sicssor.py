import random

choices = ('r', 'p', 's')

def get_user_choice():
 while True:
  user_choice = input("Rock, Paper, or Scissors? (r/p/s) :").lower()
  if user_choice in choices:
    return user_choice
  else:
    print("invalid choice ")
    
def display_choices(user_choice, computer_choice):
    print(f'you chose {user_choice}')
    print(f'computer chose {computer_choice}')
    
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
      print("tie!")
    elif (
     (user_choice == 'r' and computer_choice == 's') or 
     (user_choice == 's' and computer_choice == 'p') or 
     (user_choice == 'p' and computer_choice == 'r')):
       print("congratulations, you win!")
    else:
       print("sorry, you lose!")
       
def play_game():
    while True:
      user_choice = get_user_choice()
    
      computer_choice = random.choice(choices) 
    
      display_choices(user_choice, computer_choice)   

      determine_winner(user_choice, computer_choice)

      should_contuine = input("do you want to play again? (y/n): ").lower()
      if should_contuine == 'n':
       break

play_game()