'''
version 1:

cups = input("Enter the number of cups of flour: ")
print("To double your recipe you need", cups + cups, "cups of flour.")
'''

cups = int(input("Enter the number of cups of flour: "))
print("To double your recipe you need", cups + cups, "cups of flour.")

"""
Failed version:

print("To double your recipe you need " + cups + cups + " cups of flour.")
"""

print("To double your recipe you need " + str(cups + cups) + " cups of flour.")