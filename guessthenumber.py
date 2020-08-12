import random as random

#generate the number
random_number = random.randrange(20)

attempts = 0
lower = 0
higher = 0

#welcome message
nickname = input("Enter a nickname: ")
print("Hello " + nickname + ", you have 3 attempts to guess the number between 0 and 20!")

user_pick = int(input("Guess the number: "))

while attempts < 3:
    lower = 0
    higher = 0
    if user_pick == random_number:
        attempts = 3
        print("Wooah, nice! You guessed the number, congratulations!")
    else:
        attempts += 1
        if user_pick > random_number:
            higher = 1
        else:
            lower = 1
        print("Ohh, your number was " + ("higher" if higher == 1 else "lower") + ". Attempts: " + str(attempts) + "/3.")
        user_pick = int(input("Try again: "))
if attempts == 3:
    print("Ohh, you don't guessed the number, but you can try again any time! ;)")
    print("Oh.. I forgot to say that the number was " + str(random_number))
