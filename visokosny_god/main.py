print("Enter a Year")
year = int(input())


def is_year_leap (year):
    if year % 4 != 0:
        print("False")
    else:
        print("True")



print(is_year_leap(year))
