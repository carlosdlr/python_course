decimals = range(0, 100)
my_range = decimals[3:40:3]
# equality in ranges
print(my_range == range(3, 40, 3))  # will print True is the same range the was created in the previous line

print(range(0, 5, 2) == range(0, 6, 2))  # will print True again because we are not specifying the same list of numbers
#  to take the range.

r = range(0, 100)
print(r)

for i in r[::-2]:  # prints in a reverse way the numbers skipping by 2
    print(i)

print('=' * 50)
for i in range(99, 0, -2):
    print(i)

print('=' * 50)
print(range(0, 100)[::-2] == range(99, 0, -2))  # will print True because both functions takes the range of values in a
# inverse way

for i in range(0, 100, -2):
    print(i)  # will print nothing because we are starting the range at 0 and in the range we are telling that skips
# by -2 so the function will starts at the end of the range.


forward_string = "Python is a very powerful language"
backwards_string = forward_string[::-1]

print(backwards_string)  # will print this phrase in an inverse way
print(backwards_string[::-1])  # will print this phrase in a forward way
print(forward_string == backwards_string[::-1]) 
