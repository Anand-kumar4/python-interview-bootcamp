# ✅ Problem 20: Remove Duplicates Using Set

# 🧠 Problem Statement:

# Write a function that removes all duplicates from a list using a set and returns a list with only unique elements.
"""
✅ Problem 20: Remove Duplicates Using Set

🧠 Problem Statement:
Write a function that removes all duplicates from a list using a set and returns a list with only unique elements.
"""

def remove_duplicates(lst):
    """
    Removes duplicates from a list using a set. Order is not preserved.

    Parameters:
    lst (list): The input list that may contain duplicates.

    Returns:
    list: A list containing unique elements.
    """
    unique = set(lst)
    result_list = list(unique)
    return result_list


# 🧪 Test Cases
if __name__ == "__main__":
    print("Test 1:", remove_duplicates([1, 2, 2, 3, 1]))   # Expected: [1, 2, 3] (order may vary)
    print("Test 2:", remove_duplicates(['a', 'b', 'a']))   # Expected: ['a', 'b'] or ['b', 'a']