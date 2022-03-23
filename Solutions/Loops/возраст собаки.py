age = input('Please enter dog\'s age in human years: ') # Обратный слеш в строке нужен для того, чтобы сказать питону, что одиночная кавычка часть строки, а не часть кода. Попробуйте не использовать обратный слеш, и проверьте какой будет результат

if not age.isnumeric():
    print('Invalid type. Age should be a positive int.')

age = int(age)

if age < 0:
    print('Age must be positive')

# С помощью циклов
dog_age = 0

for i in range(int(age)):
    num = i+1 # +1, потому что функция range(n) возвращает числа от 0 до n, НЕ включая n
    if num > 2:
        dog_age += 4
    else:
        dog_age += 10.5

# Без циклов
if int(age) > 2:
    dog_age = 2*10.5 + (age-2)*4
else:
    dog_age = age * 10.5

print(f'Dog\'s age in dog years is: {dog_age}')