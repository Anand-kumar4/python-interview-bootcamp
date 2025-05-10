"""
✅ Problem 18: Group Words by Their First Letter

🧠 Problem Statement:
Given a list of words, group them in a dictionary where:
• Each key is the first letter of a word
• Each value is a list of words that start with that letter
"""

# Approach 1: Using plain dictionary
def group_by_initial(words):
    """
    Groups words by their starting letter using a regular dictionary.

    Parameters:
    words (list): List of strings

    Returns:
    dict: Dictionary with first letter as keys and list of words as values
    """
    grouped = {}
    for word in words:
        first_letter = word[0]
        if first_letter in grouped:
            grouped[first_letter].append(word)
        else:
            grouped[first_letter] = [word]
    return grouped


# Approach 2: Using defaultdict
from collections import defaultdict

def group_by_initial_defaultdict(words):
    """
    Groups words by their starting letter using collections.defaultdict.

    Parameters:
    words (list): List of strings

    Returns:
    dict: Dictionary with first letter as keys and list of words as values
    """
    grouped = defaultdict(list)
    for word in words:
        grouped[word[0]].append(word)
    return dict(grouped)


# 🧪 Test Cases
if __name__ == "__main__":
    test_words = ["apple", "ant", "banana", "bat", "car"]

    print("Approach 1:", group_by_initial(test_words))
    print("Approach 2:", group_by_initial_defaultdict(test_words))