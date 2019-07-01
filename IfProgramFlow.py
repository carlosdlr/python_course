# name = input("Please enter you name: ")
# #casting the input to integer value
# age = int(input("How old are you, {0}? ".format(name)))
#
# print(age)
#
# if age >= 18:
#   print("You are old enough to vote")
#   print("Please put an X in the box")
# else:
#   print("Please come back in {0} years".format(18 - age))

# print("Please guess a number between 1 nd 10 :")
# guess = int(input())

# if guess < 5:
#   print("guess higher")
#   guess = int(input())
#   if guess == 5:
#     print("Well done, you guessed it.")
#   else:
#     print("Sorry, you have not guessed correctly.")
# elif guess > 5:
#   print("Please guess lower")
#   guess = int(input())
#   if guess == 5:
#     print("Well done, you guessed it")
#   else:
#     print("Sorry, you have not guessed correctly.")
# else:
#   print("You go it first time")

#optimized version
# if guess != 5:
#   if guess < 5:
#    print("Please guess higher")
#   else:
#    print("Please guess lower")
#
#   guess = int(input())
#   if guess == 5:
#     print("Well done, you guessed it")
#   else:
#     print("Sorry, you have not guessed correctly.")
# else:
#   print("You go it first time")

#logical conditionals
# age = int(input("How old are you? "))

# and conditional
#if (age >= 15) and (age <= 65):
#if 15 < age < 66:
  #print("Have a good day at work")

# or conditional
#if (age < 16) or (age > 65):
#  print("Enjoy you free time")
#else:
#  print("Have a good day at work")

#not conditional
# if not(age < 18):
#   print("You are old enough to vote")
#   print("Please put an X in the box")
# else:
#   print("Please come back in {} years".format(18 - age))

# to check if a character is present in a string
parrot = "Norwegian blue"

letter = input("Enter a character: ")

# if letter in parrot:
#   print("Give me an {}, Bob".format(letter))
# else:
#   print("I don't need that letter")

if letter not in parrot:
  print("I don't need that letter")
else:
  print("Give me an {}, Bob".format(letter))
