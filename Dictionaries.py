fruits = {"orange": "a sweet, citrus fruit",
          "apple": "good for making cyder",
          "lemon": "a sour, yellow citrus fruit",
          "grape": "a small, sweet fruit growing in bunches"}

# print(fruits)

# print(fruits["apple"])  # accessing the date in the dictionary by key
#
# bike = {"make": "honda", "model": "250 dream", "colour": "red", "engine_size": "250"}
# print(bike["engine_size"])
# print(bike["colour"])
#
# # to add new key values to a dictionary
# fruits["pear"] = "an odd shaped apple"
# print(fruits)
#
# # to override a value in a dictionary
# fruits["lemon"] = "great with tequila"
# print(fruits)
#
# # to delete a value in a dictionary
# del fruits["lemon"]
# print(fruits)

# to delete the entire variable reference to the dictionary
# del fruits

# to clear the dictionary
# fruits.clear()
# print(fruits)

# while True:
#     dict_key = input("Please enter a fruit name: ")
#     if dict_key == "quit":
#         break;
#
#     description = fruits.get(dict_key, "we don't have a" + dict_key)  # shortcut to print a error message
#     # when the key doesn't exists in the dictionary
#     print(description)

# if dict_key in fruits:
#     description = fruits.get(dict_key)
#     print(description)
# else:
#     print("The fruit {0} doesn't exists in the dictionary ".format(dict_key))

# to print all the values in a dictionary
# for snack in fruits:
# print(fruits[snack])

##----------------------------------------------------------------------------##
print(fruits)

# while True:
#     dict_key = input("Please enter a fruit name: ")
#     if dict_key == "quit":
#         break
#     # another way to validate if a key is present in a dictionary
#     description = fruits.get(dict_key, "We don't have a" + dict_key)
#     print(description)
#     # if dict_key in fruits:
#     #     description = fruits.get(dict_key)
#     #     print(description)
#     # else:
#     #     print("The fruit {0} doesn't exists in the dictionary ".format(dict_key))

# iterating over a dictionary

# The dictionaries doesn't keep the keys order

# A way to order a dictionary using their keys
# ordered_keys = list(fruits.keys())
# ordered_keys.sort()

# A simplify way to sort
# ordered_keys = sorted(fruits.keys())
#
# for f in ordered_keys:
#     print(f + " - " + fruits[f])

# In a more concise way
for f in sorted(fruits.keys()):
    print(f + " - " + fruits[f])
