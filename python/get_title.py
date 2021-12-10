import sys
from tmdb_dal import get_title_by_id
from errors import invalid_movieID_syntax, invalid_movieID_argument


if len(sys.argv) != 2:
    raise Exception(invalid_movieID_syntax)


try:
    movieId = int(sys.argv[1])
except ValueError:
    raise Exception(invalid_movieID_argument)
result = get_title_by_id(movieId)
if not result:
    raise Exception(invalid_movieID_argument)
print(
    f"ID: {movieId} has the title '{result}'")
