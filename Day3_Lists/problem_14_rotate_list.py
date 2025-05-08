# ✅ Problem 14: Rotate List to the Right by k Steps

# 🧠 Problem Statement:

# Given a list and an integer k, rotate the list to the right by k steps.

def rotate_list(lst, k):
    """
    Rotates the input list to the right by k steps.

    Parameters:
    lst (list): The input list to be rotated.
    k (int): Number of steps to rotate the list.

    Returns:
    list: The rotated list.
    """
    # Return early for empty list, no rotation, or single-element list
    if not lst or k == 0 or len(lst) <= 1:
        return lst

    k = k % len(lst)  # Normalize k to avoid extra rotations
    rotated = lst[-k:] + lst[:-k]  # Slice and rearrange
    return rotated


# 🧪 Test Cases
if __name__ == "__main__":
    print("Test 1:", rotate_list([1, 2, 3, 4, 5], 2))   # Expected: [4, 5, 1, 2, 3]
    print("Test 2:", rotate_list([10, 20, 30], 1))      # Expected: [30, 10, 20]