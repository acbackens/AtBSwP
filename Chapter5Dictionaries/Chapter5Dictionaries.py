# 1. What does the code for an empty dictionary look like?
# {}

# 2. What does a dictionary with a key 'foo' and a value 42 look like?
# dict = {'foo': 42}

# 3. What is the main difference between a dictionary and a list?
# Lists are unordered and have indexes, while dictionaries have keys and values.

# 4. What happens if you try to access spam['foo'] if spam is {'bar': 100}?
# KeyError: 'foo'

# 5. If a dictionary is stored in spam, what is the difference between the expressions "'cat' in spam" and "'cat' in
# spam.keys()"?
# "'cat' in spam" checks if there is a key or value that contains the string 'cat' while "'cat' in spam.keys() only
# checks if there is a key called 'cat'.

# 6. If a dictionary is stored in spam, what is the difference between the expressions "'cat' in spam" and "'cat' in
# spam.values()"?
# "'cat' in spam" checks if there is a key or value that contains the string 'cat' while "'cat' in spam.keys() only
# checks if there is a value called 'cat'.

# 7. What is a shortcut for the following code?
# if 'color' not in spam:
#   spam['color'] = 'black'
# spam.setdefault('color', 'black')

# 8. What module and function can be used to "pretty print" dictionary values?
# Module pprint, function pprint() and pformat()


# Practice Project: Fantasy Game Inventory

def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        print(str(v) + ' ' + k)
        item_total += v
    print("Total number of items: " + str(item_total))


def addToInventory(inventory, addedItems):
    count = {}
    for x in addedItems:
        if x not in count:
            count.setdefault(x, 0)
            count[x] += 1
        else:
            count[x] += 1

    for k, v in count.items():
        if k not in inventory.keys():
            inventory.setdefault(k, v)
        else:
            inventory[k] = inventory.get(k, 0) + v

    return inventory


inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)
