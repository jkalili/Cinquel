import sys
from tmdb_dal import remove_movie, does_id_exist
from errors import invalid_movie_syntax, invalid_movieID_argument, invalid_movie_id
if len(sys.argv) != 2:
    raise Exception(invalid_movie_syntax)

try:
    movieId = int(sys.argv[1])
except ValueError:
    raise Exception(invalid_movieID_argument)

if not does_id_exist(movieId):
    raise Exception(invalid_movie_id)

movie = remove_movie(int(movieId))

print(
    f"Movie with ID:{movieId} has been removed")
