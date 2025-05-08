# ✅ Problem 15: Flatten a Nested List

# 🧠 Problem Statement:

# Write a function that takes a nested list (a list that may contain other lists) and returns a flattened list with all values in a single list.

def flatten(nested_list):
    """
    Recursively flattens a nested list into a single-level list.

    Parameters:
    nested_list (list): The input nested list

    Returns:
    list: A flattened list containing all values
    """
    result = []

    def helper(sublist):
        for element in sublist:
            if isinstance(element, list):
                helper(element)
            else:
                result.append(element)

    helper(nested_list)
    return result

# 🧪 Test Cases
if __name__ == "__main__":
    print(flatten([1, [2, 3], [4, [5, 6]]]))      # → [1, 2, 3, 4, 5, 6]
    print(flatten([[1, 2], 3, [[4], 5]]))         # → [1, 2, 3, 4, 5]