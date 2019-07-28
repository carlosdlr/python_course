# jabber = open("sample.txt", "r")
#
# for line in jabber:
#     if "jabberwock" in line.lower():
#         print(line, end='')
#
# jabber.close()

# using with function to open a file avoid to use the close function explicitly
# with open("sample.txt", "r") as jabber:
#     for line in jabber:
#         if "JAB" in line.upper():
#             print(line, end='')

# removing spaces at the end of each line
# with open("sample.txt", "r") as jabber:
#     line = jabber.read()
#     while line:
#         print(line, end='')
#         line = jabber.readline()

# reading multiple lines
with open("sample.txt", "r") as jabber:
    lines = jabber.readlines()
print(lines)  # this print the file as an array of strings

for line in lines[::-1]:
    print(line, end='')

with open("sample.txt", "r") as jabber:
    lines = jabber.read()
print(lines)

for line in lines[::-1]:
    print(line, end='')




