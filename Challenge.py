locationsDictionary = {0: "You are sitting in front of a computer learning python",
                       1: "You are standing at the end of a road before a small brick building",
                       2: "You are at the top of a hill",
                       3: "You are inside a building, a well house for a small stream",
                       4: "You are in a valley beside a stream",
                       5: "You are in the forest"}

exitsDictionaries = {0: {"Q": 0},
                     1: {"W": 2, "E": 3, "N": 5, "S": 4, "Q": 0},
                     2: {"N": 5, "Q": 0},
                     3: {"W": 1, "Q": 0},
                     4: {"N": 1, "W": 2, "Q": 0},
                     5: {"W": 2, "S": 1, "Q": 0}}

vocabulary = {
    "QUIT": "Q",
    "NORTH": "N",
    "SOUTH": "S",
    "EAST": "E",
    "WEST": "W"
}


# ways of use split
print(locationsDictionary[0].split())
print(locationsDictionary[3].split(","))
print(' '.join(locationsDictionary[0].split()))



# starting location
# loc = 1
#
# while True:
#     availableExits = ",".join(exitsDictionaries[loc].keys())
#
#     print(locationsDictionary[loc])
#
#     if loc == 0:
#         break
#
#     direction = input("Available exits are: " + availableExits).upper()
#     print()
#     # parse de user input using the vocabulary dictionary
#     if len(direction) > 1: # check if has more than 1 letter
#         for word in vocabulary:
#             if word in direction:
#                 direction = vocabulary[word]
#
#     if direction in exitsDictionaries[loc]:
#         loc = exitsDictionaries[loc][direction]
#     else:
#         print("You cannot go in that direction")
