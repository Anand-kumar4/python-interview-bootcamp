# ✅ Problem 2: Sum of Digits

# 🧠 Problem Statement:

# Write a function that takes a positive integer n and returns the sum of its digits.

def sum_of_digits(n):
    n = abs(n)
    total = 0
    while n > 0:
        last_digit = n % 10
        total = total + last_digit
        n = n // 10
    return total

print(sum_of_digits(-123))  # Expected: 6
print(sum_of_digits(987))  # Expected: 24
