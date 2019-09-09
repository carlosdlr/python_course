import shelve

# shelve allows to store dictionaries in a database file and access to values using keys
# creating a shelve

with shelve.open('ShelveTest') as fruit:  # this approach use shelve auto close and indentation
    # to create an access context to the shelve file data
    fruit['orange'] = "a sweet, orange, citrus fruit"
    fruit['apple'] = "good for making cider"
    fruit['lemon'] = "a sour, yellow citrus fruit"
    fruit['grape'] = "a small, sweet fruit growing in bunches"
    fruit['lime'] = "a sour, green citrus fruit"

    print(fruit["lemon"])
    print(fruit["grape"])

print(fruit)

# this approach allow close manually the shelve file
# fruit = shelve.open('ShelveTest')
# fruit['orange'] = "a sweet, orange, citrus fruit"
# fruit['apple'] = "good for making cider"
# fruit['lemon'] = "a sour, yellow citrus fruit"
# fruit['grape'] = "a small, sweet fruit growing in bunches"
# fruit['lime'] = "a sour, green citrus fruit"
#
# print(fruit["lemon"])
# print(fruit["grape"])
#
# fruit.close()
# print(fruit)

# another way to initialize a shelve and allow access to the data without indentation outside of the shelve context
# with shelve.open('ShelveTest') as fruit:
#     fruit = {"orange": "a sweet, orange, citrus fruit",
#              "apple": "good for making cider",
#              "lemon": "a sour, yellow citrus fruit",
#              "grape": "a small, sweet fruit growing in bunches",
#              "lime": "a sour, green citrus fruit"}
#
# print(fruit["lemon"])
# print(fruit["grape"])
#
# print(fruit)
