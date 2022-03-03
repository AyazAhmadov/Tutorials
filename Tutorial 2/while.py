x = 10

while x > 0:
    print(x)
    x -= 1

# pass
# continue
# break

running = True

while running:
    num = input('Please enter a number: ')
    if num == 'q':
        running = False
        continue
    
    num = int(num)
    if num % 2 == 0:
        print('even')
    else:
        print('uneven')

while True:
    num = input('Please enter a number: ')
    if num == 'q':
        break
    
    num = int(num)
    if num % 2 == 0:
        print('even')
    else:
        print('uneven')