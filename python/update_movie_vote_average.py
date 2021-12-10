import sys
from tmdb_dal import update_movie_vote_average

if len(sys.argv) != 3:
    print('Usage: update_movie_vote_average <movieId> <updated_vote_average>')
    exit(1)


movieId = sys.argv[1]
vote_average = sys.argv[2]

try:
    result = update_movie_vote_average(int(movieId), float(vote_average))
    print(
        f"{movieId} has been updated with a vote average of {vote_average}")
except ValueError:
    print(
        f'Sorry, something went wrong.')
