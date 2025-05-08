# ✅ Problem 9: Remove Non-Alphanumeric Characters

# 🧠 Problem Statement:
# Write a function that removes all characters from a string except letters and digits.

# 🔁 Version 1: Preserves case
def clean_string(s):
    """
    Removes all non-alphanumeric characters from the string.
    Preserves the original casing.

    Parameters:
    s (str): Input string

    Returns:
    str: Cleaned string with only alphanumeric characters
    """
    return "".join([c for c in s if c.isalnum()])


# 🔁 Version 2: Also converts to lowercase (optional normalization)
def clean_string_lowercase(s):
    """
    Removes all non-alphanumeric characters and converts the string to lowercase.

    Parameters:
    s (str): Input string

    Returns:
    str: Cleaned and lowercased string with only alphanumeric characters
    """
    return "".join([c.lower() for c in s if c.isalnum()])


# 🧪 Test Cases
if __name__ == "__main__":
    print("Preserve Case:", clean_string("Hello, World!"))         # → HelloWorld
    print("Preserve Case:", clean_string("123@#Python!_rocks"))    # → 123Pythonrocks

    print("Lowercase:", clean_string_lowercase("Hello, World!"))         # → helloworld
    print("Lowercase:", clean_string_lowercase("123@#Python!_rocks"))    # → 123pythonrocks