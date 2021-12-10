import sys
from tmdb_dal import update_movie_runtime
from errors import invalid_movieID_argument, invalid_runtime_argument, invalid_runtime_syntax
if len(sys.argv) != 3:
    raise Exception(invalid_runtime_syntax)
    exit(1)

try:
    movieId = sys.argv[1]
    runtime = int(sys.argv[2])
except ValueError:
    raise Exception(invalid_runtime_argument)

result = update_movie_runtime(int(movieId), int(runtime))
if not result:
    raise Exception(invalid_movieID_argument)
print(
    f"Movie with ID {movieId} has been updated to a runtime of {runtime}")
