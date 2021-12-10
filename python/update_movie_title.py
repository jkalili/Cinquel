import sys
from tmdb_dal import update_movie_title
from errors import invalid_movieID_argument, invalid_update_title_argument, invalid_update_title_syntax
if len(sys.argv) != 3:
    raise Exception(invalid_update_title_syntax)
    exit(1)

try:
    movieId = sys.argv[1]
    title = sys.argv[2]
except ValueError:
    raise Exception(invalid_title_argument)

result = update_movie_title(int(movieId), title)
if not result:
    raise Exception(invalid_movieID_argument)

print(
    f"{movieId} has been updated with a title of {title}")
