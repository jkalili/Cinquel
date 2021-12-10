import sys
from tmdb_dal import update_movie_original_language
from errors import invalid_language_syntax, invalid_language_argument, invalid_movieID_argument

if len(sys.argv) != 3:
    raise Exception(invalid_language_syntax)
    exit(1)

try:
    movieId = sys.argv[1]
    original_language = sys.argv[2]
except ValueError:
    raise Exception(invalid_language_argument)

result = update_movie_original_language(
    int(movieId), original_language)
if not result:
    raise Exception(invalid_movieID_argument)
print(
    f"{movieId} has been updated to a original language of {original_language}")
