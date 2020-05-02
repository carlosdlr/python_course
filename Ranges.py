# # print(range(100))
#
# # using range to fill a list
# my_list = list(range(10))  # fill the list ordered from 0 to 9
# print(my_list)
#
# even = list(range(0, 10, 2))  # fill the list ordered from 0 to 9 skipping 2 positions
# odd = list(range(1, 10, 2)) # fill the list ordered from 1 to 9 skipping 2 positions
#
# print(even)
# print(odd)

# working with indexes in a string
# my_string = "abcdefghijklmnopqrstuvwxyz"
# print(my_string.index("e"))  # returns 4 that is e, array based indexation starting from 0
# print(my_string[4])  # returns e that is 4 index, array based indexation starting from  0
#
#
# small_decimals = range(0, 10)
# print(small_decimals)
# print(small_decimals.index(3))
#
# odd = range(1, 10000, 2)
# print(odd)
#
# print(odd[1234])

# to slice a range
decimals = range(0,100)
print(decimals)

my_range = decimals[3:40:3]  # the : allows take a range inside another range in this case takes from 3 to 40
# skipping by 3

print(my_range)

for i in my_range:
    print(i)


print('=' * 40)

for i in range(3, 40, 3):
    print(i)
