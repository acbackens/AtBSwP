# 1. What are the two values of the Boolean data type? How do you write them?
# True, False
#
# 2. What are the three Boolean operators?
# and, or, not
#
# 3. Write out the truth tables of each Boolean operator (that is, every possible combination of Boolean values for the operator and what they evaluate to).
# True and True = True
# True and False = False
# False and False = False
# True or True = True
# True or False = True
# False or False = False
# not True = False
# not False = True
#
# 4. What do the following expressions evaluate to?
# (5 > 4) and (3 == 5) = False
# not (5 > 4) = False
# (5 > 4) or (3 == 5) = True
# not ((5 > 4) or (3 == 5)) = False
# (True and True) and (True == False) = False
# (not False) or (not True) = True
#
# 5. What are the six comparison operators?
# !, =, >, >=, <, <=
#
# 6. What is the difference between the equal to operator and the assignment operator?
# The equal to operator (==) checks the values between the two variables, and the assignment operator (=) assigns the value of the right variable to the left variable.
#
# 7. Explain what a condition is and where you would use one.
# A condition evaluates if a loop is True or False. It is used to prevent infinite loops.
#
# 8. Identify the three blocks in this code:
spam = 0
if spam == 10:
    print('eggs') # First block
    if spam > 5:
        print('bacon') # Second block
    else:
        print('ham') # Third block
    print('spam')
print('spam')
#
# 9. Write code that prints Hello if 1 is stored in spam, prints Howdy if 2 is stored in spam, and prints Greetings! if anything else is stored in spam.
spam = 0
if spam == 1:
    print('Hello')
elif spam == 2:
    print('Howdy')
else:
    print('Greetings!')
#
# 10. What can you press if your program is stuck in an infinite loop?
# Ctrl + C
#
# 11. What is the difference between break and continue?
# Break ends the loop, while Continue moves forward in the loop.
#
# 12. What is the difference between range(10), range(0, 10), and range(0, 10, 1) in a for loop?
# range(10) outputs 0 - 9
# range(0, 10) outputs 0 - 9
# range(0, 10, 1) outputs 0 - 9 and increments by 1
#
# 13. Write a short program that prints the numbers 1 - 10 using a for loop. Then write an equivalent program that prints the numbers 1 - 10 using a while loop.
for i in range(1, 11):
    print(i)

i = 1
while (i < 11):
    print (i)
    i = i + 1
#
# 14. If you had a function named bacon() inside a module named spam, how would you call it after importing spam?
import spam
spam.bacon()