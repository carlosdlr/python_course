import shelve

# this approach allow close manually the shelve file
fruit = shelve.open('ShelveTest')
fruit['orange'] = "a sweet, orange, citrus fruit"
fruit['apple'] = "good for making cider"
fruit['lemon'] = "a sour, yellow citrus fruit"
fruit['grape'] = "a small, sweet fruit growing in bunches"
fruit['lime'] = "a sour, green citrus fruit"

# print(fruit["lemon"])
# print(fruit["grape"])
#
# # updating values in a shelve db file
# fruit["lime"] = "great with tequila"  # updating the lime key
#
# for snack in fruit:
#     print(snack + ": " + fruit[snack])

# while True:
#     dict_key = input("Please enter a fruit: ")
#     if dict_key == "quit":
#         break
#
#     # validates that the key exists in the db shelve file
#     if dict_key in fruit:
#         description = fruit[dict_key]
#         print(description)
#     else:
#         print("We don't have a " + dict_key)

# sorting
# ordered_keys = list(fruit.keys())
# ordered_keys.sort()
#
# for f in ordered_keys:
#     print(f + " - " + fruit[f])

# values view object example
for v in fruit.values():
    print(v)

print(fruit.values())  # ValuesView reference object from shelve db file

for i in fruit.items():
    print(i)

print(fruit.items())  # ItemsView reference object from shelve db file

fruit.close()
