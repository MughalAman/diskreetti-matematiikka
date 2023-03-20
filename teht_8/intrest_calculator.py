# Description: Python program to calculate the interest for your savings
# Author: Aman Mughal

# Function to calculate the the balance after a certain number of years with a given interest rate

def calculate_balance_after_years_recursive(balance: float, interest_rate: float, years: int) -> float:
    # Check if the number of years is 0
    # If it is, return the balance
    # Otherwise, calculate the balance after one year and call the function again with the number of years subtracted by 1

    if years == 0:
        return balance
    else:
        balance = balance * (1 + interest_rate)
        return calculate_balance_after_years_recursive(balance, interest_rate, years - 1)

balance_str = input("Enter The starting balance e.g 1000 usd: ")
balance = float(balance_str.split(" ")[0])
currency = balance_str.split(" ")[1]
interest_rate = float(input("Enter the interest rate %: ")) / 100
years = int(input("Enter the number of years: "))

result = calculate_balance_after_years_recursive(balance, interest_rate, years)

print(f"The balance after {years} years is {result} {currency}.")

def calculate_balance_after_years_non_recursive(balance: float, interest_rate: float, years: int) -> float:
    # Calculate the balance after a certain number of years with a given interest rate
    balance = balance * (1 + interest_rate) ** years
    return balance

balance_str = input("Enter The starting balance e.g 1000 usd: ")
balance = float(balance_str.split(" ")[0])
currency = balance_str.split(" ")[1]
interest_rate = float(input("Enter the interest rate %: ")) / 100
years = int(input("Enter the number of years: "))

result = calculate_balance_after_years_non_recursive(balance, interest_rate, years)

print(f"The balance after {years} years is {result} {currency}.")