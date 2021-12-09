import sys
from tmdb_dal import update_movie_release_date

if len(sys.argv) != 3:
    print('Usage: update_movie_release_date <movieId> <updated_release_date>')
    exit(1)


movieId = sys.argv[1]
release_date = sys.argv[2]

try:
    result = update_movie_release_date(int(movieId), release_date)
    print(
        f"{movieId} has been updated to a release date of {release_date}")
except ValueError:
    print(
        f'Sorry, something went wrong.')
