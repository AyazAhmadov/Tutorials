num = input('Please enter a number: ')
valid = num.isnumeric()

while not valid:
    num = input('Wrong value is entered. Entered value should be int.\nTry again: ')
    valid = num.isnumeric()

num = int(num)

for i in range(num):
    d = i+1 # +1, потому что функция range(n) возвращает числа от 0 до n, НЕ включая n.
    # Также вместо range(num) можно использовать range(1, num+1), и эта строка кода будет не нужна
    # for i in range(1, num+1):
    #   if not (i % 3 == 0 or i % 5 == 0):
    #       print(i)

    if not (d % 3 == 0 or d % 5 == 0):
        print(d)

    # Также можно использовать ключевое слово pass
    # if d % 3 == 0 or d % 5 == 0:
        # pass
    # else:
    #   print(d)