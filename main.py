from game_data import data
import random
import art
from replit import clear

#Display art.
print(art.logo)
score = 0
account_b = random.choice(data)
game_should_continue = True

def format_data(account):
  """Format the account detail into a printable format."""
  account_name = account["name"]
  account_descr = account["description"]
  account_country = account["country"]
  return f"{account_name}, {account_descr}, from {account_country}"


def check_answer(guess, a_follower, b_follower):
  """Checks followers against user's guess 
  and returns True if they got it right.
  Or False if they got it wrong."""
  if a_follower > b_follower:
    if guess == "a":
      return True
    else:
      return False

while game_should_continue:      
  #Generate a random accounts from game_data.
  account_a = account_b
  account_b = random.choice(data)
  if account_a == account_b:
    account_b = random.choice(data)
  
  print(f"Compare A: {format_data(account_a)}.")
  print(art.vs)
  print(f"Against B: {format_data(account_b)}.")
  
  #Ask a user for guess.
  guess = input("Who has more followers? Type 'A' or 'B': ").lower()
  
  a_follower_count = account_a["follower_count"]
  b_follower_count = account_b["follower_count"]
  
  is_correct = check_answer(guess, a_follower_count, b_follower_count)
  clear()
  print(art.logo)
  if is_correct:
    score += 1
    print(f"You're right! Current score: {score}.")
  else:
    game_should_continue = False
    print(f"Sorry, that's wrong. Final score: {score}")
