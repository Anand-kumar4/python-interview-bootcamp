# ✅ Problem 10: Check if Two Strings Are Anagrams

# 🧠 Problem Statement:
# Write a function that returns True if two strings are anagrams, and False otherwise.

def check_anagram(str1, str2):
    """
    Check if two strings are anagrams using sorting.

    Parameters:
    str1 (str): First string
    str2 (str): Second string

    Returns:
    bool: True if anagrams, False otherwise
    """
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    return sorted(str1) == sorted(str2)


from collections import Counter

def check_anagram_counter(str1, str2):
    """
    Check if two strings are anagrams using Counter (character frequency).

    Parameters:
    str1 (str): First string
    str2 (str): Second string

    Returns:
    bool: True if anagrams, False otherwise
    """
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    return Counter(str1) == Counter(str2)


# 🧪 Test Cases
if __name__ == "__main__":
    # Using sorting
    print("Sorting:", check_anagram("listen", "silent"))    # True
    print("Sorting:", check_anagram("Hello", "Olelh"))      # True
    print("Sorting:", check_anagram("Test", "Taste"))       # False

    # Using Counter
    print("Counter:", check_anagram_counter("listen", "silent"))    # True
    print("Counter:", check_anagram_counter("Hello", "Olelh"))      # True
    print("Counter:", check_anagram_counter("Test", "Taste"))       # False