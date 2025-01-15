#!/usr/bin/python3
import sys

# Function Description:
# This function calculates the factorial of a given number n recursively.
# A factorial of a non-negative integer n is the product
# of all positive integers less than or equal to n.
# For example, factorial(5) = 5 * 4 * 3 * 2 * 1 = 120.


def factorial(n):
    # Parameters:
    # n (int): A non-negative integer whose factorial is to be calculated.

    # Returns:
    # int: The factorial of the given number n. If n is 0
    # , the result is 1 (since 0! = 1).

    if n == 0:
        return 1  # Base case: 0! = 1
    else:
        return n * factorial(n-1)  # Recursive case: n! = n * (n-1)!


# Get the input from the command line argument and calculate its factorial
f = factorial(int(sys.argv[1]))


# Print the result
print(f)
