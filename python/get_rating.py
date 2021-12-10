import sys
from tmdb_dal import get_average_rating, does_id_exist
from errors import invalid_rating_argument, invalid_rating_syntax, invalid_rating_id

if len(sys.argv) != 2:
    raise Exception(invalid_rating_syntax)
    exit(1)

try:
    movieId = int(sys.argv[1])
except ValueError:
    raise Exception(invalid_rating_argument)

result = get_average_rating(movieId)
if not result:
    raise Exception(invalid_rating_id)
print(f"{movieId} has an average rating of {result}")
