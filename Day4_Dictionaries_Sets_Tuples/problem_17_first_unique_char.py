"""
✅ Problem 17: First Non-Repeating Character

🧠 Problem Statement:
Write a function that returns the index of the first character in a string that does not repeat. 
If all characters repeat, return -1.
"""

def first_unique_char(s):
    """
    Returns the index of the first non-repeating character in the string.
    If all characters repeat, returns -1.

    Parameters:
    s (str): Input string

    Returns:
    int: Index of the first unique character or -1
    """
    freq = {}
    for char in s:
        freq[char] = freq.get(char, 0) + 1

    for index, char in enumerate(s):
        if freq[char] == 1:
            return index

    return -1


# 🧪 Test Cases
if __name__ == "__main__":
    print("Test 1:", first_unique_char("leetcode"))      # Expected: 0
    print("Test 2:", first_unique_char("aabbccdde"))     # Expected: 8
    print("Test 3:", first_unique_char("aabb"))          # Expected: -1