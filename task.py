# print(6 + 4 / 2 - (1 * 2))
#
# print(7 + 9)
#
# a = int("5") / int(2.7)
# print(type(a))
#
# # print a list
# print([1, 2, 3, 4, 5])

# for item in ["sandals", "glasses", "trousers"]:
#     print(item.capitalize())

# colors = [11, 34, 98, 43, 45, 54, 54]
# for color in colors:
#     if color > 50:
#         print(color)

# filenames = ["report.txt", "records.txt", "data.txt", "file.txt"]
# for filename in filenames:
#     if filename.endswith(".txt"):
#         name = filename[:-4]
#         print(name.capitalize())

# def format_filename():
#     filename = "report.txt"
#     new_filename = filename[0:6]
#     name = new_filename.capitalize()
#     return name
    
# print(format_filename())

# def get_maximum():
#     """
#     Returns the maximum temperature in Celsius from a predefined list.

#     :return: Maximum temperature in Celsius
#     :rtype: float
#     """
#     celsius = [14, 15.1, 12.3]
#     maximum = max(celsius)
#     return maximum


# celsius = get_maximum()

# fahrenheit = celsius * 1.8 + 32

# print(fahrenheit)

feet_inches = input("Enter your height in feet and inches: ")

def convert_feet_to_inches(feet_inches):
    feet, inches = feet_inches.split(" ")
    print(feet, inches)
    feet = int(feet)
    inches = int(inches)
    total_inches = (feet * 12) + inches
    return total_inches

def convert_feet_to_meters(feet_inches_in_meters):
    # parts = feet_inches_in_meters.split(" ")
    # print(parts)
    feet, inches = feet_inches_in_meters.split(" ")
    feet = float(feet[0])
    inches = float(inches[0:2])
    print(feet, inches)
    meters = (feet * 0.3048) + (inches * 0.0254)
    return meters

height= convert_feet_to_inches(feet_inches)

# height in meters
height_in_meters = convert_feet_to_meters(feet_inches)
print(f"Your height in meters is {height_in_meters}")

print(f"Your height in inches is {height}")
