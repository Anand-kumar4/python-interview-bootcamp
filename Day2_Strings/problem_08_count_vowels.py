# ✅ Problem 8: Count Vowels in a String

# 🧠 Problem Statement:
# Write a function that takes a string and returns the number of vowels in it.

def count_vowels(s):
    """
    Counts the number of vowels (a, e, i, o, u) in the input string (case-insensitive).
    
    Parameters:
    s (str): Input string

    Returns:
    int: Number of vowels
    """
    s = s.lower()
    vowels = set('aeiou')
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count


def count_vowels1(s):
    """
    Pythonic one-liner to count vowels in a string using generator expression.
    
    Parameters:
    s (str): Input string

    Returns:
    int: Number of vowels
    """
    return sum(1 for c in s.lower() if c in 'aeiou')


# 🧪 Test Cases
if __name__ == "__main__":
    print("Loop version:", count_vowels("anand"))       # Expected: 2
    print("Loop version:", count_vowels("Interview"))   # Expected: 4

    print("One-liner:", count_vowels1("anand"))         # Expected: 2
    print("One-liner:", count_vowels1("Interview"))     # Expected: 4