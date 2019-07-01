# #  defining a simple tuple, the tuples are immutable
# t = "a", "b", "c"
#
# print(t)  # this print a tuple you can recognize it when the values are printed is this way
# # ('a', 'b', 'c') between brackets
#
# print("a", "b", "c")  # this will print just the values a b c in line, is not a tuple
#
# print(("a", "b", "c"))  # this is another way to print the tuples
#
# welcome = "Welcome to my Nightmare", "Alice Cooper", 1975
# bad = "Bad Company", "Bad Company", 1974
# budgie = "Nightflight", "Budgie", 1981
# imelda = "More Mayhem", "Emilda May", 2011
# metallica = "Ride the Lighting", "Metallica", 1984
#
# # print(metallica)  # print the entire tuple in brackets
# # print(metallica[0])  # print the tuple first element in this case "Ride the Lighting"
# # print(metallica[1])
# # print(metallica[2])
#
# # metallica[0] = "Master of puppets"  # this will throw an error due the tuple is immutable
#
# # the tuple elements are immutable but you can update the tuple overriding it resetting the tuple
# imelda = imelda[0], "Imelda May", imelda[2]
# print(imelda)
#
# # unpacking the tuple using the left side variables separated by comma
# title, artist, year = imelda
# print(title)
# print(artist)
# print(year)
#
# metallica2 = ["Ride the Lighting", "Metallica", 1984]  # the list can be unpacked too like the tuple
# # using left side variables
# metallica2.append("rock")
#
# title, artist, year = metallica2  # this will fail because the number of arguments in the list
# # doesn't match with the number of left variables in this case are 3 and the list has 4
#
# print(metallica2)

# creating group of tuples inside a list
imelda = "More Mayhem", "Imilda May", 2011, ((1, "Pulling The Rug"), (2, "Psycho"), (3, "Mayhem"),
                                             (4, "Kentish Town Waltz"))

imelda2 = "More Mayhem", "Imilda May", 2011, (1, "Pulling The Rug"), (2, "Psycho"), (3, "Mayhem"), (4, "Kentish Town Waltz")


# unpacking the tuple using the left side variables including the group of tuples separated by comma
title, artist, year, tracks = imelda
print(title)
print(artist)
print(year)
print(tracks)

print("-"*50)

# unpacking the tuple using the left side variables including each tuple separated by comma
title, artist, year, track1, track2, track3, track4 = imelda2
print(title)
print(artist)
print(year)
print(track1)
print(track2)
print(track3)
print(track4)

print("-"*50)

print(title)
print(artist)
print(year)
for song in tracks:
    track, title = song
    print("\t Track number {}, Title: {}".format(track, title))


cast = ['Cleese', 'Idle', 'Gilliam', 'Jones', 'Palin', 'Chapman']

print(cast.sort())  


