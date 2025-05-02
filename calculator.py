def add_numbers(num1, num2):
  """Adds two numbers and returns the sum."""
  return num1 + num2

# Get input from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Calculate the sum
sum_of_numbers = add_numbers(num1, num2)

# Display the result
print("The sum of", num1, "and", num2, "is:", sum_of_numbers)