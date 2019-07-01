name = input("Please enter you name: ")
#casting the input to integer value
age = int(input("How old are you, {0}? ".format(name)))

print(age)

if 18 <= age < 31:
  print("Welcome to the holiday 18 -31 club!!")
else:
  print("Sorry you are not in the coolest club 18 - 31 club!!")