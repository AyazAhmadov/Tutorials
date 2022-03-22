summa = 0
count = 0

while True:
    user_input = input('Please enter a number: ')
    if user_input == 'q':
        break
    
    try:
        num = float(user_input)
    except ValueError:
        print('Entered wrong value. Should be a number')
    else:
        summa += num
        count += 1
    finally:
        print('Something')

avg = summa/count
r_avg = round(avg, 2)

print('Mean average: ', r_avg)