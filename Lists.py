# parrot_list = ["non pinin", "no more", "a stiff", "bereft of live"]
#
# parrot_list.append("A Norwegian Blue")
#
# for state in parrot_list:
#     print("This parrot is " + state)
#
# even = [2, 4, 6, 8]
# odd = [1, 3, 5, 7, 9]
#
# # adding 2 lists [2, 4, 6, 8, 1, 3, 5, 7, 9]
# numbers = even + odd
#
# # sorting
# # numbers.sort()
#
# # print(numbers.sort()) #this will print none because this sorting is stored in the same object
#
# numbers_in_order = sorted(numbers)
#
# print(numbers_in_order)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# # comparing lists
#
# if numbers == numbers_in_order:
#     print("The lists are equals")
# else:
#     # print this line because has the same elements but in different order
#     print("The lists are not equal")
# list_1 = []
# list_2 = list()
#
# print("List 1: {}".format(list_1))
# print("List 2: {}".format(list_2))
#
# if list_1 == list_2:
#     print("The list are equal")  # print this line because both lists are empty
#
# print(list("The lists are equals"))  # automatically converts the string in a char array
# #  ['T', 'h', 'e', ' ', 'l', 'i', 's', 't', 's', ' ', 'a', 'r', 'e', ' ', 'e', 'q', 'u', 'a', 'l', 's']
#
# even = [2, 4, 6, 8]
# another_even = even
# another_even.sort(reverse=True)
# print(even) #  will print [8, 6, 4, 2], because the 2 variables are pointing to the same list
#
# #  to check if 2 variables are pointing to the same list
# print(another_even is even) #  will be printed True because are pointing to the same list
#
# #  if i use the the list() function this will create a new list
# another_even =list(even)
# print(another_even is even) #  will be printed False because another_even variable are pointing to a new list

#creating list of lists

# even = [2, 4, 6, 8]
# odd = [1, 3, 5, 7, 9]
#
# numbers = [even, odd]
# print(numbers) #  will print a list of lists [[2, 4, 6, 8], [1, 3, 5, 7, 9]]
#
# # printing list of lists using for loop
# for number_set in numbers:
#     print(number_set)
#
#     for value in number_set:
#         print(value)


menu = []
menu.append(["egg", "spam", "bacon"])
menu.append(["egg", "spam", "bacon", "orange", "cafe"])
menu.append(["egg", "sausage", "bacon", "bread"])
menu.append(["egg", "bacon"])
menu.append(["egg", "spam", "bacon", "cafe", "bread", "rice"])

#print(menu)

for meal in menu:
    if "spam" not in meal:
        for element in meal:
            print(element)




















