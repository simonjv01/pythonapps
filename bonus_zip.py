contents = ["all carrots are to be sliced", "all onions are to be diced", "all potatoes are to be mashed"]

filenames = ["RawData.txt", "Reports.txt", "Presentation.txt"]

for content, filename in zip(contents, filenames):
    file = open(r"files/" + filename, "w") 
    file.write(content)

    print(f"{filename} has been created with the following content: {content}")