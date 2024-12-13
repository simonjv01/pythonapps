date = input("Enter today's date: ")
mood = input("How do you rate your mood today from 1 to 10? ")
journal = input("Write your journal entry: \n")

with open(f"../pythonapps/journal/{date}.txt", "w") as file:
    file.write(f"Date: {date}\n")
    file.write(f"Mood: {mood}\n")
    file.write(f"Journal: {journal}\n")
    file.write("\n")

print("Journal entry saved successfully!")