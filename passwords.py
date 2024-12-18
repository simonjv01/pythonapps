password = input("Enter your password: ")

result = []

if len(password) >= 8:
    result.append(True)
else:
    result.append(False)

digit = False

for i in password:
    if i.isdigit():
        digit = True

result.append(digit)

uppercase = False

for i in password:
    if i.isupper():
        uppercase = True

result.append(uppercase)

if all(result) == True:
    print("Password is valid")
else:
    print("Password is invalid")
# The code above is a simple password validator. It checks if the password is at least 8 characters long, contains a digit, and contains an uppercase letter. If all conditions are met, the password is considered valid. Otherwise, it is considered invalid. The code uses a list called result to keep track of the validation results for each condition. The all() function is used to check if all elements in the result list are True, indicating that all conditions are met. Depending on the validation result, the code prints either "Password is valid" or "Password is invalid".



