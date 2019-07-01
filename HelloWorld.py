# print('Hello, World!')
# print(1 + 2)
# print(7 * 6)
# print()
# print("The End")
# print("Pyhton's Strings are easy to use")
# print('We can even include "quotes" in strings')
print("Hello" + " World") # concatenation

#defining variables
greeting = "Hello"
name = "Carlos"
print(greeting + " " +name)

#to capture input from keyboard
# nameInput = input("Please enter your name ")
# print(greeting + " " +nameInput)

#to split a string
splitString = "This string has been\nsplit over\nseveral\nlines"
print(splitString)

#to tab a string
tabString = "1\t2\t3\t4\t5\t"
print(tabString)

#to scape special characters
print('The pet shop owner said "No, no, \'e\'s uh,...he\s resting"')
print("The pet shop owner said \"No, no, \'e\'s uh,...he\s resting\"")

#another way to split lines using 3 double quotes
anotherSplitString = """This string has been
split over
several lines"""
print(anotherSplitString)

#triple quotes help to scape characters in a easiest way
print('''The pet shop owner said "No, no, 'e's uh,...he's resting"''')
print("""The pet shop owner said "No, no, 'e's uh,...he's resting" """)
