all_nums = {1, 2, 3, 4, 5, 6, 7, 8, 9}
even_nums = {2, 4, 6, 8}
odd_nums = {1, 3, 5, 7, 9}

# iterate
# Можно итерировать
for num in all_nums:
    print(num)

# Объединение
st = even_nums.union(odd_nums)
st = even_nums | odd_nums

# Пересечение
st = all_nums.intersection(even_nums)
all_nums & even_nums

# Разница
st = all_nums.difference(even_nums)
all_nums - even_nums

all_nums.update({10, 11, 12, 13})

all_nums.add(10)
all_nums.remove(11)
all_nums.discard(11)
all_nums.clear()
num_9 = all_nums.pop()
num_8 = all_nums.pop()