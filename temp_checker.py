def temp_checker(temp):
    if temp > 25:
        return "Hot"
    elif temp > 15:
        return "Warm"
    elif temp >= 5:
        return "Cold"
    else:
        return "Freezing"

print(temp_checker(30))
