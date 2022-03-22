# Хотим срздать функции для сложения 2 чисел
def add(x, y):
    summa = x + y
    print(f'Sum of number is: {summa}')

# add(4, 8)

def add_default(x, y=3):
    summa = x + y
    print(f'Sum of number is: {summa}')

# add_default(10, y=15)

def avg_numbers(*numbers):
    summa = 0

    for num in numbers:
        summa += num

    avg = summa/len(numbers)
    
    return avg

# avg_numbers(1, 2, 3)
# avg_nums = avg_numbers(1, 2, 3, 4, 5)
# print(avg_nums)
# sqr_avgs = avg_nums**2
# print(sqr_avgs)

def avg_list(lst):
    summa = sum(lst)
    avg = summa/len(lst)

    print(avg)

# avg_list([1, 2, 3, 4, 5, 6, 7, 8, 9])

# x = 8

def foo():
    global x
    x = 5
    print('-----')
    print(x)
    print('-----')

# print(x)
# foo()
# print(x)

# Docstring
def fibonacci(n, cache={}):
    """Returns nth element in fibonacci sequence.

    Args:
        n (int): Order of the element
        cache (dict, optional): Cache of the previous values. Defaults to {}.

    Raises:
        TypeError: Raised if argument 'n' is not of type int.
        ValueError: Raised if argument 'n' is smaller or equal to 0.

    Returns:
        int: Nth element of fibonacci
    """
    if not isinstance(n, int):
        raise TypeError(f"'n' should be of type int and not {type(n).__name__}")

    if n < 1:
        raise ValueError("'n' should be a positive integer")

    if n in cache:
        return cache[n]

    if n == 1:
        value = 0
    elif n == 2:
        value = 1
    else:
        value = fibonacci(n-2) + fibonacci(n-1)

    cache[n] = value
    return value

def print_n_fibonacci(n):
    for i in range(1, n+1):
        val = fibonacci(i)
        print(f'{i}: {val}')

# import time

# t1 = time.time()
# print_n_fibonacci(40)
# t2 = time.time()
# print(f'Time to execute: {t2-t1}s')

avg_two_numbers = lambda x, y: (x+y)/2

# avg = avg_two_numbers(2, 9)
# print(avg)

# names = ['Ayaz', 'Seymur', 'Imad', 'Sabir', 'Ali', 'Ceka', 'Rufat']

# sorted_names = sorted(names, key=lambda name: name[-1], reverse=True)
# filtered_names = filter(lambda name: len(name) <= 4, names)
# print(list(filtered_names))

# numbers = list(range(1, 31))

# even_numbers = filter(lambda x: x%2==0, numbers)
# print(numbers)
# print(list(even_numbers))

# numbers = list(range(1, 11))

# sqrd_numbers = map(lambda num: num**2, numbers)
# print(list(sqrd_numbers))