# Polucheniye chisel i operatora
x = input("Plese enter the first number:\n")
operator = input('Please enter the operator:\n')
y = input('Please enter the second number:\n')

# Проверяем если введенные значения это числа
if x.isnumeric() and y.isnumeric():
    print('========================')
else:
    print('One or both of the values is not a number!!!!!!!!!!!!!')

# Проверяем оператор
if operator == '+':
    result = x + y
elif operator == '-':
    result = x - y
elif operator == '*':
    result = x * y
elif operator == '/':
    result = x / y
elif operator == '**':
    result = x ** y
else:
    result = 'Wrong operator!!!!!' # Проверка если оператор какая-то хуйня

print(result)