# ✅ Problem 3: Swap Two Numbers (No Temp Variable)

# 🧠 Problem Statement:

# Write a function that takes two integers and returns them swapped, without using a third (temporary) variable.

def swap_numbers(a, b):
    a, b = b, a
    return a,b

a, b = swap_numbers(10, 20)
print("a:", a, "b:", b) 