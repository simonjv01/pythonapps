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

print(result)


