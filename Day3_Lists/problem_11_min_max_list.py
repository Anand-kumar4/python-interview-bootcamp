# ✅ Problem 11: Find Minimum and Maximum in a List

# 🧠 Problem Statement:
# Write a function that returns the minimum and maximum values in a list.

def min_max(lst):
    """
    Finds the minimum and maximum values in a list.

    Parameters:
    lst (list): List of numeric values

    Returns:
    tuple: (min_value, max_value)
    """
    if not lst:
        raise ValueError("List must not be empty.")
        
    min_val = lst[0]
    max_val = lst[0]
    for item in lst[1:]:
        if item < min_val:
            min_val = item
        if item > max_val:
            max_val = item
    return (min_val, max_val)


# 🧪 Test Cases
if __name__ == "__main__":
    print("Test 1:", min_max([4, 2, 9, 1, 7]))     # Expected: (1, 9)
    print("Test 2:", min_max([-5, 0, 22, 3]))      # Expected: (-5, 22)