# Получаем числа
x = float(input('Please eter the first number:\n'))
y = float(input('Please enter the second number:\n'))

# Сравнение
if x > y: # если х больше чем
    print('x is bigger than y')
elif x == y: # а если х меньше чем у
    print('x is equal to y')
else: # в любом другом случае (если х равен у)
    print('x is not bigger than y')
# else if