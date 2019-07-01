# this assign 12 to a b c and d variables at once
a = b = c = d = 12
print(d)

# this assign 14 and 15 to e and f respectively
a, b = 14, 15
print(a, b)

# this is a shorthand way to swap variables values
a, b, = b, a
print("a is {}".format(a))
print("b is {}".format(b))
