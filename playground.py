#print("hello " + input("What is your name?"))
#
# name = input("What is your name?")
#
# print(name)


# print(len(input("What is your name?")))

weight = float(input("What is your weight in kg?"))
height = float(input("What is your height in m?"))

bmi = weight / height ** 2
print(bmi)

print(round(bmi, 2))
