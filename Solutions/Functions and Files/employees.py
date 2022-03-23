def read_file(file_path):
    with open(file_path) as f:
        data = [[val.strip() for val in line.split(';')] for line in f.readlines()[1:]]

    return data

def count_cities(data):
    cities = {}
    for employee in data:
        id, name, last_name, city = employee
        if city in cities:
            cities[city] += 1
        else:
            cities[city] = 1

    return cities

def write_to_file(file_path, cities):
    content = []
    for city, number in cities.items():
        sentence = f'Количество работников в городе {city}: {number}'
        content.append(sentence)

    with open(file_path, 'w') as f:
        f.write('\n'.join(content))

data = read_file('Tutorial 3\examples\employees.csv')
cities = count_cities(data)
write_to_file(cities)