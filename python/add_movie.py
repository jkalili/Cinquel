import sys
from tmdb_dal import insert_movie, does_id_exist
from errors import invalid_add_syntax, invalid_add_argument, invalid_add_id

if len(sys.argv) != 9:
    raise Exception(invalid_add_argument)
    exit(1)
if does_id_exist(int(sys.argv[2])):
    raise Exception(invalid_add_id)
try:
    budget = int(sys.argv[1])
    movieId = int(sys.argv[2])
    original_language = sys.argv[3]
    popularity = float(sys.argv[4])
    release_date = sys.argv[5]
    runtime = int(sys.argv[6])
    title = sys.argv[7]
    vote_average = float(sys.argv[8])
except ValueError:
    raise Exception(invalid_add_syntax)
movie = insert_movie(budget, movieId, original_language,
                     popularity, release_date, runtime, title, vote_average)
print(f"Movie “{movie.get('title')}” added with id {movieId} ")
