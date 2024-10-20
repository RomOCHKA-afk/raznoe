def sum_of_digits(n):
    return sum(int(digit) for digit in str(abs(n)))  # Преобразуем в строку, берем каждую цифру и суммируем

# Ввод данных
n = int(input("Введите число: "))

# Вызов функции и вывод результата
print(f"Сумма цифр числа {n}: {sum_of_digits(n)}")