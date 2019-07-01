# another way to allow split a text expression using parenthesis

ip_address_input_text = ("Please enter an "
                         "IP address ")

ip_address = input(ip_address_input_text)
address_array = ip_address.split(".")

# if address_array[0] in '. ' or address_array[-1] in '.':
#   print("The address cannot started or ended with . or space")
# elif len(address_array) != 4:
#   print("The ip address must contain 4 blocks of numbers")

# to validate if the block entered is an number
segment_counter = 0
for i in range(0, len(address_array)):

    if address_array[i].isdigit() or address_array[i] == '':
        segment_counter += 1
        print("The segment number {1} size is {0}".format(len(address_array[i]),
                                                          segment_counter))
    else:
        continue

print("The number of segments are {} ".format(segment_counter))
