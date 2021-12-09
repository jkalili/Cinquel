import sys
from tmdb_dal import get_average_rating, does_id_exist

if len(sys.argv) != 2:
    print('Usage: get_rating <movieId>')
    exit(1)


movieId = sys.argv[1]
invalid_id = (
    f'Sorry, the movie id "{movieId}" is invalid.')
result = get_average_rating(int(movieId))
if not result:
    raise Exception(invalid_id)
print(f"{movieId} has an average rating of {result}")
