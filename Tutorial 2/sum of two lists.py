# К каждому числу в списке lst суммируем все числа в списке lst2 и добавляем в список result
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
lst2 = [11, 12, 13, 14, 15, 16, 17, 18, 19]

result = []

for num1 in lst: # Для каждого числа в списке lst
    summa = 0 # Изначальная сумма равна 0
    for num2 in lst2: # Суммируем все числа в списке lst2
        summa += num2
    summa += num1 # Добавляем к сумме число из списка lst
    result.append(summa) # Добавляем в список result

print(result)