summa = 0
count = 0

while True:
    user_input = input('Please enter a number: ')

    if user_input == 'q':
        break
    
    num = float(user_input)
    summa += num
    count += 1

avg = summa/count
r_avg = round(avg, 2)

print('Mean average: ', r_avg)