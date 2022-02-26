import random

num = random.randrange(0,10)
ug = -1
t = 0

while ug != num: 
    ug = input("Guess a number between 1 and 10: ")
    
    if ug > num:
        print("You guessed too high!")

    if ug < num:
        print("You guessed too low...")

    t += 1

print("Congrats you guessed the number, and it only took you {} tries!".format( t))




