# file = open(r'Tutorial 3\examples\the-zen-of-python.txt')
# text = file.read()
# file.close()

# with open(r'Tutorial 3\examples\the-zen-of-python.txt', 'r') as file:
#     text = file.read()

# with open(r'Tutorial 3\examples\uni.txt', 'r', encoding='utf-8') as f:
#     text = f.read()

# with open(r'Tutorial 3\examples\maad_city.txt') as f:
#     text = f.read()

# text_replaces = text.replace('nigga', 'n**ga')

# with open(r'Tutorial 3\examples\maad_city_censored.txt', 'w') as f:
#     f.write(text_replaces)

# comma separated values
def open_file(file_path):
    with open(file_path, 'r') as f:
        data = f.readlines()

    return data

def parse_data(data):
    all_movies = []
    for d in data[1:]:
        movie = d.split(',')
        year = int(movie[0])
        score = int(movie[1])
        if len(movie) > 3:
            title = ', '.join(movie[2:])
            title = title.replace('"', '').strip()
        else:
            title = movie[2].replace('"', '').strip()

        parsed_movie = [year, score, title]
        all_movies.append(parsed_movie)

    return all_movies

def highest_scored_movie(movies):
    highest_score = 0
    highest_year = None
    highest_title = None
    for mov in movies:
        score = mov[1]
        if score > highest_score:
            highest_score = score
            highest_title = mov[2]
            highest_year = mov[0]

    print(f'Robert De Niro\'s highest scored movie is {highest_title}, release in {highest_year}, scored at {highest_score}')

data = open_file(r'Tutorial 3\examples\deniro.csv')
all_movies = parse_data(data)
# highest_scored_movie(all_movies)
highest_movie = max(all_movies, key=lambda movie: movie[1])
print(highest_movie)