# ✅ Problem 16: Frequency Dictionary

# 🧠 Problem Statement:

# Write a function that takes a list and returns a dictionary where:
# 	•	Each key is a unique item from the list
# 	•	Each value is the number of times that item appears


# Approach 1
def count_frequency(lst):
    """
    Counts the frequency of each element in the list using a manual dictionary approach.

    Parameters:
    lst (list): A list of elements (can be strings, numbers, etc.)

    Returns:
    dict: A dictionary with each unique element as key and its count as value
    """
    freq = {}
    for item in lst:
        if item in freq:
            freq[item] += 1
        else:
            freq[item] = 1
    return freq

# Approach 2
from collections import defaultdict

def count_frequency2(lst2):
    """
    Counts the frequency of each element in the list using collections.defaultdict.

    Parameters:
    lst2 (list): A list of elements (can be strings, numbers, etc.)

    Returns:
    dict: A dictionary with each unique element as key and its count as value
    """
    freq2 = defaultdict(int)
    for item2 in lst2:
        freq2[item2] += 1
    return dict(freq2)


# 🧪 Test Cases
if __name__ == "__main__":
    print("Approach 1 Tests:")
    print(count_frequency(['a', 'b', 'a', 'c', 'b', 'a']))  # Expected: {'a': 3, 'b': 2, 'c': 1}
    print(count_frequency([1, 2, 2, 3, 1, 4]))              # Expected: {1: 2, 2: 2, 3: 1, 4: 1}

    print("\nApproach 2 Tests:")
    print(count_frequency2(['a', 'b', 'a', 'c', 'b', 'a']))  # Expected: {'a': 3, 'b': 2, 'c': 1}
    print(count_frequency2([1, 2, 2, 3, 1, 4]))              # Expected: {1: 2, 2: 2, 3: 1, 4: 1}

