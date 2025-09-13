def get_season(month):
    if month in (12, 1, 2):
        return "winter"
    elif month in (3, 4, 5):
        return "spring"
    elif month in (6, 7, 8):
        return "summer"
    elif month in (9, 10, 11):
        return "autumn"


user_input = int(input("Enter the number of a month (1-12): "))

if 1 <= user_input <= 12:
    season = get_season(user_input)
    print(f"You entered: {user_input}\nThe season is {season}.")
else:
    print(f"You entered: {user_input}\nPlease enter a number between 1 and 12.")