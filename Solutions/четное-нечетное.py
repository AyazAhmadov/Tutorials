number = input('Please enter a number: ')

if number.isnumeric(): # Проверяем если введенное значение это целое число
    x = int(number)
    if x % 2 == 0: # Если остаток при делении числа на 2 равен 0, то число четное
        print(f'{x} is even')
    else: # В противном случае число нечетное
        print(f'{x} is odd')
else: # Если введенное значение не целое число, то выдается сообщение об ошибке 
    print('Entered value should be an int!!!!!!!!')