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

def get_maximum():
    """
    Returns the maximum temperature in Celsius from a predefined list.

    :return: Maximum temperature in Celsius
    :rtype: float
    """
    celsius = [14, 15.1, 12.3]
    maximum = max(celsius)
    return maximum


celsius = get_maximum()

fahrenheit = celsius * 1.8 + 32

print(fahrenheit)