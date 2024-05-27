import random
import sys

def between():
  min_int = int(0)
  max_int = int(100)
  while True:
    lower = int(random.randint(min_int, max_int))
    higher = int(random.randint(min_int, max_int))
    if (higher > lower):
      a = higher - lower
      if (5 <= a <= 25):
        return (lower, higher)
      
def generate_random_int(lower, higher):
  x = int(random.randint(lower, higher))
  return (x)

lower, higher = between()
x = generate_random_int(lower, higher)
count = int(0)
while (count <= 7):
  print(f"Choose Between: {lower} <-> {higher}")
  count = count + 1
  user = int(input("Guess The Number: "))
  if user == x:
    print(f"Congratulations You Did It In {count}""\tTries")
    print(f"THE WINNING NUMBER WAS: {x}\n")
    break
  elif(user != x and count < 7):
    print(f"Ops! You Mmissed")
    print(f"You Still Have {7 - count} Tries\n")
  if (count == 7):
    print(f"Ops! You failed")
    print("Better Luck Next Time")
    print("The Winning Number Was: %d\n" % x)
    break

