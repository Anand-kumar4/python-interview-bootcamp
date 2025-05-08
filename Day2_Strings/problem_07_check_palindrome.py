# ✅ Problem 7: Palindrome Check

# 🧠 Problem Statement:
# Write a function that returns True if the string is a palindrome (same forward and backward), and False otherwise.
# Implement three versions:
#   1. Case-sensitive check
#   2. Case-insensitive check
#   3. Ignore case and non-alphanumeric characters

# 🔁 Version 1: Case-Sensitive
def is_palindrome(s):
    return s == s[::-1]

# 🔁 Version 2: Case-Insensitive
def is_palindrome_case_insensitive(s):
    s = s.lower()
    return s == s[::-1]

# 🔁 Version 3: Ignore Case + Non-Alphanumeric
def is_palindrome_cleaned(s):
    filtered = "".join([c.lower() for c in s if c.isalnum()])
    return filtered == filtered[::-1]

# 🧪 Test Cases
if __name__ == "__main__":
    print("Version 1:", is_palindrome("madam"))            # True
    print("Version 1:", is_palindrome("hello"))            # False
    
    print("Version 2:", is_palindrome_case_insensitive("RaceCar"))  # True
    print("Version 2:", is_palindrome_case_insensitive("Hello"))    # False
    
    print("Version 3:", is_palindrome_cleaned("A man, a plan, a canal: Panama"))  # True
