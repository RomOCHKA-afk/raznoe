def stroka(s):
    return {char: s.count(char) for char in s}

s = input("Введите строку: ")
print(stroka(s))
