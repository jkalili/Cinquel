import sys
from tmdb_dal import update_movie_popularity

if len(sys.argv) != 3:
    print('Usage: update_movie_popularity <movieId> <updated_popularity>')
    exit(1)


movieId = sys.argv[1]
popularity = sys.argv[2]

try:
    result = update_movie_popularity(int(movieId), int(popularity))
    print(
        f"{movieId} has been updated to a popularity of {popularity}")
except ValueError:
    print(
        f'Sorry, something went wrong.')
