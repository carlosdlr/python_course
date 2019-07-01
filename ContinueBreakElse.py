shopping_list = ["milk","pasta","eggs","spam","bread","rice"]

for item in shopping_list:
  if item == 'spam':
    continue # skip the current iteration

  print("Buy -- {0}".format(item))

print("===========================")

for item in shopping_list:
  if item == 'spam':
    break # exit out of the for loop

  print("Buy -- {0}".format(item))

print("===========================")

for item in shopping_list:
  if item == 'beans':
    break # exit out of the for loop
    print("Buy -- {0}".format(item))

else: # this else will be executed meanwhile the for finished all the iterations without break
  print("I'll have a plate of that, then, please")
