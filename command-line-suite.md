# Command Line Suite for DAL

## Usage:

` DB_URL=neo4j://localhost DB_PASSWORD=<your password> python3 <function>.py [args]`

## Example:

`DB_URL=neo4j://localhost DB_PASSWORD=<your password> python3 insert_move.py Titanic`

## Formatting for args:

- For space(s) in a single arg, wrap in single quotes
  - i.e. `... remove_movie.py Saving' 'Private' 'Ryan`
- For multiple args, seperate with space(s)
  - i.e. `... update_movie_vote_average.py Saving' 'Private' 'Ryan 8.9`

## Available Functions:

### Insert/Create a Movie

`... insert_movie.py [budget] [movieId] [original_language] [popularity] [release_date] `

### Query id by movie title

` ... get_id_by_title.py [title]`

### Query movie title by id

`... get_title_by_id.py [movieId]`

### Validate movie id

`... does_id_exist.py [movieId]`

### Remove Movie by id

`... remove_movie.py [movieId]`

### Query average rating by id

`... get_average_rating.py [movieId]`

### Update movie runtime by id

`... update_movie_runtime.py [movieId] [runtime]`

### Update movie budget by id

`... update_movie_budget.py [movieId] [budget]`

### Update movie popularity by id

`... update_movie_popularity.py [movieId] [popularity]`

### Update movie release date by id

`... update_movie_release_date.py [movieId] [releaseDate]`

### Update movie original lanaguage by id

`... update_movie_original_language.py [movieId] [originalLanguage]`

### Update movie title by id

`... update_movie_title.py [movieId] [movieTitle]`

### Update movie vote average by id

`... update_movie_vote_average.py [movieId] [voteAverage]`

### Lists all movies based on performer cast id

`... get_actor_performances.py [castID]`

### Lists all movies based on keyword

`... get_movies_with_keyword.py [keyword]`

### Lists all movies where both cast id acted together

`... acted_together.py [castID] [castID]`
