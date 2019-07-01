# for i in range(17):
#     print("{0:>2} in binary is {0:>02x}".format(i))


# printing decimal number in binary

powers =[]
for power in range(15, -1, -1):
    powers.append(2 ** power)

print(powers)


x = int(input("Enter a number: "))

printing = False


for power in powers:
    bit = x // power
    if bit !=0 or power == 1:
        printing = True
    if printing:
        print(bit, end='')
    x %= power
