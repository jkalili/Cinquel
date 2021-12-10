import sys
from tmdb_dal import update_movie_budget
from errors import invalid_movieID_argument, invalid_movie_budget_argument, invalid_movie_budget_syntax
if len(sys.argv) != 3:
    raise Exception(invalid_movie_budget_syntax)
    exit(1)

try:
    movieId = sys.argv[1]
    budget = sys.argv[2]
except ValueError:
    raise Exception(invalid_movie_budget_argument)

result = update_movie_budget(int(movieId), int(budget))
if not result:
    raise Exception(invalid_movieID_argument)
print(
    f"{movieId} has been updated to a budget of {budget}")
