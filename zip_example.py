countries = ['USA', 'Canada', 'Mexico']
filenames = ["a.txt", "b.txt", "c.txt"]

for content, filename in zip(countries, filenames):
    file = open(filename, "w")
    file.write(content)
    file.close()
