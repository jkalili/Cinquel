import sys
from tmdb_dal import update_movie_original_language

if len(sys.argv) != 3:
    print('Usage: update_movie_original_language <movieId> <updated_original_language>')
    exit(1)


movieId = sys.argv[1]
original_language = sys.argv[2]

try:
    result = update_movie_original_language(
        int(movieId), original_language)
    print(
        f"{movieId} has been updated to a original language of {original_language}")
except ValueError:
    print(
        f'Sorry, something went wrong.')
