# string = "1234567890"
#
# #  using iterator to move in the string char array
#
# my_iterator = iter(string)
# print(my_iterator)
#
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# #  this is the last element 10 that corresponds to 0
# print(next(my_iterator))
#
# #  this will throw an error because is out of the char array range that is 10 and this one is 11
# # print(next(my_iterator))


data = []
data.append(1)
data.append("hi")
data.append(2)
data.append("salut")
data.append(3)
data.append("hola")
data.append(4)
data.append("allo")

my_iterator = iter(data)
# for n in data:
#     print(next(my_iterator))

# another way
for i in range(0, len(data)):
        next_item = next(my_iterator)
        print(next_item)

