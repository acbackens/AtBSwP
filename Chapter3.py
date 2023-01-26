# 1. Why are functions advantageous to have in your programs?
# Functions help reduce the amount of code that you have to repeat and can do repetitive tasks very quickly
#
# 2. When does the code in a function execute: when the function is defined or when the function is called?
# When the function is called
#
# 3. What statement creates a function?
# def function()
#
# 4. What is the different between a function and a function call?
# A function defines what it does, and a function call executes the function
#
# 5. How many global scopes are there in a Python program? How many local scopes?
# There is 1 global scope, and an infinite number of local scopes
#
# 6. What happens to variables in a local scope when the function call returns?
# The values terminate
#
# 7. What is a return value? Can a return value be part of an expression?
# A return value is a value that a function outputs. A return value cannot be part of an expression.
#
# 8. If a function does not have a return statement, what is the return value of a call to that function?
# None
#
# 9. How can you force a variable in a function to refer to the global variable
# The global keyword, like 'global variable'
#
# 10. What is the data type of None?
# NoneType
#
# 11. What does the import areallyourpetsnamederic statement do?
# Imports the areallyourpetsnamederic module in order to use the functions from it
#
# 12. If you had a function named bacon() in a module named spam, how would you call it after importing spam?
# spam.bacon()
#
# 13. How can you prevent a program from crashing when it gets an error?
# Use the except function to catch these errors, like: except(GenericError): print('Error!')
#
# 14. What goes in the try clause? What goes in the except clause?
# The function goes in the try clause, while the output statement, when it errors, goes in the except clause
#
# The Collatz Sequence
def collatz(num):
    if num % 2 == 0:
        num = num // 2
        print(num)
        return num
    elif num % 2 == 1:
        num = 3 * num + 1
        print(num)
        return num

print('Enter number:')
try:
    number = int(input())
except ValueError:
    print('Please enter an integer!')
    number = int(input())
while number != 1:
    number = collatz(number)
