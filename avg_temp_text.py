def get_avgerage():
    with open('files/numbers.txt', 'r') as file:
        data = file.readlines()
    values = data[1:]
    values = [float(value) for value in values]
    return values

average = get_avgerage()
print(average)