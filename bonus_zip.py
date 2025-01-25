contents = ["this is pretty cool", "python is interesting", "pandas is fun"]

filenames = ["RawData.txt", "Reports.txt", "Presentation.txt"]

for content, filename in zip(contents, filenames):
    file = open(r"files/" + filename, "w") 
    file.write(content)

    print(f"{filename} has been created with the following content: {content}")