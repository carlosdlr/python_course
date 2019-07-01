number = "9,223,372,036,854,775,807"
cleaned_number = ''

for i in range(0, len(number)):
  if number[i] in '0123456789':
    cleaned_number += number[i] #augmented way to assign in python

new_number = int(cleaned_number)
print("The number is {} ".format(new_number))

x = 24
x += 1
print(x)

y = 24
y -= 1
print(y)

z = 24
z *= 5
print(z)

w = 24
w /= 2
print(w)

p = 24
p **= 2
print(p)

t = 24
t %= 2
print(t)

#binary operation with augmented assignments in strings
greeting = "Good "
greeting += "morning "
print(greeting)

greeting *= 5 #will create 5 strings something like Good morning
print(greeting)


number = 5
multiplier = 8
answer = 0
for i in range(0, 8):
  answer += number

print(answer)