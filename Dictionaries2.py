fruits = {"orange": "a sweet, citrus fruit",
          "apple": "good for making cyder",
          "lemon": "a sour, yellow citrus fruit",
          "grape": "a small, sweet fruit growing in bunches"}

print(fruits)

veg = {
    "cabbage": "every child's favorite",
    "sprouts": "mmmmm delicious",
    "spinach": "can i have some more fruit, please"
}

print(veg)

# fruits.update(veg)  # this function allows to python add 2 dictionaries
# print(fruits)

# veg.update(fruits)  # this function allows to python add 2 dictionaries
# print(veg)

nice_and_nasty = fruits.copy()
nice_and_nasty.update(veg)

print(nice_and_nasty)
