# Description: Calculate the factorial of a number
# Author: Aman Mughal

# Function to calculate the factorial of a number recursively
def calculate_factorial_recursive(n: int) -> int:
    # Check if the number is negative or zero
    # If it is negative, return None. if it is zero, return 1
    # Otherwise, return the number multiplied by the factorial of the number subtracted by 1

    if n == 0:
        return 1
    elif n < 0:
        return None
    else:
        return n * calculate_factorial_recursive(n - 1)


number = int(input("Enter a number to calculate its factorial: "))
result = calculate_factorial_recursive(number)

if result is None:
    print("Factorial of negative numbers is not defined.")
else:
    print(f"The factorial of {number} is {result}.")

def calculate_factorial_non_recursive(n: int) -> int:
    # Check if the number is negative or zero
    # If it is negative, return None. if it is zero, return 1
    #Otherwise calculate the factorial of the number using a for loop and return the result

    if n == 0:
        return 1
    elif n < 0:
        return None
    else:
        factorial = 1
        for i in range(1, n + 1):
            factorial *= i
        return factorial

number = int(input("Enter a number to calculate its factorial: "))
result = calculate_factorial_non_recursive(number)

if result is None:
    print("Factorial of negative numbers is not defined.")
else:
    print(f"The factorial of {number} is {result}.")