deposit = float(input('Введите сумму вклада:'))
years = float(input('Введите срок вклада:'))
stavka=0.1

def bank(deposit, years,stavka):
    result = (deposit * (1+stavka) ** years)
    return result


print(f'Сумма на счете: {bank(deposit, years, stavka):.2f} рублей')