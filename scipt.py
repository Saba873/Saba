import random
current_number = random.randint(1, 10)
score = 0

while True:
  print(current_number)
  user = input("Higher or Lower? (h/l): ")
  new_number = current_number

  while new_number == current_number:
      new_number = random.randint(1, 10)
  if user == 'h' and new_number > current_number:
    print("Corect")
    score += 1
    current_number = new_number
  elif user == 'l' and new_number < current_number:
    print("Corecrt")
    score += 1
    current_number = new_number
  else:
      print("Wrong")
      break
print(f"Game Over! Final score: {score}")
