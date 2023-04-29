import random
from game_data import data
from art import logo, vs
from replit import clear

def randomizer():
  randict = random.choice(data)
  return randict
  
score = 0
game_on = True
first = randomizer()
second = randomizer()
print(logo)
while game_on:
  print(f"Compare A: {first['name']}, a {first['description']}, from {first['country']}")

  print(vs)
  
  print(f"Compare B: {second['name']}, a {second['description']}, from {second['country']}")

  choice = input("Who has more followers? Type 'A' or 'B': ")
  if choice == 'A' or choice == 'a':
    if first['follower_count'] > second['follower_count']:
      score += 1
      clear()
      print(logo)
      print(f"You're right! Your current score is {score}")
      second = randomizer()
    else:
      clear()
      print(logo)
      print(f"Sorry, that's wrong. Final score: {score}")
      game_on = False
  elif choice == 'B' or choice == 'b':
    if second['follower_count'] > first['follower_count']:
      score += 1
      clear()
      print(logo)
      print(f"You're right! Your current score is {score}")
      c = first
      first = second
      second = randomizer()
    else:
      clear()
      print(logo)
      print(f"Sorry, that's wrong. Final score: {score}")
      game_on = False
  
