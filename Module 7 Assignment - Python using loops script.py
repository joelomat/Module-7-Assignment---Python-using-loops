# Assignment: Create a list of 15 numbers and print whether each is odd or even
# Author: [Your Name]
# Date: July 27, 2025
# Purpose: Demonstrate use of for loop and conditional statements to identify odd/even numbers

# Create a list of 15 numbers (1 to 15)
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

# Iterate through each number in the list
for number in numbers:
    # Check if number is even using modulo operator
    if number % 2 == 0:
        print(str(number) + " is even")
    else:
        print(str(number) + " is odd")
