# ✅ Problem 4: Largest of Three Numbers

# 🧠 Problem Statement:

# Write a function that takes three integers and returns the largest among them.

# ⸻

def largest_of_three(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c
    

print(largest_of_three(10, 25, 3))