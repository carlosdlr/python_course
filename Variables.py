#valid names for variables
greeting = "James"
_myName = "Carlos"
Carlos36 = "Good"
Carlos_Was_37 = "Salut"
Greeting = "There"
print(Carlos_Was_37 + ' '+greeting)

age = 24
print(age)

#this will cause an exception
# due is not able to concatenate a string with a int
#print(greeting + age)

#number variables and basic math operations
a = 12
b = 3
print(a + b)
print(a - b)
print(a * b)
print(a / b) #returns a decimal (float) value
print(a // b) # returns a int value
print(a % b)
print("-------------------------------")
#loop using range function with specific range values
for i in range(1, 4):
  print(i)
print("-------------------------------")
#loop using range function with an expression
#for i in range(1, a/b): # this will cause a exception because the expression returns a float just allow int values
#  print(i)

for i in range(1, a//b): #using double slash to return an int value
  print(i)
print("-------------------------------")

#operators precedence
print(a + b /3 -4 * 12)
print(8 / 2 * 3)
print(8 * 3 / 2)
print((((a + b) /3) -4) * 12)