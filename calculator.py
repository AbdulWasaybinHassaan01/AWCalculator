Division















































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
=======
Multiplication





























def multiply_numbers(x, y):
  """
  This function multiplies two numbers and returns the result.
  """
  product = x * y
  return product
=======

Subtraction















def subtract_numbers(num1, num2):
  """Subtracts two numbers and returns the result."""
  difference = num1 - num2
  return difference
=======

def add_numbers(num1, num2):
  """Adds two numbers and returns the sum."""
  return num1 + num2

Addition
Addition

# Get input from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

Multiplication
# Multiply the numbers
result = multiply_numbers(num1, num2)

# Print the result
print("The product of", num1, "and", num2, "is", result)
=======

Subtraction
# Call the function and print the result
result = subtract_numbers(num1, num2)
print("The difference is:", result)
=======

# Calculate the sum
sum_of_numbers = add_numbers(num1, num2)

# Display the result
print("The sum of", num1, "and", num2, "is:", sum_of_numbers)
Addition
Addition
Addition
