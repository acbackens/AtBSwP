# 1. What is []?
# [] is an empty list.

# 2. How would you assign the value 'hello' as the third value in a list stored in a variable named spam? (Assume spam contains [2, 4, 6, 8, 10].)
# spam[2] = 'hello'

# For the following three questions, let's say spam contains the list ['a', 'b', 'c', 'd'].

# 3. What does spam[int('3' * 2) / 11] evaluate to?
# TypeError: list indices must be integers or slices, not float

# 4. What does spam[-1] evaluate to?
# ['d']

# 5. What does spam[:2] evaluate to?
# ['a', 'b']

# For the following 3 questions, let's say bacon contains the list [3.14, 'cat', 11, 'cat', True].

# 6. What does bacon.index('cat') evaluate to?
# 1

# 7. What does bacon.append(99) make the list value in bacon look like?
# [3.14, 'cat', 11, 'cat', True, 99]

# 8. What does bacon.remove('cat') make the list value in bacon look like?
# [3.14, 11, 'cat', True]

# 9. What are the operators for list concatenation and list replication?
# +=, -=, *=, /=, %=

# 10. What is the difference between append() and insert() list methods?
# append() adds the element at the end of the list, and insert() adds the element at the specific position.

# 11. What are two ways to remove values from a list?
# del list[] and list.remove()

# 12. Name a few ways that list values are similar to string values?
# Both are able to hold values and are able to be identified by ''.

# 13. What is the difference between lists and tuples?
# A list is identifed with [] and is mutable, while a tuple is identifed with () and is immutable.

# 14. How do you type the tuple value that has just the integer value 42 in it?
# tuple = (42,)

# 15. How can you get the tuple form of a list value? How can you get the list form of a tuple value?
# tuple([]) and list(())

# 16. Variables that "contain" list values don't actually contain lists directly. What do they contain instead?
# They contain references to the lists.

# 17. What is the difference between copy.copy() and copy.deepcopy()?
# copy.copy() copies the value to a variable, and copy.deepcopy() copies the value to a variable while keeping it a list.

# Practice Project: Comma Code

print('Comma Code')
def commacode(listElem):
    listString = ''
    for x in listElem:
        if (listElem.index(x) == len(listElem) - 2):
            listString += x + ', and '
        elif (listElem.index(x) == len(listElem) - 1):
            listString += x
        else:
            listString += x + ', '
    return listString

spam = ['apples', 'bananas', 'tofu', 'cats']
spamString = commacode(spam)
print(spamString)

print()

# Practice Project: Character Picture Grid

print('Character Picture Grid')
grid = [['.', '.', '.', '.', '.', '.'],
        ['.', '0', '0', '.', '.', '.'],
        ['0', '0', '0', '0', '.', '.'],
        ['0', '0', '0', '0', '0', '.'],
        ['.', '0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '0', '.'],
        ['0', '0', '0', '0', '.', '.'],
        ['.', '0', '0', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

def printGrid(grid):
    coordY = 0
    while coordY < 6:
        coordX = 0
        while coordX < 9:
            print(grid[coordX][coordY], end=' ')
            coordX += 1
        print('\n')
        coordY += 1

printGrid(grid)
