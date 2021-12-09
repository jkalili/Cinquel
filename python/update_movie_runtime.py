import sys
from tmdb_dal import update_movie_runtime

if len(sys.argv) != 3:
    print('Usage: update_movie_runtime <movieId> <updated_runtime>')
    exit(1)


movieId = sys.argv[1]
runtime = sys.argv[2]

try:
    result = update_movie_runtime(int(movieId), int(runtime))
    print(
        f"{movieId} has been updated to a runtime of {runtime}")
except ValueError:
    print(
        f'Sorry, something went wrong.')
