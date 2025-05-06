# ✅ Problem 1: Even or Odd

# 🧠 Problem Statement:

# Write a function that:
# 	•	Takes an integer n as input
# 	•	Returns "Even" if the number is divisible by 2
# 	•	Returns "Odd" otherwise


def is_even(n):
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"

print(is_even(4))   # Expected: Even
print(is_even(9))   # Expected: Odd