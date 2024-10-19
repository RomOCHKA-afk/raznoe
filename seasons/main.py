def season(month_number):
    if month_number == 12 or month_number == 1 or month_number == 2:
        return "Winter"
    elif month_number == 3 or month_number == 4 or month_number == 5:
        return "Spring"
    elif month_number == 6 or month_number == 7 or month_number == 8:
        return "Summer"
    elif month_number == 9 or month_number == 10 or month_number == 11:
        return "Autumn"
    else:
        return "Enter a valid month"

while True:
    input_user = input("Enter a month or exit:")

    if input_user == 'exit':
        break

    try:
        month_number = int(input_user)
        print(season(month_number))
    except ValueError:
        print("Enter a valid number:")