import shelve

# btl = ["bacon", "lettuce", "tomato", "bread"]
# beans_on_toast = ["beans", "bread"]
# scrambled_eggs = ["eggs", "butter", "milk"]
soup = ["tin of soup"]
# pasta = ["pasta", "cheese"]

# writeback can update automatically the shelve info into disk but has heavy memory consumption
with shelve.open('recipes', writeback=True) as recipes:
    # recipes["btl"] = btl
    # recipes["beans on toast"] = beans_on_toast
    # recipes["scrambled_eggs"] = scrambled_eggs
    # recipes["pasta"] = pasta
    # recipes["soup"] = soup

    # updating the recipes shelve file
    # temp_list = recipes["btl"]
    # temp_list.append("butter")
    # recipes["btl"] = temp_list
    #
    # temp_list = recipes["pasta"]
    # temp_list.append("tomato")
    # recipes["pasta"] = temp_list
    recipes["soup"].append("croutons")

    for snack in recipes:
        print(snack, recipes[snack])