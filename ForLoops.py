# for i in range(1, 20):
#   print("i is now {}".format(i))


number = "9,234,345,123,890,567,554"

# for i in range(0, len(number)):
#   print(number[i])
#

cleanedNumber = ''

# for i in range(0, len(number)):
#   if number[i] in '0123456789':
#     print(number[i])

# for i in range(0, len(number)):
#   if number[i] in '0123456789':
#     cleanedNumber = cleanedNumber + number[i]
#
# newNumber = int(cleanedNumber)
# print("The number is {}".format(newNumber))

#iterating over a char array
# for char in number:
#   if char in "0123456789":
#     cleanedNumber = cleanedNumber + char
#
#
# newNumber = int(cleanedNumber)
# print("The number is {}".format(newNumber))

#iterating over a string array
for state in ["not pinin","no more","a stiff","bereft of life"]:
  print("This parrot is {}".format(state))

#iterating over a range stepping 5
for i in range(0,100,5):
  print("i is {}".format(i))

for i in range(1,13):
  for j in range(1,13):
    print("{1} times {0} is {2}".format(i, j, i*j))
print("==================================")

#to print left to right
for i in range(1,13):
  for j in range(1,13):
    print("{1} times {0} is {2} {3:3}".format(i, j, i*j,"||"),end='\t')
  print('')