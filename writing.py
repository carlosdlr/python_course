# cities = ["Brussels", "Liege", "Waterloo", "Leuven", "Antrewp"]
#
# with open("cities.txt", "w") as city_file:
#     for city in cities:
#         print(city, file=city_file)

# Adding data from a file to a data structure
cities = []
with open("cities.txt", "r") as city_file:
    for city in city_file:
        cities.append(city.strip("\n"))  # strip function allows to remove characters from the beginning or the end

print(cities)
for city in cities:
    print(city)
