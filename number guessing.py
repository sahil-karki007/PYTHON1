import random

print("Welcome to Number Guessing Number")

n = random.randint(1,100)

while True:
    a = int(input("Guess no. between 1 to 100"))

    if a < n:
        print("too low! TRY AGAIN")

    elif a > n:
        print("too high! TRY AGAIN")

    elif a == n:
        print("CONGRATULATIONS!!! You guessed right:",n)   
        break 
