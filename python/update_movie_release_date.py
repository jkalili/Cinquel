import sys
from tmdb_dal import update_movie_release_date
from errors import invalid_movieID_argument, invalid_date_argument, invalid_date_syntax

if len(sys.argv) != 3:
    raise Exception(invalid_date_syntax)
    exit(1)

try:
    movieId = sys.argv[1]
    release_date = sys.argv[2]
except ValueError:
    raise Exception(invalid_date_argument)

result = update_movie_release_date(int(movieId), release_date)
if not result:
    raise Exception(invalid_movieID_argument)

print(f"{movieId} has been updated to a release date of {release_date}")
