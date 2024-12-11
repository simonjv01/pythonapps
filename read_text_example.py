# file = open("../pythonapps/a.txt", "r")
# a_file = file.read()
# file.close()
# print(a_file)

# file = open("./b.txt", "r")
# b_file = file.read()
# file.close()
# print(b_file)

# file = open("./c.txt", "r")
# c_file = file.read()
# file.close()
# print(c_file)

filenames = ['a.txt', 'b.txt', 'c.txt']

for filename in filenames:
    file = open(filename, 'r')
    content = file.read()
    print(content)