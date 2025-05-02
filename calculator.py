














































def divide_numbers(numerator, denominator):
    """Divides two numbers and returns the quotient.

    Args:
        numerator: The number to be divided.
        denominator: The number to divide by.

    Returns:
        The quotient of the division.

    Raises:
        ZeroDivisionError: If the denominator is zero.
    """
    if denominator == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return numerator / denominator

# Get input from the user
try:
    num1 = float(input("Enter the numerator: "))
    num2 = float(input("Enter the denominator: "))

    # Perform the division and print the result
    result = divide_numbers(num1, num2)
    print("The result of the division is:", result)

except ValueError:
    print("Invalid input. Please enter numbers only.")
except ZeroDivisionError as e:
    print(e)