# lst = []
# tpl = ()
# st = set()
# dct = {}

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Получение элемента(-ов) из списка
lst[4]
lst[2:6]
lst[2:6:2]
lst[:5]
lst[3:]

# Заменение элемета(-ов) в списке
lst[3] = 10
lst[1:4] = [10, 11, 12]
lst[1:4:2] = [10, 11]

# Проверка существования элемениа в списке
11 in lst

# Удаление элементыа из списка
del lst[4]

# Соединение списков
lst2 = [10, 11, 12, 13, 14]
lst3 = lst + lst2

# Копирование списка
lst2 = lst*2

lst.append(10)
lst.insert(3, 10)
lst.clear()
lst.remove(9) # в качестве аргумета элемент из списка

lst2 = [2, 65, 32, 90, 22, 1, -565]
lst2.sort() # Сортировка
lst2.reverse() # Обратный порядок спсика
lst3 = list(reversed(lst2)) # Обратный порядок списка (создается новый список)

num = lst.pop(2)