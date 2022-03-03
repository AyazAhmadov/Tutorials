dct = {'Seymur': 30, 'Imad': 24, 'Ayaz': 23, 'Sabir': 22, 'Ali': 28}
# countries = {'Azerbaijan': 'Baku', 'Spain': 'Madrid', 'USA': 'Washington', 'Austria': 'Vienna'}

# website = {'num_of_users': 123131, 'average_speed': 24}
# print(website['average_speed'])

# spain = countries.pop('Spain')
# spain = countries.pop('Spain')
# austria = countries.popitem()

# countries.update({'Germany': 'Berlin'})
# countries |= {'France': 'Paris'}

# new_dict = dct | countries

# print(new_dict)

# summa = 0
# for age in dct.values():
#     print(age)
#     summa += age

# print('+++++++++++++++++++++++++')
# print(summa)

# for name in dct.keys():
#     print(name)

summa = 0
for name, age in dct.items():
    print(name)
    summa += age

print('==========================')
print(summa)