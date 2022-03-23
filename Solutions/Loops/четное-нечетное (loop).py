even = 0
odd = 0

message = 'Please enter a number or \'q\': '

while True:
    user_input = input(message)

    if not user_input.isnumeric() and user_input != 'q':
        message = 'Wrong value is entered. Entered value should be int.\nPlease enter a number or \'q\': '
        continue
    else:
        message = 'Please enter a number or \'q\': '

    if user_input == 'q':
        break

    num = int(user_input)

    if num % 2 == 0:
        even += 1
    else:
        odd += 1
    print('==========================') # Разделитель

print(f'Number of even numbers: {even}')
print(f'Number of odd numbers: {odd}')