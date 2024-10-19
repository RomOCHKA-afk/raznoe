def is_prime(chislo):
    if chislo < 2:
        return False
    for d in range(2, int(chislo**0.5) + 1):
        if chislo % d == 0:
            return False
    return True

chislo = int(input('Введите число от 0 до 1000:'))
if chislo <= 1000:
    print(is_prime(chislo))
else:
    print("Число должно быть меньше или равно 1000.")
