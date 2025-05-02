




























def multiply_numbers(x, y):
  """
  This function multiplies two numbers and returns the result.
  """
  product = x * y
  return product

# Get input from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Multiply the numbers
result = multiply_numbers(num1, num2)

# Print the result
print("The product of", num1, "and", num2, "is", result)