#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calculate the factorial of a given number using recursion.
    
    Function Description:
    This function computes the factorial of a non-negative integer using
    recursive approach. The factorial of n (denoted as n!) is the product
    of all positive integers less than or equal to n. By definition, 0! = 1.
    The function uses the mathematical property that n! = n × (n-1)!
    
    Parameters:
    n (int): A non-negative integer for which to calculate the factorial.
             Must be >= 0 to avoid infinite recursion.
    
    Returns:
    int: The factorial of the input number n. Returns 1 if n is 0,
         otherwise returns n multiplied by the factorial of (n-1).
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Get the number from command line argument and calculate its factorial
f = factorial(int(sys.argv[1]))
print(f)
