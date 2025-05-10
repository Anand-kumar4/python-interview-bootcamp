# ✅ Problem 19: Find Intersection of Two Lists

# 🧠 Problem Statement:

# Write a function that returns the common elements between two lists. The result should not contain duplicates.

# ✅ Constraints:
# 	•	Order doesn’t matter
# 	•	Result can be a list (sorted or not)
# 	•	Should not include duplicates
"""
✅ Problem 19: Find Intersection of Two Lists

🧠 Problem Statement:
Write a function that returns the common elements between two lists.
The result should not contain duplicates.
"""

def intersection(list1, list2):
    """
    Returns the list of common elements between two input lists, with duplicates removed.

    Parameters:
    list1 (list): First input list
    list2 (list): Second input list

    Returns:
    list: List of elements present in both input lists, without duplicates
    """
    set1 = set(list1)
    set2 = set(list2)
    result_set = set1.intersection(set2)
    result_list = list(result_set)
    return result_list


# 🧪 Test Cases
if __name__ == "__main__":
    print("Test 1:", intersection([1, 2, 2, 3], [2, 3, 4]))   # Expected: [2, 3]
    print("Test 2:", intersection(['a', 'b'], ['b', 'c']))    # Expected: ['b']