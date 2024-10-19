from math import sqrt
print("Введите сторону квадрата:")
side=float(input())
def square(side):
    perimetr=side*4
    s=side**2
    diag=side*sqrt(2)

    return(perimetr,s,diag)

print(square(side))
