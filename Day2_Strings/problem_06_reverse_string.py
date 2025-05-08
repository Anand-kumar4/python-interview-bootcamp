# ✅ Problem 6: Reverse a String

# 🧠 Problem Statement:
# Write a function that takes a string s and returns the reversed string.

# 🔁 Approach 1: Using slicing
def reverse_string(s):
    """
    Reverses a string using slicing.

    Parameters:
    s (str): Input string

    Returns:
    str: Reversed string
    """
    return s[::-1]

# 🔁 Approach 2: Using a loop
def reverse_string1(s):
    """
    Reverses a string by prepending characters in a loop.

    Parameters:
    s (str): Input string

    Returns:
    str: Reversed string
    """
    reversed_str = ""
    for char in s:
        reversed_str = char + reversed_str
    return reversed_str


# 🧪 Test Cases
if __name__ == "__main__":
    print("Slicing:", reverse_string("anand"))     # Expected: dnana
    print("Slicing:", reverse_string("Python"))    # Expected: nohtyP

    print("Loop:", reverse_string1("anand"))       # Expected: dnana
    print("Loop:", reverse_string1("Python"))      # Expected: nohtyP