# 2 ways to create sets
# 1 using curly braces
farm_animals = {"sheep", "cow", "hen"}
print(farm_animals)

for animal in farm_animals:
    print(animal)

print("=" * 40)

# 2 using the set function and brackets
wild_animals = set(["lion", "tiger", "panther", "elephant"])
print(wild_animals)

for animal in wild_animals:
    print(animal)

# adding values to a set
farm_animals.add("horse")
wild_animals.add("horse")
print(farm_animals)
print(wild_animals)

# create an empty set
empty_set = set()
empty_set_2 = {}  # this will create a dictionary
empty_set.add("a")
# empty_set_2.add("a") this line will fail because if we use curly braces will create dictionary this structure doesn't
# have the add function
# print()
# print("printing even numbers from 0 to 40 in a set and also the set length")
# print("=" * 40)
# even = set(range(0, 40, 2))
# print(even)
# print(len(even))
#
# print()
# print("printing a tuple transformed into a set and also the set length")
# print("=" * 40)
# squares_tuple = (4, 6, 9, 16, 25)
# # transforming tuple into a set
# squares = set(squares_tuple)
# print(squares)
# print(len(squares))
#
# print()
# print("printing the union between 2 sets")
# print("=" * 40)
# print(even.union(squares))
# print(len(even.union(squares)))
#
# print()
# print("printing the intersection between 2 sets")
# print("=" * 40)
# print(even.intersection(squares))
# print(even & squares)  # another way to make an intersection
# print(squares.intersection(even))
# print(squares & even)

# print()
# even = set(range(0, 40, 2))
# print(sorted(even))
# squares_tuple = (4, 6, 9, 16, 25)
# squares = set(squares_tuple)
# print(sorted(squares))
#
# print()
# print("even minus squares")
# print(sorted(even.difference(squares)))
# print(sorted(even - squares))
#
# print()
# print("squares minus even")
# print(sorted(squares.difference(even)))
# print(sorted(squares - even))
#
# print("=" * 40)
# print(sorted(even))
# print(squares)
# even.difference_update(squares);
# print(sorted(even))

# even = set(range(0, 40, 2))
# print(sorted(even))
# squares_tuple = (4, 6, 9, 16, 25)
# squares = set(squares_tuple)
# print(sorted(squares))
#
# print("symmetric even minus squares")
# print(sorted(even.symmetric_difference(squares)))
#
# print("symmetric squares minus even")
# print(sorted(squares.symmetric_difference(even)))

# even = set(range(0, 40, 2))
# print(even)
# squares_tuple = (4, 6, 9, 16, 25)
# squares = set(squares_tuple)
# print(squares)
#
# squares.discard(4)
# squares.remove(16)
# squares.discard(8)  # doesn't throw error
# # handling the error
# try:
#     squares.remove(8)  # throw error if the element is not present in the set
# except KeyError:
#     print("element 8 is not present in the set")

# even = set(range(0, 40, 2))
# print(even)
# squares_tuple = (4, 6, 16)
# squares = set(squares_tuple)
# print(squares)
#
# if squares.issubset(even):
#     print("squares is a subset of even")
#
# if even.issuperset(squares):
#     print("even is a super subset of squares")

# immutable sets
even = frozenset(range(0, 100, 2))
print(even)
even.add(3)  # this implementation doesn't have the add method to avoid modifications


