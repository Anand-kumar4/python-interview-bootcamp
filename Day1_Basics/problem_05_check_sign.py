# ✅ Problem 5: Check if a Number is Positive, Negative, or Zero

# 🧠 Problem Statement:

# Write a function that:
# 	•	Takes an integer n
# 	•	Returns:
# 	•	"Positive" if n > 0
# 	•	"Negative" if n < 0
# 	•	"Zero" if n == 0


def check_sign(n):
    if n > 0:
        return "Positive"
    elif n == 0:
        return "Zero"
    else:
        return "Negative"
    

print(check_sign(10))
print(check_sign(-1))
print(check_sign(0))