result=0
print("Введите первое число:")
x = float(input())
print("Введите знак операции:")
operatsiya = input()
print("Введите второе число:")
y = float(input())

def arithmetic (x,y,operatsiya):

    if (operatsiya) == "+":
        result = (x+y)
        print("=", result)
    elif (operatsiya) == "-":
        result = (x-y)
        print("=", result)
    elif (operatsiya) == "*":
        result = (x*y)
        print("=", result)
    elif (operatsiya) ==  "/":
        if y==0:
            print("DOLBOEB")
        result = (x/y)
        print("=", result)
    else:
        print("Неправильная операция")

arithmetic(x,y,operatsiya)








