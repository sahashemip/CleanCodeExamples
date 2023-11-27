# factorial.py
# This script calculates the factorial of a given number.

def calculate_factorial(number):
    """
    Calculate the factorial of a number.

    Args:
    number (int): The number to calculate the factorial of.

    Returns:
    int: The factorial of the number.
    """
    if number < 0:
        return "Factorial not defined for negative numbers"
    elif number == 0 or number == 1:
        return 1
    else:
        factorial = 1
        for i in range(2, number + 1):
            factorial *= i
        return factorial

def main():
    try:
        number = int(input("Enter a number to calculate its factorial: "))
        result = calculate_factorial(number)
        print(f"The factorial of {number} is {result}")
    except ValueError:
        print("Please enter a valid integer.")
