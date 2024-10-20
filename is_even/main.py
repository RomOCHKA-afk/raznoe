def is_even(a):
    if a % 2 == 0:
        return True
    else:
        return False

a = int(input('Enter a num: '))
print(is_even(a))