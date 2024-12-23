def calculate_average(filename_local):
    numbers = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                try:
                    number = float(line.strip()) # Convert the line to a float
                    numbers.append(number) # Add the number to the list
                except ValueError:
                    print(f"Skipping invalid input: {line.strip()}") # Print an error message

        if numbers:
            return sum(numbers) / len(numbers)
        else:
            return 0

    except FileNotFoundError:
        print(f"File not found: {filename}")
        return 0


filename = "../pythonapps/files/numbers.txt"
result = calculate_average(filename)
print(f"The average of the numbers in the {filename} is: {result}")
