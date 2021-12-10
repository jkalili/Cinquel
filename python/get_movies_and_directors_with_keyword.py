import sys
from tmdb_dal import get_movies_and_directors_with_keyword
from errors import invalid_movie_director_keyword_argument, invalid_movie_director_keyword_syntax
if len(sys.argv) != 2:
    raise Exception(invalid_movie_director_keyword_syntax)
    exit(1)


keyword = sys.argv[1]
result = get_movies_and_directors_with_keyword(keyword)
if not result:
    raise Exception(invalid_movie_director_keyword_argument)
print(
    f'\nYour query returned {len(result)} movies pertaining to "{keyword}":\n')
for entry in result:
    print(
        f'movie: {entry["r2"][0]["title"]} | directed by: {entry["c"]["crewID"]}\n')
