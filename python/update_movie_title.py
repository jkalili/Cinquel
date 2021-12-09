import sys
from tmdb_dal import update_movie_title

if len(sys.argv) != 3:
    print('Usage: update_movie_title <movieId> <updated_title>')
    exit(1)


movieId = sys.argv[1]
title = sys.argv[2]

try:
    result = update_movie_title(int(movieId), title)
    print(
        f"{movieId} has been updated with a title of {title}")
except ValueError:
    print(
        f'Sorry, something went wrong.')
