first_number = input('Please enter the first number: ') # Получаем первое число
second_number = input('Please enter the second number: ') # Получаем второе число

# Из-за того, что isnumeric() проверяет только целые числа, а мы хотим также десятичные числа, нужно провести пару махинаций
# чтобы также возмрдно было проверить десятичные числа. Для этого, я избавился от точки при помощи функции replace(), заменив первую попавшуюся точку "."
# (поэтому функции был дан аргумент 1 (смотреть скрипт str.pdf)) на пустую строку "". Оставшуюся строку уже можно проверить при помощи isnumeric().
if first_number.replace('.', '', 1).isnumeric() and second_number.replace('.', '', 1).isnumeric():
    x = float(first_number)
    y = float(second_number)
    d = abs(x-y) # Находим абсолютное значение. Если х < у, то разница будет отрицательная и ее не получится проверить на больше чем 1000, потому что отрицательное число никогда не будет больше чем 1000
    # Также можно вычеслить разницу взависимости от результат сравнения. Если х больше чем у то d = х - у. Если х меньше чем у d = у - х
    if x > y: # Если х больше чем у
        # d = х - у
        if d >= 1000:
            print('First number is much bigger than the second number')
        else:
            print('First number is a little bigger than the second number')
    elif x < y: # А если х меньше чем у
        # d = у - х
        if d >= 1000:
            print('First number is much smaller than the second number')
        else:
            print('First number is a little smaller than the second number')
    else: # В противном случае они равны
        print('First number is equal to the second number')
else: # Если введенное значение не число, то выдается сообщение об ошибке 
    print('Entered value should be numeric (int or float) !!!!!!')
