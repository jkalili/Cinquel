import sys
from tmdb_dal import update_movie_vote_average
from errors import invalid_movieID_argument, invalid_update_vote_argument, invalid_update_vote_syntax

if len(sys.argv) != 3:
    raise Exception(invalid_update_vote_syntax)

try:
    movieId = sys.argv[1]
    vote_average = sys.argv[2]
except ValueError:
    raise Exception(invalid_update_vote_argument)

result = update_movie_vote_average(int(movieId), float(vote_average))
if not result:
    raise Exception(invalid_movieID_argument)

print(
    f"{movieId} has been updated with a vote average of {vote_average}")
