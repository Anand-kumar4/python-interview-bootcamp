"""
✅ Problem 21: Tuple Unpacking and Swapping

🧠 Problem Statement:
Write a function that takes two numbers, unpacks them using tuple unpacking, and returns them in swapped order.
"""


def swap(a, b):
    """
    Swaps two input values using tuple unpacking.

    Parameters:
    a (any): First value
    b (any): Second value

    Returns:
    tuple: Swapped values as a tuple (b, a)
    """
    a, b = b, a
    return a, b


# 🧪 Test Cases
if __name__ == "__main__":
    print("Test 1:", swap(5, 10))     # Expected: (10, 5)
    print("Test 2:", swap(-1, 7))     # Expected: (7, -1)
