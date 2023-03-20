# Description: Python program to display the Fibonacci sequence
# Author: Aman Mughal

def calculate_fibonacci_recursive(n: int) -> int:
    if n <= 1:
        return n
    else:
        return calculate_fibonacci_recursive(n - 1) + calculate_fibonacci_recursive(n - 2)

nterms = int(input("Enter the number of terms: "))
result = calculate_fibonacci_recursive(nterms)

print(f"The Fibonacci number of the terms {nterms} is {result}.")

print("The Fibonacci sequence is: ")
for i in range(nterms + 1):
    print(calculate_fibonacci_recursive(i))
