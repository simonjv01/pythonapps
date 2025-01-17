def get_age(year_of_birth, current_year=2025):
    age = current_year - year_of_birth
    return age

print(get_age(1974))

print(get_age(1990, 2023))


