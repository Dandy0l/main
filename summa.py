num = int(input('Введите число: '))
summ = 0

while num != 0:
    lst_num = num % 10
    summ += lst_num
    if lst_num == 5:
        print('Обнаружен разрыв.')
        break
    num //= 10
    print('Текущая сумма цифр:', summ)
    print()
print('\nИтоговая сумма цифр:', summ)
