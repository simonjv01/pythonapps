def get_avgerage():
    with open('files/numbers.txt', 'r') as file:
        data = file.readlines()
    values = data[1:]
    values = [float(value) for value in values]

    average_local = sum(values) / len(values)
    avg_temp = round(average_local, 2)
    return avg_temp

average = get_avgerage()
print(average)