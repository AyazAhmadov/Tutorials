user_input = input('Plese enter a number: ')
num = int(user_input)

while num > 20:
    user_input = input('Wrong value. Number should be less or equal to 10.\nPlese enter a number: ')
    num = int(user_input)

header = ' '*3 + '||'

# Эта часть программы печатает заглавную строку.
for i in range(1, num+1):
    length_i = len(str(i)) # Получаем длину числа, чтобы знать сколько поставить пробелов между предыдущим числом и нынешним 
    num_of_spaces = 3 - length_i # Количество пробелов. Длина каждой клетки в таблице 3. Если число состоит из одной цифры, то до нее поставится два пробела. Если два - один пробел. Если три цифры то пробел не поставится
    header += ' '*num_of_spaces + str(i) + '|' # К строке добавляются пробелы, и число
print(header)
print('='*len(header)) # Разделитель. Это знак "=". Количество зависит от длины заглавной строки

for i in range(1, num+1):
    length_i = len(str(i)) #
    num_of_spaces = 3 - length_i #
    to_print = str(i) + ' '*num_of_spaces + '||' #
    for j in range(1, num+1):
        product = i*j #
        length_product = len(str(product)) #
        num_of_spaces = 3 - length_product #
        to_print += ' '*num_of_spaces #
        to_print += str(product) #
        to_print += '|' #
    print(to_print) #
    print('-'*len(to_print)) #