# pickling is the name that is use in python to serialize (counterpart concept in java) and stored objects

import pickle

# metallica = ('Black Album',
#              'Metallica',
#              '1994',
#              ((1, 'Enter sandman'),
#               (2, 'Sad but true'),
#               (3, 'Holier Than Thou'),
#               (4, 'The Unforgiven')))
#
# Example how to serialize
# with open("metallica.pickle", "wb") as  pickle_file:
#     pickle.dump(metallica, pickle_file)

# Example how to deserialize making the assumption that the metallica.pickle file is present
# with open("metallica.pickle", "rb") as  metallica_file:
#     metallica = pickle.load(metallica_file)
#
# print(metallica)
#
# album, artist, year, track_list = metallica
#
# print(album)
# print(artist)
# print(year)
# for track in track_list:
#     track_number, track_title = track
#     print(track_number, track_title)


# serializing and deserialized multiple objects in the same file
metallica = ('Black Album',
             'Metallica',
             '1994',
             ((1, 'Enter sandman'),
              (2, 'Sad but true'),
              (3, 'Holier Than Thou'),
              (4, 'The Unforgiven')))

even = list(range(0, 10, 2))
odd = list(range(1, 10, 2))

with open("metallica.pickle", "wb") as  pickle_file:
    pickle.dump(metallica, pickle_file)
    pickle.dump(even, pickle_file)
    pickle.dump(odd, pickle_file)
    pickle.dump(2895655, pickle_file)

with open("metallica.pickle", "rb") as  metallica_file:
    metallica = pickle.load(metallica_file)
    even_list = pickle.load(metallica_file)
    odd_list = pickle.load(metallica_file)
    x = pickle.load(metallica_file)


print(metallica)

album, artist, year, track_list = metallica

print(album)
print(artist)
print(year)
for track in track_list:
    track_number, track_title = track
    print(track_number, track_title)

print('=' * 40)

for i in even_list:
    print(i)


print('=' * 40)

for i in odd_list:
    print(i)


print('=' * 40)

print(x)


# how to execute OS commands using the pickle library
# pickle.loads(b"cos\nsystem\n(S'rm metallica.pickle'\ntR")  # remove the file using OS command rms




