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

filenames = ["report.txt", "records.txt", "data.txt", "file.txt"]
for filename in filenames:
    if filename.endswith(".txt"):
        name = filename[:-4]
        print(name.capitalize())
