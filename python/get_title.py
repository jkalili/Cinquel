import sys
from tmdb_dal import get_title_by_id

if len(sys.argv) != 2:
    print('Usage: get_title <movieId>')
    exit(1)


movieId = sys.argv[1]

try:
    result = get_title_by_id(int(movieId))
    print(
        f"ID: {movieId} has the title '{result}'")
except ValueError:
    print(
        f'Sorry, something went wrong.')
