# password = input("Enter your password: ")

# result = {}

# if len(password) >= 8:
#     result["length"] = True
# else:
#     result["length"] = False

# digit = False

# for i in password:
#     if i.isdigit():
#         digit = True

# result["digits"] = digit

# uppercase = False

# for i in password:
#     if i.isupper():
#         uppercase = True

# result["uppercase"] = uppercase

# print(result)
# print(result.values())

# if all(result.values()):
#     print("Password is valid")
# else:
#     print("Password is invalid")
# The code above is a simple password validator. It checks if the password is at least 8 characters long, contains a digit, and contains an uppercase letter. If all conditions are met, the password is considered valid. Otherwise, it is considered invalid. The code uses a list called result to keep track of the validation results for each condition. The all() function is used to check if all elements in the result list are True, indicating that all conditions are met. Depending on the validation result, the code prints either "Password is valid" or "Password is invalid".

def strength(password):
    if len(password) < 8:
        return "Weak Password"
    if any(char.isupper() for char in password) is False:
        return "Weak Password"
    if any(char.isdigit() for char in password) is False:
        return "Weak Password"
    return "Strong Password"

password = input("Enter your password: ")
print(strength(password))
# The code above is a password strength checker. It checks if the password is at least 8 characters long, contains an uppercase letter, and contains a digit. If any of these conditions are not met, the password is considered weak. Otherwise, it is considered strong. The code uses the any() function to check if any character in the password meets the specified condition. Depending on the password strength, the code returns either "Weak Password" or "Strong Password".

