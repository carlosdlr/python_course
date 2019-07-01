parrot = "Norwegian blue"
print(parrot)
print(parrot[3]) #prints the character that is in the string array position 3
#print(parrot[14]) # will throw and error because the string array doesn't have that position
print(parrot[-1]) #returns the last element of the string array
print(parrot[0:6]) #returns the elements of the string array between the range
print(parrot[:6]) #if the started point of the range is not defined the function takes the first element of the string by default
print(parrot[6:]) #if the ended point of the range is not defined the function takes the last element of the string by default
print(parrot[-4:-2]) #negaive range allows takes values from the string array starting from the end (-1) and so on
print(parrot[0:6:2]) # skip characters in the string array that are in the range
print(parrot[0:6:3])
print("------------------------------")

#examples to show how format inputs with the string array manipulation
number = "1,223,456,789,760,567"
print(number[1::4]) #print just commas start at position 1 and takes the 4 element
numbers = "1, 2, 3, 4, 5, 6, 7, 8, 9"
print(numbers[0::3]) #remove the commas start at position 0
print("------------------------------")

string1 = "he's "
string2 = "probably "
print(string1 + string2)
print("Hello " *5) #allows print the string different number of times
print("Hello " * (5+4)) #allows use an expression bear in mind the operator precedence
print("Hello " *5 + "4") #allows print a number of times and add another string
print("------------------------------")

#to check if a substring is in a string
today = "wednesday"
print("day" in today) #check if the substring day is in today string return True or False
print("sen" in today)