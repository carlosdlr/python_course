#i = 0
# while i < 10:
#     print("i is now {0}".format(i))
#     i += 1

# infinity loop
#while True:
#    print("i is now {0}".format(i))

# available_exits = ["east", "north east", "south"]
# choosen_exit = ""
#
# while choosen_exit not in available_exits:
#     choosen_exit = input("Please choose a direction: ")
#     if choosen_exit == "quit":
#         print("Game Over")
#         break
#
# else:
#     print("aren't you glad you got out of there")

import random

highest = 10
answer = random.randint(1,highest)

print("Plese guess a number between 1 and {}".format(highest))
guess = 0

while guess !=  answer:
    guess = int(input())

    if guess < answer:
        print("Please guess higher")
    elif guess > answer:
        print("Please guess lower")
    else:
        print("Well done, you guessed it")
