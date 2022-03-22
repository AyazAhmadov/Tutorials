summa = 0
counter = 0

message = 'Please enter a number or \'q\': '

while True:
    user_input = input(message)

    if not user_input.replace('.', '', 1).isnumeric() and user_input != 'q':
        message = 'Wrong value is entered. Entered value should be int.\nPlease enter a number or \'q\': '
        continue
    else:
        message = 'Please enter a number or \'q\': '

    if user_input == 'q':
        break

    num = float(user_input)
    summa += num
    counter += 1

    print('===============') # Разделитель

avg = summa / counter
avg_rnd = round(avg, 2)
print(f'Average value of numbers is: {avg_rnd}')