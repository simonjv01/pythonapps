filenames = ['doc.txt', 'report.txt', 'presentation.txt']

for filename in filenames:
    with open(filename, 'w') as file:
        file.write("Hello")
        print("Created file: " + filename)


# for filename in filenames:
#     file = open(filename, 'w')
#     file.write("Hello")
#     file.close()