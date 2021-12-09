import sys
from tmdb_dal import insert_movie

if len(sys.argv) != 9:
    print('Usage: add_movie <budget> <movieId> <original_language> <popularity> <release_date> <runtime> <title> <vote_average>')
    exit(1)

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
    raise Exception('Please regard the following format: <budget: int> <movieId: str> <original_language: str> <popularity: float> <release_date: Date> <runtime: int> <title: str> <vote_average: float>')

movie = insert_movie(budget, movieId, original_language,
                     popularity, release_date, runtime, title, vote_average)
print(f"Movie “{movie.get('title')}” added with id {movieId} ")
