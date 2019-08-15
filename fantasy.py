# use a dictionary to store users where keys are strings values describing the item in the inventory and value is an int
# how many player of that item player has. { 'rope': 1, 'torch': 6, 'gold coin': 42}
# write function display_inventor()

stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}


def display_inventory(inventory):
    print("Inventory: ")
    item_total = 0

    for k, v in sorted(inventory.items()):
        print(k, ':', v)
        item_total += v
    print("Total number of items: " + str(item_total))


display_inventory(stuff)
# test
