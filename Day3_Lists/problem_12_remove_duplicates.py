# ✅ Problem 12: Remove Duplicates from a List

# 🧠 Problem Statement:
# Write a function that takes a list and returns a new list with all duplicates removed,
# preserving the original order of first occurrence.

def remove_duplicates(lst):
    """
    Removes duplicate elements from a list while preserving the original order.

    Parameters:
    lst (list): The input list which may contain duplicates.

    Returns:
    list: A list with duplicates removed, in original order.
    """
    seen = set()
    new_lst = []
    for item in lst:
        if item not in seen:
            seen.add(item)
            new_lst.append(item)
    return new_lst


# 🧪 Test Cases
if __name__ == "__main__":
    print("Test 1:", remove_duplicates([1, 2, 2, 3, 1]))     # Expected: [1, 2, 3]
    print("Test 2:", remove_duplicates(['a', 'b', 'a']))     # Expected: ['a', 'b']
