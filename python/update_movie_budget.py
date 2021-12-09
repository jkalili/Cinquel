import sys
from tmdb_dal import update_movie_budget

if len(sys.argv) != 3:
    print('Usage: update_movie_runtime <movieId> <updated_budget>')
    exit(1)


movieId = sys.argv[1]
budget = sys.argv[2]

try:
    result = update_movie_budget(int(movieId), int(budget))
    print(
        f"{movieId} has been updated to a budget of {budget}")
except ValueError:
    print(
        f'Sorry, something went wrong.')
