languages = ['Python', 'Java', 'C++', 'Ruby', 'JavaScript']

for language in languages:
    with open(f"../pythonapps/languages/{language}.txt", "w") as file:
        file.write(f"Language: {language}\n")
        file.write(f"Type: Programming\n")
        file.write(f"Creator: Guido van Rossum\n")
        file.write("\n")