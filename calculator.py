














def subtract_numbers(num1, num2):
  """Subtracts two numbers and returns the result."""
  difference = num1 - num2
  return difference

# Get input from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Call the function and print the result
result = subtract_numbers(num1, num2)
print("The difference is:", result)