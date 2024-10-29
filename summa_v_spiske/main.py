user_input =input('Введите числа, разделенные пробелом:')
list1 = list(map(int, user_input.split()))

def sum_of_list(list1):
    return sum(list1)
print(sum_of_list(list1))