# ✅ Problem 13: Find the Second Largest Number

# 🧠 Problem Statement:

# Write a function that returns the second largest unique number in a list.


# Solution 1: Sorting + Set approach
def second_largest_sorted(lst):
    """
    Finds the second largest unique number using set and sorting.

    Parameters:
    lst (list): List of numbers

    Returns:
    int or None: Second largest unique number or None if not found
    """
    uniques = sorted(set(lst))
    return uniques[-2] if len(uniques) >= 2 else None


# Solution 2: Manual traversal approach
def second_largest_manual(lst):
    """
    Finds the second largest unique number by manually tracking max and second max.

    Parameters:
    lst (list): List of numbers

    Returns:
    int or None: Second largest unique number or None if not found
    """
    first = second = float('-inf')
    seen = set()
    for num in lst:
        if num in seen:
            continue
        seen.add(num)
        if num > first:
            second = first
            first = num
        elif num > second:
            second = num
    return second if second != float('-inf') else None


# 🧪 Test Cases
if __name__ == "__main__":
    data = [
        [1, 3, 4, 5, 0],          # → 4
        [10, 10, 9],              # → 9
        [5],                      # → None
        [1, 2, 3, 3, 2, 1],       # → 2
        [100, 90, 90, 80],        # → 90
    ]

    print("Using Sorted Set Approach:")
    for lst in data:
        print(f"{lst} → {second_largest_sorted(lst)}")

    print("\nUsing Manual Traversal Approach:")
    for lst in data:
        print(f"{lst} → {second_largest_manual(lst)}")