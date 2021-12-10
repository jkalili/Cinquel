import sys
from tmdb_dal import update_movie_popularity
from errors import invalid_popularity_argument, invalid_popularity_syntax, invalid_movieID_argument

if len(sys.argv) != 3:
    raise Exception(invalid_movieID_syntax)
    exit(1)

try:
    movieId = sys.argv[1]
    popularity = sys.argv[2]
except ValueError:
    raise Exception(invalid_popularity_argument)

result = update_movie_popularity(int(movieId), int(popularity))
if not result:
    raise Exception(invalid_movieID_argument)
print(
    f"{movieId} has been updated to a popularity of {popularity}")
