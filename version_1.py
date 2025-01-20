# My first program, made in 2020
# I was 15 and learned from YouTube and Stack Overflow

operators = ["+", "-", "*", "/"]

# First input: first number
while True:
    try:
        number_1 = float(input("Number 1: "))
        break  # No error -> Correct input typing
    except ValueError:  # Catching incorrect input typing
        print("Input must be an integer or a float.\n")

# Second input: second number
while True:
    try:
        number_2 = float(input("Number 2: "))
        break  # No error -> Correct input typing
    except ValueError:  # Catching incorrect input typing
        print("Input must be an integer or a float.\n")

# Third input: operator
operation = input("Operation: ")
while operation not in operators:
    print(f"Input must be one of the following operators:", operators)
    operation = input("Operation: ")

# Checking what to do based on the operation
if operation == "+":
    number_1 += number_2
elif operation == "-":
    number_1 -= number_2
elif operation == "*":
    number_1 *= number_2
elif operation == "/":
    number_1 /= number_2

# Printing out the final result
print("Result:", round(number_1, 4))
